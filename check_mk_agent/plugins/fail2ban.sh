#!/bin/sh
#
# CheckMK agent plugin
# target directory on CheckMK site: ~/local/share/check_mk/agents/plugins/
# target directory on CheckMK agent host: /usr/lib/check_mk_agent/plugins/
#

if command -v fail2ban-client > /dev/null 2>&1; then
	echo "<<<fail2ban:sep(58)>>>"
	fail2ban-client status |
		awk -F: '$1 ~ /Jail list$/ { gsub(/,/, "", $2); print $2}' |
		xargs -n1 fail2ban-client status
fi
