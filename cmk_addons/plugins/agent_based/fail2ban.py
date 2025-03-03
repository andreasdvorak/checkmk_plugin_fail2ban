#!/usr/bin/env python3
#
# CheckMK server part of the plugin to create services from the raw data.
# target directory: ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/

# Example for output from agent
# ---------------------------------------------------------
#<<<fail2ban:sep(58)>>>
#Status for the jail: ssh
#|- Filter
#|  |- Currently failed: 1
#|  |- Total failed:     21053
#|  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
#`- Actions
#   |- Currently banned: 5
#   |- Total banned:     78
#   `- Banned IP list:   188.162.1.237 118.122.129.4 218.90.144.222 115.216.102.101 140.245.39.158
#Status for the jail: sshd
#|- Filter
#|  |- Currently failed: 1
#|  |- Total failed:     21053
#|  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
#`- Actions
#   |- Currently banned: 1
#   |- Total banned:     72
#   `- Banned IP list:   140.245.39.158

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric, check_levels, DiscoveryResult, CheckResult, StringTable

from typing import Any, Mapping

Section = Mapping[str, Mapping[str, str]]

def parse_fail2ban(string_table: StringTable) -> Section:
    parsed = {}
    currentjail = None
    for line in string_table:
        if ' ' not in line[0]:
            # Re-split on : instead of space
            line = " ".join(line).split(":")

        if len(line) != 2:
            # Not a key-value pair
            continue

        key = line[0].strip("|-` ")
        value = line[1].strip()

        if key == 'Status for the jail':
            currentjail = value
            parsed[currentjail] = dict()
        elif currentjail is not None:
            try:
                parsed[currentjail][key] = int(value)
            except ValueError:
                # we are only interested in the numeric values
                pass
    return parsed


def discovery_fail2ban(section: Section) -> DiscoveryResult:
    for jail in section:
        yield Service(item=jail)

def check_fail2ban(
    item: str,
    params: Mapping[str, Any],
    section: Section,
) -> CheckResult:
    try:
        data = section[item]
    except KeyError:
        # removed jails should not create a crash,
        # so we dont yield anything and simply return without anything
        return

    for what in ("failed", "banned"):
        current_key = f"Currently {what}"
        total_key = f"Total {what}"
        yield from check_levels(
            metric_name=f"current_{what}",
            value=data[current_key],
            levels_upper=params[what],
            label=current_key,
            render_func=int,
        )
        yield from check_levels(
            metric_name=f"total_{what}",
            value=data[total_key],
            notice_only=True,
            label=total_key,
            render_func=int,
        )

agent_section_fail2ban = AgentSection(
    name = "fail2ban",
    parse_function = parse_fail2ban,
)

check_plugin_fail2ban = CheckPlugin(
    name = "fail2ban",
    service_name = "Fail2Ban Jail %s",
    discovery_function = discovery_fail2ban,
    check_function = check_fail2ban,
    check_default_parameters = {"banned": ("fixed", (10, 20)), "failed": ("fixed", (30, 40))},
    check_ruleset_name = "fail2ban",
)