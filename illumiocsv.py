from illumio import Ilo
import csv, json
from urllib3.exceptions import InsecureRequestWarning


class IloCsv(Ilo):
    def label_to_json(self,lab):
        l=[]
        for i in lab:
            l.append({"label":{"href":i}})
        return json.dumps(l, indent=4,sort_keys=True)
    def service_to_json(self,serv):
        
        return json.dumps(serv)
    
    def add_csv_label(self, csvfile):
        l=['app','loc','env','role']
        with open(csvfile,encoding="utf-8-sig") as f:
            cfile=csv.DictReader(f, delimiter=";")
            for i in cfile:
                data={}
                if(i['type'] in l):
                    data['key']=i['type']
                    data['value']=i['name']
                    print(self.create_label(json.dumps(data, indent=4,sort_keys=True)))

    def comparer(self, list1, list2):
        diff=[i for i in list1+list2 if i not in list1 or i not in list2]
        result=len(diff)==0
        return result

    def pairing_profil_to_csv(self,profil):
        label="SCOPE; RULESET\n"
        for i in profil:
            if('PPL-' in i['name']):
                label=label+i['name'].split('PPL-')[1]+'; RS-'+i['name'].split('PPL-')[1]+"\n"
        with open("ppl_csv.csv", "w") as f:
            f.write(label)
            f.close()
        return label
            




    def add_csv_services(self, csvfile):
        proto={"tcp":6,"udp":17,"icmp":1}
        
        with open(csvfile,encoding="utf-8-sig") as f:
            cfile=csv.DictReader(f, delimiter=";")
            for i in cfile:
                service_ports=[]
                serv="""       
                {
                    "name": "$name$",
                    "description": "$description$",
                    "service_ports":$service_ports$
                }
                """
                sports=i['service_ports'].split(',')
                ports=[]
                for sport in sports:
                    ports.append(sport.strip())
                print(ports)
                for port in ports:
                    p={}
                    if("tcp" in port):
                        p["port"]=int(port.split(" ")[0])
                        p["proto"]=6
                    if("udp" in port):
                        p["port"]=int(port.split(" ")[0])
                        p["proto"]=17
                    if("icmp" in port):
                        p["port"]=int(port.split(" ")[0])
                        p["proto"]=1
                    service_ports.append(p)
                name=i['name']
                description=i['description']
                print(self.create_service(serv.replace("$name$",name).replace("$description$",description).replace("$service_ports$",self.service_to_json(service_ports))))





    def add_csv_intra_ruleset(self, csvfile):
        r=[]
        with open(csvfile, encoding="utf-8-sig") as f:
            cfile=csv.DictReader(f, delimiter=';')
            for i in  cfile:
                name=i['NAME']
                update="false"
                extrascope="false"
                sec_connect="false"
                scope=self.label_to_json(self.return_label_href(i['SCOPE']))
                consumer=self.label_to_json(self.return_label_href(i['CONSUMER']))
                provider=self.label_to_json(self.return_label_href(i['PROVIDER']))
                service=self.service_to_json(self.return_service_href(i['SERVICE']))
                if(i['EXTRASCOPE']=='yes' or i['EXTRASCOPE']=='true'):
                    extrascope="true"
            
                if(i['SECURE']=='yes' or i['SECURE']=='true'):
                    sec_connect="true"

                if(i['UPDATE']=='yes' or i['UPDATE']=='true'):
                    update="true"
                rulset="""
            {
                "enabled": true,
                "name": "$NAME$",

                "scopes":
                    [
                        $SCOPE$
                    ],

                "rules":
                    [
                        {
                            "enabled":      true,
                            "providers":
                                            $PROVIDER$,
                            "consumers":
                                            $CONSUMER$,
                            "ingress_services":

                                            $SERVICE$,
                            "resolve_labels_as":

                                            {
                                                "providers": ["workloads"],
                                                "consumers": ["workloads"]
                                            },
                            "unscoped_consumers": $EXTRASCOPE$,
                            "sec_connect": $SECURE$

                        }
                    ]
  }
                """


                ruleset=rulset.replace("$SCOPE$",scope).replace("$PROVIDER$",provider).replace("$CONSUMER$",consumer).replace("$NAME$",name).replace("$SERVICE$",service).replace("$EXTRASCOPE$",extrascope).replace("$SECURE$",sec_connect)
                if(update=="false"):
                    print(self.add_ruleset(ruleset))

                if(update=="true"):
                    ref=None
                    r=json.loads(self.get_draft_rulesets())
                    
                    ruls="""

                        {
                            "enabled":      true,
                            "providers":
                                            $PROVIDER$,
                            "consumers":
                                            $CONSUMER$,
                            "ingress_services":

                                            $SERVICE$,
                            "resolve_labels_as":

                                            {
                                                "providers": ["workloads"],
                                                "consumers": ["workloads"]
                                            },
                            "unscoped_consumers": $EXTRASCOPE$,
                            "sec_connect": $SECURE$

                        }
                    """
                    for el in r:

                        if(el['name']==i['NAME']):
                            ref=el['href'].split('/')[-1]

                            break

                    if(ref!=None):
                       
                       rules=ruls.replace("$PROVIDER$",provider).replace("$CONSUMER$",consumer).replace("$SERVICE$",service).replace("$EXTRASCOPE$",extrascope).replace("$SECURE$",sec_connect)
                       jrules=json.loads(rules)
                       roul=json.loads(self.get_draft_rules(ref))
                       for ro in roul:
                           if(self.comparer(ro['consumers'],jrules['consumers']) and self.comparer(ro['providers'],jrules['providers']) and self.comparer(ro['ingress_services'],jrules['ingress_services'])):
                               print(f"rule:\n {rules}\n already exists in this ruleset")
                               break
                       


                           
                       print(self.add_rules(rules,ref))
                    else:
                        print(f'can not update {i["NAME"]}. rule does not exist') 




