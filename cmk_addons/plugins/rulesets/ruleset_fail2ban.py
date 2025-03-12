#!/usr/bin/env python3
#
# target directory: ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/

"""CheckMK plugin file to create rules for the parameter"""

from cmk.rulesets.v1 import Title
from cmk.rulesets.v1.form_specs import \
      DefaultValue, DictElement, Dictionary, Integer, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import \
      CheckParameters, HostAndItemCondition, Topic

def _parameter_form():
    return Dictionary(
        elements = {
            "banned": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Number of banned IPs"),
                    form_spec_template = Integer(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(10, 20)),
                ),
                required = True,
            ),
            "failed": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Number of failed IPs"),
                    form_spec_template = Integer(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(30, 40)),
                ),
                required = True,
            ),
        }
    )

rule_spec_fail2ban = CheckParameters(
    name = "fail2ban",
    title = Title("Fail2Ban level"),
    topic = Topic.GENERAL,
    parameter_form = _parameter_form,
    condition = HostAndItemCondition(item_title=Title("Service name of Jail")),
)
