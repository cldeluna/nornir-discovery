# Example from Patrick Ogenstad at Networklore
# https://networklore.com/introducing-nornir
# https://blogs.cisco.com/developer/nornir-python-automation-framework
from nornir.core import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result

nornir_object = InitNornir()

result = nornir_object.run(
             napalm_get,
             getters=['get_facts'])

print_result(result)