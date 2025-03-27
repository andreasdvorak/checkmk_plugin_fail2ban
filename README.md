# CheckMK Plugin Fail2Ban
CheckMK agent plugin to monitor fail2ban.

Tested with CheckMK 2.3.0

It uses cmk.agent_based.v2
 
I followed [Writing you own check plug-ins](https://docs.checkmk.com/latest/en/devel_check_plugins.html) and the [Guidelines](https://docs.checkmk.com/latest/en/dev_guidelines.html).

## Install from source
If you want to install the files from source clone the reppo as site user and run the script copy-to-mk.sh

## Install from package
* Download mkp from my GitHub or from [CheckMK exchange](https://exchange.checkmk.com/p/fail2ban-3)
* Install mkp [CheckMK extension packages](https://docs.checkmk.com/latest/en/mkps.html)

# Services
![Services](images/services.png?raw=true "Services")

# Service Details

![Service details](images/service_details.png?raw=true "Services details")

## Service parameter to configure

![Parameter rule](images/parameter_rule.png?raw=true "Parameter rule")

# Development

## Pylint
    pylint -d E0401 -d E0611 $(git ls-files '*.py')

## Creation of mkp
Manifest file tmp/check_mk/fail2ban.manifest.temp

```
{'author': 'Andreas Dvorak',
 'description': 'Monitoring of Fail2Ban jail',
 'download_url': 'https://github.com/andreasdvorak/checkmk_plugin_fail2ban',
 'files': {'agents': ['plugins/fail2ban.sh'],
           'cmk_addons_plugins': ['fail2ban/agent_based/fail2ban.py',
                                  'fail2ban/graphing/graphing_fail2ban.py',
                                  'fail2ban/rulesets/ruleset_fail2ban.py',
                                  'fail2ban/rulesets/ruleset_fail2ban_bakery.py'],
            'lib': ['local/lib/check_mk/base/cee/plugins/bakery/fail2ban_bakery.py']
           },
 'name': 'fail2ban',
 'title': 'Fail2ban monitoring with agent plugin',
 'version': '1.1.0',
 'version.min_required': '2.3.0',
 'version.packaged': 'cmk-mkp-tool 0.2.0',
 'version.usable_until': None
}
```

create the package

    mkp package tmp/check_mk/fail2ban.manifest.temp

Path to package: var/check_mk/packages_local