# First Nornir Test Run - Discovery
## Get Facts

## Summary

First test with Nornir.

This was my first use of Nornir.  I started out with the sample get facts run_nornir.py script from from [Patrick Ogenstad at Networklore.](https://networklore.com/introducing-brigade/)

The first_nornir.py script is my attempt to decompose the objects and resulting data structures.

I'm fairly excited about this!  It took me about 45 minutes to get things set up on my Windows 10 system.  It took
almost no time at all on my Mac.

Using PyCharm on my mac the print_result output is formatted and color coded nicely.  Using PyCharm on my Windows 10
system the output is less colorful.

My next Sunday afternoon project will involve generating configurations and applying them.

## Code Example

Like Ansible, Nornir will leverage a set of inventory data.  Here you see a very basic groups.yaml file which
can also contain a default section for more general values and a hosts.yaml file which can reference specific
or more general group settings defined in the groups.yaml file.  These files can take any key:value pair and the values
with the "Nornir_" prefix have special meaning as you would expect.



groups.yaml

        ---
        uwaco_network:
          Nornir_username: cisco
          Nornir_password: cisco
          Nornir_nos: ios

hosts.yaml

        ---
        eu-med-as01:
          Nornir_host: 10.1.10.25
          groups: ['uwaco_network']
      
        arctic-ds01-as01:
          Nornir_host: 10.1.10.26
          groups: ['uwaco_network']


The first part of the first_nornir.py script initializes a Nornir object called nornir_instance.  

```
nornir_instance = InitNornir()
```

This reads in the "environment" you will act on including the host and group information.

The following sections attempt to deconstruct the objects into workable values like getting the keys of all the hosts and understanding what type of data structure was returned.  This script will pause so that you can examine the results before continuing with the next action.

```
(nornir) Claudias-iMac:nornir-discovery claudia$ python first_nornir.py
= Creating a Nornir instances which sets up a basic environment we can explore..

Hosts derived from the Inventory file are:
{'eu-med-as01': Host: eu-med-as01, 'pacific-as01': Host: pacific-as01}
    Key: eu-med-as01    Value: eu-med-as01
    Key: pacific-as01   Value: pacific-as01
Groups derived from the Inventory file are:
{'uwaco_network': Group: uwaco_network, 'uwaco_datacenter': Group: uwaco_datacenter}
    Key: uwaco_network  Value: uwaco_network
    Key: uwaco_datacenter   Value: uwaco_datacenter


== Lets "decompose" some of these instance objects so we know what we have to work with...
Decomposing Hosts object <nornir_instance.inventory.hosts>...
    Type of my_hosts is <class 'dict'>
    Host keys = ['eu-med-as01', 'pacific-as01'] of type <class 'list'>
eu-med-as01
pacific-as01

Decomposing Groups <nornir_instance.inventory.groups>...
    Group keys = ['uwaco_network', 'uwaco_datacenter'] of type <class 'list'>
uwaco_network
uwaco_datacenter


Now that we have an environment established, lets run some discovery unsing napalm getters...
Press any key to continue...s
```

```
Press any key to continue...


Decomposing Result Object of type <class 'nornir.core.task.AggregatedResult'>...
Lets turn our result object into a dictionary so that now result is of type <class 'dict'>

    Decomposing Result Object for hostname eu-med-sw01...
        Key uptime   : Value = 14880
        Key vendor   : Value = Cisco
        Key os_version   : Value = IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.06E RELEASE SOFTWARE (fc1)
        Key serial_number    : Value = FDO1821Q100
        Key model    : Value = WS-C3650-24TS
        Key hostname     : Value = eu-med-sw01
        Key fqdn     : Value = eu-med-sw01.not set
        Key interface_list   : Value = ['Vlan1', 'GigabitEthernet0/0', 'GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3', 'GigabitEthernet1/0/4', 'GigabitEthernet1/0/5', 'GigabitEthernet1/0/6', 'GigabitEthernet1/0/7', 'GigabitEthernet1/0/8', 'GigabitEthernet1/0/9', 'GigabitEthernet1/0/10', 'GigabitEthernet1/0/11', 'GigabitEthernet1/0/12', 'GigabitEthernet1/0/13', 'GigabitEthernet1/0/14', 'GigabitEthernet1/0/15', 'GigabitEthernet1/0/16', 'GigabitEthernet1/0/17', 'GigabitEthernet1/0/18', 'GigabitEthernet1/0/19', 'GigabitEthernet1/0/20', 'GigabitEthernet1/0/21', 'GigabitEthernet1/0/22', 'GigabitEthernet1/0/23', 'GigabitEthernet1/0/24', 'GigabitEthernet1/1/1', 'GigabitEthernet1/1/2', 'GigabitEthernet1/1/3', 'GigabitEthernet1/1/4']


    Decomposing Result Object for hostname pacific-sw01...
        Key uptime   : Value = 10260
        Key vendor   : Value = Cisco
        Key os_version   : Value = C2960S Software (C2960S-UNIVERSALK9-M), Version 15.2(2)E3, RELEASE SOFTWARE (fc3)
        Key serial_number    : Value = FOC1709W1DT
        Key model    : Value = WS-C2960S-24TS-S
        Key hostname     : Value = pacific-sw01
        Key fqdn     : Value = pacific-sw01.uwaco.net
        Key interface_list   : Value = ['Vlan1', 'FastEthernet0', 'GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3', 'GigabitEthernet0/4', 'GigabitEthernet0/5', 'GigabitEthernet0/6', 'GigabitEthernet0/7', 'GigabitEthernet0/8', 'GigabitEthernet0/9', 'GigabitEthernet0/10', 'GigabitEthernet0/11', 'GigabitEthernet0/12', 'GigabitEthernet0/13', 'GigabitEthernet0/14', 'GigabitEthernet0/15', 'GigabitEthernet0/16', 'GigabitEthernet0/17', 'GigabitEthernet0/18', 'GigabitEthernet0/19', 'GigabitEthernet0/20', 'GigabitEthernet0/21', 'GigabitEthernet0/22', 'GigabitEthernet0/23', 'GigabitEthernet0/24', 'GigabitEthernet0/25', 'GigabitEthernet0/26']


```

The last section uses the Nornir print_result module to print an Ansible-like status to stdout.


```
Print run results with the print_result module (this is an Ansible like run status)...
napalm_get**********************************************************************
* arctic-ds01-as01 ** changed : False ******************************************
vvvv napalm_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'get_facts': { 'fqdn': 'artic-sw01.uwaco.net',
                 'hostname': 'artic-sw01',
                 'interface_list': [ 'Vlan1',
                                     'FastEthernet0',
                                     'GigabitEthernet0/1',
                                     'GigabitEthernet0/2',
                                     'GigabitEthernet0/3',
                                     'GigabitEthernet0/4',
                                     'GigabitEthernet0/5',
                                     'GigabitEthernet0/6',
                                     'GigabitEthernet0/7',
                                     'GigabitEthernet0/8',
                                     'GigabitEthernet0/9',
                                     'GigabitEthernet0/10',
                                     'GigabitEthernet0/11',
                                     'GigabitEthernet0/12',
                                     'GigabitEthernet0/13',
                                     'GigabitEthernet0/14',
                                     'GigabitEthernet0/15',
                                     'GigabitEthernet0/16',
                                     'GigabitEthernet0/17',
                                     'GigabitEthernet0/18',
                                     'GigabitEthernet0/19',
                                     'GigabitEthernet0/20',
                                     'GigabitEthernet0/21',
                                     'GigabitEthernet0/22',
                                     'GigabitEthernet0/23',
                                     'GigabitEthernet0/24',
                                     'GigabitEthernet0/25',
                                     'GigabitEthernet0/26'],
                 'model': 'WS-C2960S-24TS-S',
                 'os_version': 'C2960S Software (C2960S-UNIVERSALK9-M), '
                               'Version 15.2(2)E3, RELEASE SOFTWARE (fc3)',
                 'serial_number': 'FOC1709W1DT',
                 'uptime': 49560,
                 'vendor': 'Cisco'}}
^^^^ END napalm_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* eu-med-as01 ** changed : False ***********************************************
vvvv napalm_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'get_facts': { 'fqdn': 'eu-med-sw01.wp.comcast.net',
                 'hostname': 'eu-med-sw01',
                 'interface_list': [ 'Vlan1',
                                     'GigabitEthernet0/0',
                                     'GigabitEthernet1/0/1',
                                     'GigabitEthernet1/0/2',
                                     'GigabitEthernet1/0/3',
                                     'GigabitEthernet1/0/4',
                                     'GigabitEthernet1/0/5',
                                     'GigabitEthernet1/0/6',
                                     'GigabitEthernet1/0/7',
                                     'GigabitEthernet1/0/8',
                                     'GigabitEthernet1/0/9',
                                     'GigabitEthernet1/0/10',
                                     'GigabitEthernet1/0/11',
                                     'GigabitEthernet1/0/12',
                                     'GigabitEthernet1/0/13',
                                     'GigabitEthernet1/0/14',
                                     'GigabitEthernet1/0/15',
                                     'GigabitEthernet1/0/16',
                                     'GigabitEthernet1/0/17',
                                     'GigabitEthernet1/0/18',
                                     'GigabitEthernet1/0/19',
                                     'GigabitEthernet1/0/20',
                                     'GigabitEthernet1/0/21',
                                     'GigabitEthernet1/0/22',
                                     'GigabitEthernet1/0/23',
                                     'GigabitEthernet1/0/24',
                                     'GigabitEthernet1/1/1',
                                     'GigabitEthernet1/1/2',
                                     'GigabitEthernet1/1/3',
                                     'GigabitEthernet1/1/4'],
                 'model': 'WS-C3650-24TS',
                 'os_version': 'IOS-XE Software, Catalyst L3 Switch Software '
                               '(CAT3K_CAA-UNIVERSALK9-M), Version 03.06.06E '
                               'RELEASE SOFTWARE (fc1)',
                 'serial_number': 'FDO1821Q100',
                 'uptime': 55260,
                 'vendor': 'Cisco'}}
^^^^ END napalm_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(nornir) Claudias-iMac:nornir-discovery claudia$

```

Windows 10 Output in PyCharm which does not render the color codes.

```
(nornir) D:\Dropbox (Indigo Wire Networks)\scripts\nornir\nornir-discovery>python run_Nornir.py
?[1m?[36mnapalm_get**********************************************************************?[0m
?[0m?[1m?[34m* arctic-ds01-as01 ** changed : False ******************************************?[0m
?[0m?[1m?[32mvvvv napalm_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO?[0m
?[0m{?[0m ?[0m'get_facts'?[0m: ?[0m{?[0m ?[0m'fqdn'?[0m: ?[0m'artic-sw01.uwaco.net'?[0m,
                 ?[0m'hostname'?[0m: ?[0m'artic-sw01'?[0m,
                 ?[0m'interface_list'?[0m: ?[0m[?[0m ?[0m?[0m'Vlan1'?[0m,
                                     ?[0m'FastEthernet0'?[0m,
                                     ?[0m'GigabitEthernet0/1'?[0m,
                                     ?[0m'GigabitEthernet0/2'?[0m,
                                     ?[0m'GigabitEthernet0/3'?[0m,
                                     ?[0m'GigabitEthernet0/4'?[0m,
                                     ?[0m'GigabitEthernet0/5'?[0m,
                                     ?[0m'GigabitEthernet0/6'?[0m,
                                     ?[0m'GigabitEthernet0/7'?[0m,
                                     ?[0m'GigabitEthernet0/8'?[0m,
                                     ?[0m'GigabitEthernet0/9'?[0m,
                                     ?[0m'GigabitEthernet0/10'?[0m,
                                     ?[0m'GigabitEthernet0/11'?[0m,
                                     ?[0m'GigabitEthernet0/12'?[0m,
                                     ?[0m'GigabitEthernet0/13'?[0m,
                                     ?[0m'GigabitEthernet0/14'?[0m,
                                     ?[0m'GigabitEthernet0/15'?[0m,
                                     ?[0m'GigabitEthernet0/16'?[0m,
                                     ?[0m'GigabitEthernet0/17'?[0m,
                                     ?[0m'GigabitEthernet0/18'?[0m,
                                     ?[0m'GigabitEthernet0/19'?[0m,
                                     ?[0m'GigabitEthernet0/20'?[0m,
                                     ?[0m'GigabitEthernet0/21'?[0m,
                                     ?[0m'GigabitEthernet0/22'?[0m,
                                     ?[0m'GigabitEthernet0/23'?[0m,
                                     ?[0m'GigabitEthernet0/24'?[0m,
                                     ?[0m'GigabitEthernet0/25'?[0m,
                                     ?[0m'GigabitEthernet0/26'?[0m]?[0m,
                 ?[0m'model'?[0m: ?[0m'WS-C2960S-24TS-S'?[0m,
                 ?[0m'os_version'?[0m: ?[0m'C2960S Software (C2960S-UNIVERSALK9-M), '?[0m
                               ?[0m'Version 15.2(2)E3, RELEASE SOFTWARE (fc3)'?[0m,
                 ?[0m'serial_number'?[0m: ?[0m'FOC1709W1DT'?[0m,
                 ?[0m'uptime'?[0m: ?[0m52440?[0m,
                 ?[0m'vendor'?[0m: ?[0m'Cisco'?[0m}?[0m}?[0m
?[0m?[1m?[32m^^^^ END napalm_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^?[0m
?[0m?[1m?[34m* eu-med-as01 ** changed : False ***********************************************?[0m
?[0m?[1m?[32mvvvv napalm_get ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO?[0m
?[0m{?[0m ?[0m'get_facts'?[0m: ?[0m{?[0m ?[0m'fqdn'?[0m: ?[0m'eu-med-sw01.wp.comcast.net'?[0m,
                 ?[0m'hostname'?[0m: ?[0m'eu-med-sw01'?[0m,
                 ?[0m'interface_list'?[0m: ?[0m[?[0m ?[0m?[0m'Vlan1'?[0m,
                                     ?[0m'GigabitEthernet0/0'?[0m,
                                     ?[0m'GigabitEthernet1/0/1'?[0m,
                                     ?[0m'GigabitEthernet1/0/2'?[0m,
                                     ?[0m'GigabitEthernet1/0/3'?[0m,
                                     ?[0m'GigabitEthernet1/0/4'?[0m,
                                     ?[0m'GigabitEthernet1/0/5'?[0m,
                                     ?[0m'GigabitEthernet1/0/6'?[0m,
                                     ?[0m'GigabitEthernet1/0/7'?[0m,
                                     ?[0m'GigabitEthernet1/0/8'?[0m,
                                     ?[0m'GigabitEthernet1/0/9'?[0m,
                                     ?[0m'GigabitEthernet1/0/10'?[0m,
                                     ?[0m'GigabitEthernet1/0/11'?[0m,
                                     ?[0m'GigabitEthernet1/0/12'?[0m,
                                     ?[0m'GigabitEthernet1/0/13'?[0m,
                                     ?[0m'GigabitEthernet1/0/14'?[0m,
                                     ?[0m'GigabitEthernet1/0/15'?[0m,
                                     ?[0m'GigabitEthernet1/0/16'?[0m,
                                     ?[0m'GigabitEthernet1/0/17'?[0m,
                                     ?[0m'GigabitEthernet1/0/18'?[0m,
                                     ?[0m'GigabitEthernet1/0/19'?[0m,
                                     ?[0m'GigabitEthernet1/0/20'?[0m,
                                     ?[0m'GigabitEthernet1/0/21'?[0m,
                                     ?[0m'GigabitEthernet1/0/22'?[0m,
                                     ?[0m'GigabitEthernet1/0/23'?[0m,
                                     ?[0m'GigabitEthernet1/0/24'?[0m,
                                     ?[0m'GigabitEthernet1/1/1'?[0m,
                                     ?[0m'GigabitEthernet1/1/2'?[0m,
                                     ?[0m'GigabitEthernet1/1/3'?[0m,
                                     ?[0m'GigabitEthernet1/1/4'?[0m]?[0m,
                 ?[0m'model'?[0m: ?[0m'WS-C3650-24TS'?[0m,
                 ?[0m'os_version'?[0m: ?[0m'IOS-XE Software, Catalyst L3 Switch Software '?[0m
                               ?[0m'(CAT3K_CAA-UNIVERSALK9-M), Version 03.06.06E '?[0m
                               ?[0m'RELEASE SOFTWARE (fc1)'?[0m,
                 ?[0m'serial_number'?[0m: ?[0m'FDO1821Q100'?[0m,
                 ?[0m'uptime'?[0m: ?[0m58140?[0m,
                 ?[0m'vendor'?[0m: ?[0m'Cisco'?[0m}?[0m}?[0m
?[0m?[1m?[32m^^^^ END napalm_get ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^?[0m
?[0m
(nornir) D:\Dropbox (Indigo Wire Networks)\scripts\nornir\nornir-discovery>

```