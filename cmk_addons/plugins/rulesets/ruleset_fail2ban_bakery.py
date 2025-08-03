#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Shebang only needed for editor!

"""CheckMK ruleset for bakery"""

# ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban_bakery.py

from cmk.rulesets.v1 import Label, Title
from cmk.rulesets.v1.form_specs import (
    DefaultValue,
    DictElement,
    Dictionary,
    TimeSpan,
    TimeMagnitude
)
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic

def _parameter_form_bakery():
    return Dictionary(
        elements = {
            "interval": DictElement(
                parameter_form = TimeSpan(
                    title = Title("Run asynchronously"),
                    label = Label("Interval for collecting data"),
                    displayed_magnitudes = [TimeMagnitude.SECOND, TimeMagnitude.MINUTE],
                    prefill = DefaultValue(300.0),
                )
            )
        }
    )

rule_spec_fail2ban_bakery = AgentConfig(
    name = "fail2ban",
    title = Title("Fail2Ban (Linux)"),
    topic = Topic.APPLICATIONS,
    parameter_form = _parameter_form_bakery,
)
