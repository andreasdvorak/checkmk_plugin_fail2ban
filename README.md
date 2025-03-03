# CheckMK Plugin Fail2Ban
CheckMK agent plugin to monitor fail2ban.

Tested with CheckMK 2.3.0

It uses cmk.agent_based.v2

This is my first plugin with the new API. 
I followed [Writing you own check plug-ins](https://docs.checkmk.com/latest/en/devel_check_plugins.html) and the [Guidelines](https://docs.checkmk.com/latest/en/dev_guidelines.html).

## Install from source
If you want to install the files from source clone the reppo as site user and run the script copy-to-mk.sh

## Install from package
* Download mkp.
* Install with cmk -P install fail2ban*.mkp

# Services
![Services](images/services.png?raw=true "Services")

![Service details](images/service_details.png?raw=true "Services details")

![Parameter rule](images/parameter_rule.png?raw=true "Parameter rule")

## Service parameter to configure
