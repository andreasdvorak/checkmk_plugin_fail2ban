#!/bin/bash
#
# Script to copy the source files to the CheckMK site directories

cp cmk_addons/plugins/rulesets/ruleset_fail2ban.py ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban.py
chown $USER ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban.py
chmod 755   ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban.py

#cp web/plugins/metrics/fail2ban_metric.py ~/local/share/check_mk/web/plugins/metrics/fail2ban_metric.py
#chown $USER ~/local/share/check_mk/web/plugins/metrics/fail2ban_metric.py
#chmod 755   ~/local/share/check_mk/web/plugins/metrics/fail2ban_metric.py

#mkdir -p ~/local/lib/check_mk/base/cee/plugins/bakery/
#cp lib/check_mk/base/cee/plugins/bakery/fail2ban.py   ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban.py
#chown $USER ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban.py
#chmod 755   ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban.py

#cp share/check_mk/checkman/fail2ban ~/local/share/check_mk/checkman/fail2ban
#chown $USER ~/local/share/check_mk/checkman/fail2ban
#chmod 755   ~/local/share/check_mk/checkman/fail2ban

cp cmk_addons/plugins/agent_based/fail2ban_checks.py ~/local/lib/check_mk/base/plugins/agent_based/fail2ban_checks.py
chown $USER ~/local/lib/check_mk/base/plugins/agent_based/fail2ban_checks.py
chmod 755   ~/local/lib/check_mk/base/plugins/agent_based/fail2ban_checks.py

cp check_mk_agent/plugins/fail2ban.sh ~/local/share/check_mk/agents/plugins/fail2ban.sh
chown $USER ~/local/share/check_mk/agents/plugins/fail2ban.sh
chmod 755   ~/local/share/check_mk/agents/plugins/fail2ban.sh

#cp web/plugins/wato/fail2ban_bakery.py ~/local/share/check_mk/web/plugins/wato/fail2ban_bakery.py
#chown $USER ~/local/share/check_mk/web/plugins/wato/fail2ban_bakery.py
#chmod 755   ~/local/share/check_mk/web/plugins/wato/fail2ban_bakery.py

rm -f ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/__pycache__/*
rm -f ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/__pycache__/*

