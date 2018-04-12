# pyportainer
Portainer API library
----------

The usage is very simple:

```python

from pyportainer import *

user = "username"
password = "<password>"
endpoint = "<portainer-base-endpoint>"

p = PyPortainer(endpoint)
p.login(user, password)
stacks = p.get_stacks(1)
for s in stacks:
    print s.get("Name"), s.get("Env"), p.get_stackfile(1,s.get("Id"))["StackFileContent"]

```
