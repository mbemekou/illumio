# illumio
is a pythonic tool  that allows you to make api calls to illumio PCE with simplicity so that you can automate process.


 Usage: illumio-api <command> <options> 
    
    <command>:
    
    init - this command  setup illumio pce api parameters and then we can use others command without having to specify  parameters
    
    get -  this command allow us to get objects through api to illumio pce and eventually to save in csv file
    
    create - this command allow us to create  list of objects  from  csv file's
    
    update - not implemented yet but with this command we can update object's value from csv file.


    Most used options for 'init' command:

    --fqdn/-f: Illumio REST API PCE fqdn
    --port/-p: Illumio REST APIs PCE port number (default value = 8443)
    --version/-v: Illumio REST API release versions ( default value =2)
    --org/-o: Illumio REST API   organization HREF (default value =1)
    --username/-u: Illumio REST API username
    --secret/-s: Illumio REST API key secret

    EXAMPLES:
    illumio-api init --fqdn pce.tds.local --port 8443 -api 2 ---org 1 --username api_183ab0757df31cf75 --secret 0c8b09a6a35a51d0f12fdf960fd2b531970325c1e
    illumio-api init -f pce.tds.local  -u api_183ab0757df31cf75 -s 0c8b09a6a35a51d0f12fdf960fd2b531970325c1e
  

    
    Most used options for 'get' command:


    --id/-i: Illumio object id to get
    --out/-o: the csv file where the illumio object will be saved


    Most used objects for 'get' command:


    labels
    services
    api_key
    authentication_settings
    api_keys_collections
    workloads
    rulesets
    ruleset
    active_rulesets
    draft_rulesets
    pairing_profiles

    EXAMPLES:
    illumio-api init -f pce.tds.local -u api_183ab0757df31cf75 -s 0c8b09a6a35a51d0f12fdf960fd2b531970325c1e
    illumio-api get labels
    illumio-api get labels -o labels.csv
    illumio-api get services 
    illumio-api get services -o services.csv
    illumio-api get workloads
    illumio-api get rulesets
    illumio-api get ruleset -id 90

    Most used objects for 'create' command:
    labels
    services
    rules
    Most used options for 'create command:
    --file/-f: <csv file name>

    EXAMPLES:

    illumio-api init -f pce.tds.local  -u api_183ab0757df31cf75 -s 0c8b09a6a35a51d0f12fdf960fd2b531970325c1e
    illumio-api create labels -f labels.csv
    
    csv file template for labels creation
   
![image](https://user-images.githubusercontent.com/50032599/126626587-af276e4a-dc07-4cc4-a7a7-4297a716b1aa.png)
  

    illumio-api create services -f services.csv
    
    csv file template for services creation
  ![image](https://user-images.githubusercontent.com/50032599/126625875-baa13001-ffa4-4e15-878d-015428dd6005.png)

    
    
    illumio-api create rulesets -f rules.csv
    csv  file template for rulesets creation
![image](https://user-images.githubusercontent.com/50032599/126628174-d78010be-e0db-473f-a293-713bcb119de6.png)

    
   
