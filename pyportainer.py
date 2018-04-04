import json

import requests

class PyPortainer():
    def __init__(self, portainer_endpoint):
        self.portainer_endpoint = portainer_endpoint+"/api"
    
    def login(self, username, password):
        r = requests.post(
            self.portainer_endpoint+"/auth", 
            data=json.dumps({"Username":username, "Password":password}), 
            verify=False)
        j = r.json()
        self.token = j.get("jwt")
    
    
    
    def get_dockerhub_info(self):
        r = requests.get(
            self.portainer_endpoint+"/dockerhub", 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def put_dockerhub_info(self, options):
        r = requests.put(
            self.portainer_endpoint+"/dockerhub", 
            data=json.dumps(options), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
        
    
    def get_endpoints(self):
        r = requests.get(
            self.portainer_endpoint+"/endpoints", 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def new_endpoints(self, options):
        r = requests.post(
            self.portainer_endpoint+"/endpoints", 
            data=json.dumps(options), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def get_endpoint(self, identifier):
        r = requests.get(
            self.portainer_endpoint+"/endpoints/{}".format(identifier), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def update_endpoint(self, identifier, options):
        r = requests.put(
            self.portainer_endpoint+"/endpoints/{}".format(identifier), 
            data=json.dumps(options), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def delete_endpoint(self, identifier):
        r = requests.delete(
            self.portainer_endpoint+"/endpoints/{}".format(identifier), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def access_endpoint(self, identifier, options):
        r = requests.put(
            self.portainer_endpoint+"/endpoints/{}/access".format(identifier), 
            data=json.dumps(options), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    
    def get_stacks(self, endpoint):
        r = requests.get(
            self.portainer_endpoint + "/endpoints/{}/stacks".format(endpoint), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def new_stack(self, endpoint, options):
        r = requests.post(
            self.portainer_endpoint + "/endpoints/{}/stacks".format(endpoint), 
            data=json.dumps(options),
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def get_stack(self, endpoint, stack):
        r = requests.get(
            self.portainer_endpoint + "/endpoints/{}/stacks/{}".format(endpoint, stack), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def update_stack(self, endpoint, stack, options):
        r = requests.put(
            self.portainer_endpoint + "/endpoints/{}/stacks/{}".format(endpoint, stack), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def delete_stack(self, endpoint, stack):
        r = requests.delete(
            self.portainer_endpoint + "/endpoints/{}/stacks/{}".format(endpoint, stack), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    def get_stackfile(self, endpoint, stack):
        r = requests.get(
            self.portainer_endpoint + "/endpoints/{}/stacks/{}/stackfile".format(endpoint, stack), 
            headers={"Authorization": "Bearer {}".format(self.token)}, 
            verify=False)
        return r.json()
        
    
    