import json

import requests

class PyPortainer():
    def __init__(self, portainer_endpoint):
        self.portainer_endpoint = portainer_endpoint+"/api"
    
    def login(self, username, password):
        r = requests.post(self.portainer_endpoint+"/auth", data=json.dumps({"Username":username, "Password":password}), verify=False)
        j = r.json()
        self.token = j.get("jwt")
    
    def get_dockerhub(self):
        pass
    def put_dockerhub(self, options):
        pass
    
    def get_endpoints(self):
        r = requests.get(self.portainer_endpoint+"/endpoints", headers={"Authorization": "Bearer {}".format(self.token)}, verify=False)
        return r.json()
        
    def new_endpoints(self, options):
        pass
    def get_endpoint(self, identifier):
        pass
    def update_endpoint(self, identifier, options):
        pass
    def delete_endpoint(self, identifier):
        pass
    def access_endpoint(self, identifier, options):
        pass
    
    def get_stacks(self, endpoint):
        r = requests.get(self.portainer_endpoint + "/endpoints/{}/stacks".format(endpoint), headers={"Authorization": "Bearer {}".format(self.token)}, verify=False)
        return r.json()
        
    def new_stack(self, endpoint, options):
        pass
    def inspect_stack(self, endpoint, stack):
        pass
    def update_stack(self, endpoint, stack, options):
        pass
    def delete_stack(self, endpoint, stack):
        pass
    def get_stack(self, endpoint, stack):
        pass
    
    