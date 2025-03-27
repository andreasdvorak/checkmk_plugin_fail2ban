#!/bin/bash
#
# Script to copy the source files to the CheckMK site directories.
# It should only be used for testing.
# Better install the package (mkp).

mkdir -p ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based
cp cmk_addons/plugins/agent_based/fail2ban.py ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/fail2ban.py
chown $USER ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/fail2ban.py
chmod 755   ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/fail2ban.py

mkdir -p ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets
cp cmk_addons/plugins/rulesets/ruleset_fail2ban.py ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban.py
chown $USER ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets
chmod 755   ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban.py

# There is no bakery in CheckMK RAW
if [ -d ~/local/lib/check_mk/base/cee/plugins/bakery ]
then
    cp cmk_addons/plugins/rulesets/ruleset_fail2ban_bakery.py ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban_bakery.py
    chown $USER ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets
    chmod 755   ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/ruleset_fail2ban_bakery.py
fi

mkdir -p ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing
cp cmk_addons/plugins/graphing/graphing_fail2ban.py ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing/graphing_fail2ban.py
chown $USER ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing/graphing_fail2ban.py
chmod 755   ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing/graphing_fail2ban.py

# There is no bakery in CheckMK RAW
if [ -d ~/local/lib/check_mk/base/cee/plugins/bakery ]
then
    cp lib/fail2ban_bakery.py   ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban_bakery.py
    chown $USER ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban_bakery.py
    chmod 755   ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban_bakery.py
fi

cp check_mk_agent/plugins/fail2ban.sh ~/local/share/check_mk/agents/plugins/fail2ban.sh
chown $USER ~/local/share/check_mk/agents/plugins/fail2ban.sh
chmod 755   ~/local/share/check_mk/agents/plugins/fail2ban.sh

rm -f ~/local/lib/python3/cmk_addons/plugins/fail2ban/agent_based/__pycache__/*
rm -f ~/local/lib/python3/cmk_addons/plugins/fail2ban/rulesets/__pycache__/*
rm -f ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing/__pycache__/*
