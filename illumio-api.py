#!/usr/bin/python3
from illumio import Ilo
from illumiocsv import IloCsv
import csv, json, argparse, sys,os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_object_type(s):
    l=["labels","services","api_key","authentication_settings","api_keys_collections","workloads","rulesets","ruleset","active_rulesets","draft_rulesets","pairing_profiles"]
    try:
        v=str(s)
    except ValueError:

        raise argparse.ArgumentTypeError(f'expected str, got {s}')
    if(s not in l):
        raise argparse.ArgumentTypeError(f'specify object among:  "labels","services","api_key","authentication_settings","api_keys_collections","workloads","rulesets","ruleset","active_rulesets","draft_rulesets","pairing_profiles" ')
    else:
        return s

def create_object_type(s):
    l=["labels","services","rulesets"]
    try:
        v=str(s)
    except ValueError:

        raise argparse.ArgumentTypeError(f'expected str, got {s}')
    if(s not in l):
        raise argparse.ArgumentTypeError(f'specify object among:  "labels","services","rulesets" ')
    else:
        return s

def update_object_type(s):
    l=["labels","services","rulesets"]
    try:
        v=str(s)
    except ValueError:

        raise argparse.ArgumentTypeError(f'expected str, got {s}')
    if(s not in l):
        raise argparse.ArgumentTypeError(f'specify object among:  "labels","services","rulesets" ')
    else:
        return s

def start():
    try:
        parser=argparse.ArgumentParser(description='illumio api command', prog='illumio-api')

        subparsers=parser.add_subparsers(dest='command', required=True)

        init_parser=subparsers.add_parser('init', help='setup illumio pce api parameters')

        init_parser.add_argument('--fqdn','-f', help='Illumio REST API PCE fqdn',required=True)
        init_parser.add_argument('--port','-p', help='Illumio REST APIs PCE port number(default to 8443)',default=8443, type=int)
        init_parser.add_argument('--version','-v', help='Illumio REST API release versions (default to 2)',default=2, type=int)
        init_parser.add_argument('--org','-o', help='Illumio REST API   organization HREF(default to 1)',default=1, type=int)
        init_parser.add_argument('--username','-u', help='Illumio REST API username', required=True)
        init_parser.add_argument('--secret','-s', help='Illumio REST API key secret', required=True)

        get_parser=subparsers.add_parser('get', help='get policy object')
        get_parser.add_argument('object', help='Illumio  PCE object to get',type=get_object_type)
        get_parser.add_argument('-id', help='Illumio PCE object Id to get ', type=int)
        get_parser.add_argument('-o','--out', help='the CSV file to output object  in csv format', type=str)

        create_parser=subparsers.add_parser('create', help='create policy object from csv file\'s')
        create_parser.add_argument('object', help='Illumio PCE object to create', type=create_object_type)
        create_parser.add_argument('--file','-f', help='csv file name',required=True)
        update_parser=subparsers.add_parser('update', help='create policy object from csv file\'s')
        update_parser.add_argument('object', help='Illumio  PCE object to update', type=update_object_type)
        update_parser.add_argument('--file','-f', help='csv file name',required=True)

        args=parser.parse_args()
    except:
        sys.exit()
  
    if(args.command=="init"):
        a=os.path.expanduser("~")

        if( "\\" in a):

            conn_directory_ilo=a+"\\AppData\\Roaming\\illumio-api"
            if(not os.path.exists(conn_directory_ilo)):
                os.makedirs(conn_directory_ilo)
            conn_file_ilo=conn_directory_ilo+"\\illumio-api.txt"
            with open(conn_file_ilo, "w") as f:
                f.write(json.dumps(vars(args)))
        else:
            conn_directory_ilo=a+"/.illumio-api"
            if(not os.path.exists(conn_directory_ilo)):
                os.makedirs(conn_directory_ilo)
            conn_file_ilo=conn_directory_ilo+"/.illumio-api.txt"
            with open(conn_file_ilo, "w") as f:
                f.write(json.dumps(vars(args)))


        ilo=IloCsv(args.fqdn,args.port,args.version,args.username,args.secret,args.org)

    if(args.command=="get"):

        if(os.name == 'nt'):
            conn_file_ilo=os.path.expanduser("~")+"\\AppData\\Roaming\\illumio-api\\illumio-api.txt"
        else:
            conn_file_ilo=os.path.expanduser("~")+"/.illumio-api/.illumio-api.txt"

        if(os.path.exists(conn_file_ilo)):
            with open(conn_file_ilo,encoding="utf-8-sig") as f:
                dict_var=json.load(f)
                ilo=IloCsv(dict_var["fqdn"],dict_var["port"],dict_var["version"],dict_var["username"],dict_var["secret"],dict_var["org"])
        else:
            print("illumio-api parameters are not set\n Please fill in the api parameters, with the command:\n illumio-api init [options]")
            sys.exit(0)
        if(args.object=="labels" and args.out==None):
            print(ilo.get_labels())
        if(args.object=="labels" and args.out!=None):
            json_lab=json.loads(ilo.get_labels())
            with open(args.out, "w") as f:
                csv_file=csv.writer(f,delimiter=";")
                csv_file.writerow(["type","name"])
                for element in json_lab:
                    csv_file.writerow([element["key"],element["value"]])
            


        if(args.object=="services" and args.out==None):
            print(ilo.get_services())
        if(args.object=="services" and args.out!=None):
            json_serv=json.loads(ilo.get_services())
            with open(args.out,"w") as f:
                csv_file=csv.writer(f,delimiter=";")
                csv_file.writerow(["SERVICE","DESCRIPTION"])
                for element in json_serv:
                    csv_file.writerow([element["name"],element["description"]])
        if(args.object=="api_keys_collections"):
            print(ilo.get_api_key_collections())
        if(args.object=="authentication_settings"):    
            print(ilo.get_authentication_settings())
        if(args.object=="workloads"):
            print(ilo.get_workloads())
        if(args.object=="pairing_profiles" and args.out==None):
            print(ilo.get_pairing_profiles())
        if(args.object=="pairing_profiles" and args.out!=None):

            with open(args.out, "w") as f:
                f.write(ilo.pairing_profil_to_csv(json.loads(ilo.get_pairing_profiles())))
                f.close()
        if(args.object=="active_rulesets"):
            print(ilo.get_active_rulesets()) 
        if(args.object=="draft_rulesets" and args.out==None):
            print(ilo.get_draft_rulesets()) 
        if(args.object=="draft_rulesets" and args.out!=None):
            json_rul=json.loads(ilo.get_draft_rulesets())
            with open(args.out,"w") as f:
                csv_file=csv.writer(f,delimiter=";")
                csv_file.writerow(["RULENAME"])
                for element in json_rul:
                    csv_file.writerow([element["name"]])
        if(args.object=="rulesets"):
            print(ilo.get_rulesets())    
        if((args.object=="api_key") and (args.id!=None)):
            print(ilo.get_api_key(args.id))
        if((args.object=="ruleset") and (args.id!=None)):
            print(ilo.get_ruleset_by_id(args.id))
        if((args.object=="ruleset") and (args.id==None)):
            print("please specify a valid ruleset id")
        sys.exit()    
    if(args.command=="create" and os.path.exists(args.file)):
        if(os.name == 'nt'):
            conn_file_ilo=os.path.expanduser("~")+"\\AppData\\Roaming\\illumio-api\\illumio-api.txt"
        else:
            conn_file_ilo=os.path.expanduser("~")+"/.illumio-api/.illumio-api.txt"

        if(os.path.exists(conn_file_ilo)):
            with open(conn_file_ilo,encoding="utf-8-sig") as f:
                dict_var=json.load(f)
                ilo=IloCsv(dict_var["fqdn"],dict_var["port"],dict_var["version"],dict_var["username"],dict_var["secret"],dict_var["org"])
        else:
            print("illumio-api parameters are not set\n Please fill in the api parameters, with the command:\n illumio-api init [options]")
            sys.exit(0)
        if(args.object=="labels"):
            try:
                ilo.add_csv_label(args.file)
            except:
                print("invalid CSV schema or connection failed")
        if(args.object=="services"):
            try:
                ilo.add_csv_services(args.file)
            except:
                print("invalid CSV schema or connection failed")
        if(args.object=="rulesets"):
            ilo.add_csv_intra_ruleset(args.file)
            
    if(args.command in ["create","get","update"] and not os.path.exists(args.file)):
        print("file doesn't exist or you dont have the permission to access it")
start()

