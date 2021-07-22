import requests
import json
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.web import JsonLexer
from urllib3.exceptions import InsecureRequestWarning
class Ilo:
    def __init__(self,pce_fqdn,port,api_version,api_username,api_secret,org_href):
        self.pce_fqdn=pce_fqdn
        self.port=port
        self.api_version=api_version
        self.auth=(api_username,api_secret)
        self.org_href=org_href

    def get_labels(self):

        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/labels"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_services(self):

        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/services"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
       # colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json

    def get_api_key(self,user_id,api_key_id):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/users/{user_id}/api_keys/{api_key_id}"
        headers={"Accept":"application/json"}
        res=requests.get(url,headers=headers,auth=self.auth,verify=False).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
       # colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_authentication_settings(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/authentication_settings"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
       # colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_api_key_collections(self,user_href):
        headers={"Accept":"application/json"}
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/users/{user_href}/api_keys"
        res=requests.get(url,headers=headers,verify=False,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_workloads(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/workloads"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
       # colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_rulesets(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json
    def get_ruleset_by_id(self,ruleset_id):

        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/{ruleset_id}"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json
    
    def get_active_rulesets(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/active/rule_sets"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json

    def get_draft_rulesets(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/rule_sets"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_pairing_profiles(self):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/pairing_profiles"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def get_draft_rules(self, ruleset_id):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/rule_sets/{ruleset_id}/sec_rules"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json



    
    def get_active_ruleset_by_id(self,ruleset_id):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/active/rule_sets/{ruleset_id}"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return raw_json


    def add_ruleset(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/rule_sets"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful



    def add_rules(self,data,ruleset_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/rule_sets/{ruleset_href}/sec_rules"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful



    def create_label(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/labels"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    def create_service(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/services"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def create_unmanaged_workload(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/workloads"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def create_pairing_profile(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/pairing_profiles"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def create_pairing_key(self,pairing_profile_href,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/pairing_profiles/{pairing_profile_href}/pairing_key"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def update_label(self,data,label_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/labels/{label_href}"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful


    def update_ruleset(self,data, rule_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/sec_policy/draft/rule_sets/{rule_href}"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data)
        print(res.text)
        #parsed=json.loads(res)
        #raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        #colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        #return colorful
        return(res)


    def update_workload(self,data,workload_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/workloads/{workload_href}"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    
    def update_agent(self,data,agent_id):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/agents/{agent_id}"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    
    def  update_pairing_profile(self,data,pairing_profile_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/pairing_profiles/{pairing_profile_href}"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def delete_label(self,label_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/labels/{label_href}"
        headers={"Accept":"application/json"}
        res=requests.delete(url,verify=False,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    
    def delete_pairing_profile(self,pairing_profile_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/pairing_profiles/{pairing_profile_href}"
        headers={"Accept":"application/json"}
        res=requests.delete(url,verify=False,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    
    
    def delete_workload(self,workload_href):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/workloads/{workload_href}"
        headers={"Accept":"application/json"}
        res=requests.delete(url,verify=False,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful
    

    def unpair_workload(self,data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/workloads/unpair"
        headers={"Content-Type":"application/json"}
        res=requests.put(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    def get_agent_by_id(self, agent_id):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/agents/{agent_id}"
        headers={"Accept":"application/json"}
        res=requests.get(url,verify=False,headers=headers,auth=self.auth).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful

    

    def enable_vulnerability_license(self,license_id, data):
        url=f"https://{self.pce_fqdn}:{self.port}/api/v{self.api_version}/orgs/{self.org_href}/licenses/{license_id}/pairing_key"
        headers={"Content-Type":"application/json"}
        res=requests.post(url,verify=False,headers=headers,auth=self.auth,data=data).text
        parsed=json.loads(res)
        raw_json=json.dumps(parsed, indent=4, sort_keys=True)
        colorful = highlight(raw_json,lexer=JsonLexer(),formatter=Terminal256Formatter(),)
        return colorful



    def return_label_href(self,label):
        lab=label.split('|')
        L=[]
        l=json.loads(self.get_labels())
        for item in l:
            if(item["value"] in lab):
                L.append(item["href"])
        return L

    def return_ruleset_href(self, rulename):
        l=self.get_active_rulesets()
        for item in l:
            if(item["name"]==rulename):
                return item["href"]
        l=self.get_draft_rulesets()
        for item in l:
            if(item["name"]==rulename):
                return item["href"]
    def return_service_href(self, list_service):
        servicelist=[]
        s_val=list_service.split(',')
        for i in s_val:
            servicelist.append(i.strip())
        s=json.loads(self.get_services())
        services=[]
        for item in s:
            if(item["name"] in servicelist):
                services.append(item["href"])

        return services
    
   
