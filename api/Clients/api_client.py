from Utils import request_utils, utils
import requests
from Utils.rpatch import rpatch 


class apic:

    def __init__(self, env):
        self.env = env
        self.vti_server = "https://www.virustotal.com/"
        self.vti_hdr = {'x-apikey': 'd67ef00ed070ca37e1065d29f5545a8c64700040c1418ca01ed4cf1db53258e8'}
        self.req_server = "https://api.restful-api.dev/objects"
        #self.req_id = 'ff808181884221810188450806e800b3'
        self.req_id = 'ff8081818856250801885656ab0a0000'

        self.db_server = "https://api.dropboxapi.com/2/"
        self.db_hdr = {'Authorization': 'Bearer sl.BfC1ZE36PAdwUaZdvPgKPIaSsdECjfJGjObQ1OgccbTCiihklUXkJiPvGE-ILcmp2OU0bHJUfb_DzReoe0tkJQ9ybXm-1ZjB1vlo_muHHGNOzrSqJP2OP2NSB5zRuO1i28pO7mu-',"Content-Type": "application/json"}
        # Authorization header with the value Bearer <TOKEN>   
        '''    
        url = "https://api.dropboxapi.com/2/files/list_folder"
        headers = {
            "Authorization": "Bearer sl.BfC1ZE36PAdwUaZdvPgKPIaSsdECjfJGjObQ1OgccbTCiihklUXkJiPvGE-ILcmp2OU0bHJUfb_DzReoe0tkJQ9ybXm-1ZjB1vlo_muHHGNOzrSqJP2OP2NSB5zRuO1i28pO7mu-",
            "Content-Type": "application/json"
        }

        data = {
            "path": ""
        }

        r = requests.post(url, headers=headers, data=json.dumps(data))


        curl -X POST https://content.dropboxapi.com/2/files/download \
          --header 'Authorization: Bearer sl.BfC1ZE36PAdwUaZdvPgKPIaSsdECjfJGjObQ1OgccbTCiihklUXkJiPvGE-ILcmp2OU0bHJUfb_DzReoe0tkJQ9ybXm-1ZjB1vlo_muHHGNOzrSqJP2OP2NSB5zRuO1i28pO7mu-' \
          --header 'Dropbox-API-Arg: {"path":"/rick_resume_4th.pdf"}' 
        
        '''



        # prev object rest_api
        # 'id': 'ff808181884221810188450806e800b3'
        # google drive == AIzaSyCFtSxxSJDtMlvXJ2wUBXfLwVqzDqEW0cI
        # dropbox token == sl.BfC1ZE36PAdwUaZdvPgKPIaSsdECjfJGjObQ1OgccbTCiihklUXkJiPvGE-ILcmp2OU0bHJUfb_DzReoe0tkJQ9ybXm-1ZjB1vlo_muHHGNOzrSqJP2OP2NSB5zRuO1i28pO7mu-

    @staticmethod
    def good(r):
        assert (r.status_code in range(200, 204))







    def vti_get_query(self,hsh):
        _url = self.vti_server + "api/v3/search?query=%s" % hsh
        r = requests.get(_url, headers=self.vti_hdr)
        jrc = None
        try:
          jrc = r.json()
        except:
            pass
        rpatch(r)   
        return  r



    #
    # https://restful-api.dev/
    #    
    def rest_api_post_add_object(self,pdict):   
        r = requests.post(self.req_server,json=pdict )
        jrc = None
        try:
          jrc = r.json()
        except:
            pass
        rpatch(r)   
        return  r


    def rest_api_patch_object(self,id,pdict):   
        r = requests.patch(self.req_server + f"/{id}",json=pdict )
        jrc = None
        try:
          jrc = r.json()
        except:
            pass
        rpatch(r)   
        return  r



    def rest_api_get_object(self,id):   
        r = requests.get(self.req_server + f"/{id}")
        jrc = None
        try:
          jrc = r.json()
        except:
            pass
        rpatch(r)   
        return  r

    def rest_api_get_objects(self):   
        r = requests.get(self.req_server)
        jrc = None
        try:
          jrc = r.json()
        except:
            pass
        rpatch(r)   
        return  r


    ###

    def clear_manifest_ids(self):
        pdict = {
        "data": {
        "ids": [],
        } }
        r = self.rest_api_patch_object(self.req_id,pdict)
        return r


    def add_manifest_id(self,add_id):
        r1 = self.rest_api_get_object(self.req_id)
        rpatch(r1)
        id_list = r1.getVal('data.ids')
        id_list.append(add_id)
        pdict = {
        "data": {
        "ids": id_list,
        } }
        
        r2 = self.rest_api_patch_object(self.req_id,pdict)
        return r2



'''
import requests
import json

headers = {"content-type": "application/json"}
payload = json.dumps({ "name": "Joe Mama", "data": { "color": "white", "generation": "3rd", "relationship": "mama of joe"}})
requestUrl = "https://api.restful-api.dev/objects"
r = requests.post(requestUrl, data=payload, headers=headers)
print(r.content)



"ff80818188289aac01882bb3008000c8"

url = 'https://api.restful-api.dev/objects?id=ff80818188289aac01882bb3008000c8'
r = requests.get(url)
'''
