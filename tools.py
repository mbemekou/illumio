import requests
import warnings
import contextlib
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
from urllib3.exceptions import InsecureRequestWarning
import time
from datetime import datetime, timedelta
from dateutil import parser, tz
import logging
import sys
class PCE:
    def __init__(self,quel_pce):
        self.base_file="C:/Users/e44955/Desktop/script"
        try:
            json_file=open(f"{self.base_file}/config/config.json")
        except:
            print(f"No config file found, check [{self.base_file}/config/config.json]")
            exit(1)
        data=json.load(json_file)
        mtnt=datetime.now()
        logging.basicConfig(filename=f"{self.base_file}/logs/tools.log",level=logging.INFO,format='%(levelname)s - %(message)s')
        self.now=mtnt.strftime("%d-%m-%Y_%H-%M")
        self.auj=mtnt.strftime("%d-%m-%Y")
        self.orgs=data["orgs"]
        self.user=data["api_user"]
        self.key=data["api_key"]
        if(quel_pce=="pce1"):
            self.pce=data["pce"]
        elif(quel_pce=="pce2"):
            
           self.pce=data["pce2"] 
        elif(quel_pce=="pce3"):
            self.pce==data["pce_internet"] 
        elif(quel_pce=="qual"):
            self.pce==data["pce_qual"]
            self.orgs=data["orgs_qual"]
            self.user=data["api_qual_user"]
            self.key=data["api_qual_key"]
        else:
            print("quel pce?\n - pce1?\n - pce2? - pce3?\n - pce_qual?\n")
            sys.exit(1)
    def issue_datetime(self):
        tmp_date=datetime.strptime(str(datetime.now().date()), "%Y-%m-%d").strftime('%d-%m-%Y')
        return str(tmp_date+' '+str(datetime.now().time())).split('.')[0]
    def get(self,endpoint, payload):
        headers={'Accept':'application/json'}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] GET url {url} and payload {payload}")
        res=requests.get(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',params=payload)
        status_code=res.status_code
        logging.info(f"{self.issue_datetime()}:[PCE] GET status {status_code}")
        req=res.text
        try:
            json_data=json.loads(req)
            logging.info(f"{self.issue_datetime()}:[PCE] JSON convertion OK")
            return(json_data)
        except:
            logging.error(f"{self.issue_datetime()}:[PCE] JSON convertion KO")
            return(False)
    def post(self,endpoint, payload):
        headers={'Accept':'application/json','Content-Type':'application/json'}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] POST url {url} and payload {payload}")
        res=requests.post(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',data=payload)
        status_code=res.status_code
        logging.info(f"{self.issue_datetime()}:[PCE] POST status {status_code}")
        req=res.text
        try:
            json_data=json.loads(req)
            logging.info(f"{self.issue_datetime()}:[PCE] JSON convertion OK")
            return(json_data)
        except:
            logging.error(f"{self.issue_datetime()}:[PCE] JSON convertion KO")
            return(False)
    
    def put(self,endpoint, payload):
        headers={'Accept':'application/json','Content-Type':'application/json'}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] PUT url {url} and payload {payload}")
        res=requests.put(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',data=payload)
        status_code=res.status_code
        logging.info(f"{self.issue_datetime()}:[PCE] PUT status {status_code}")
        req=res.text
        try:
            json_data=json.loads(req)
            logging.info(f"{self.issue_datetime()}:[PCE] JSON convertion OK")
            return(json_data)
        except:
            logging.error(f"{self.issue_datetime()}:[PCE] JSON convertion KO")
            return(False)
    def delete(self,endpoint, payload):
        headers={'Accept':'application/json'}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] DELETE url {url} and payload {payload}")
        res=requests.delete(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',data=payload)
        status_code=res.status_code
        logging.info(f"{self.issue_datetime()}:[PCE] DELETE status {status_code}")
        req=res.text
        try:
            json_data=json.loads(req)
            logging.info(f"{self.issue_datetime()}:[PCE] JSON convertion OK")
            return(json_data)
        except:
            logging.error(f"{self.issue_datetime()}:[PCE] JSON convertion KO")
            return(False)
    def get_async(self,endpoint,payload):
        headers={'Content-Type':'application/json',"prefer":"respond-async"}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] GET ASYNC url {url} and payload {payload}")
        try:
            req=requests.get(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',params=payload)
            status_code=res.status_code
            logging.info(f"{self.issue_datetime()}:[PCE] GET ASYNC status {status_code}")
            assync_request=req.headers.get("Location")
            url_assync_req=self.pce+assync_request
            while(42):
                req2=requests.get(url_assync_req,headers={'Content-Type':'application/json'},auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt')
                json_response_content=json.loads(req2.content)
                status=json_response_content["status"]
                print(status)
                logging.info(f"{self.issue_datetime()}:[PCE] {status}")
                if status=="done":
                    break
                time.sleep(5)
            
            url_data=self.pce+json_response_content["result"]["pce"]
            req3=requests.requests.get(url_data,headers={'Content-Type':'application/json'},auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt')
            json_data=json.loads(req3.content)
            logging.info(f"{self.issue_datetime()}:[PCE] JSON convertion OK")
            return(json_data)
        except:
            logging.error(f"{self.issue_datetime()}:[PCE] GET ASYNC ERROR")
            return False
                
    def convert_time(self,time):
        return time.strftime("%d-%m-%Y_%H-%M")
    
    def date_parse(self,date):
        FRA=tz.gettz('Europe/Paris')
        if(date==None):
            parisdate=""
        else:
            yourdate=parser.parse(date)
            try:
                parisdate=str(yourdate.astimezone(tz=FRA)).split(".")[0]
            except:
                parisdate="error"
            return(parisdate)
        
            
    def get_download(self, endpoint,payload,filename):
        
        headers={'Accept':'application/json'}
        url=f"{self.pce}{self.orgs}{endpoint}"
        logging.info(f"{self.issue_datetime()}:[PCE] DOWNLOADING url {url} and payload {payload} filename {filename}")
        res=requests.get(url,headers=headers,auth=(self.user,self.key),verify=f'{self.base_file}/ca.crt',params=payload)
        status_code=res.status_code
        logging.info(f"{self.issue_datetime()}:[PCE] GET status {status_code}")
        print(f"status {status_code}")
        with open(f'{self.base_file}/sr/{filename}_{self.now}.tgz','wb') as f:
            for chunk in req.iter_content(chunk_size=1024):
                f.write(chunk)
        print("File downloaded successfully ...")
        logging.info("f{self.issue_datetime()}:[PCE] File downloaded successfully ...")