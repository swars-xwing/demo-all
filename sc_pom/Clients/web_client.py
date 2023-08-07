from Utils import request_utils, utils
import requests
from Utils.rpatch import rpatch 
from Utils import  utils


class wc:

    def __init__(self, env,ff_browser):
        self.env = env
        self.ff = ff_browser
        self.vti_server = "https://www.virustotal.com/"
        self.vti_hdr = {'x-apikey': 'd67ef00ed070ca37e1065d29f5545a8c64700040c1418ca01ed4cf1db53258e8'}
        self.req_server = "https://api.restful-api.dev/objects"
        #self.req_id = 'ff808181884221810188450806e800b3'
        self.req_id = 'ff8081818856250801885656ab0a0000'

        self.db_server = "https://api.dropboxapi.com/2/"
        self.db_hdr = {'Authorization': 'Bearer sl.BfC1ZE36PAdwUaZdvPgKPIaSsdECjfJGjObQ1OgccbTCiihklUXkJiPvGE-ILcmp2OU0bHJUfb_DzReoe0tkJQ9ybXm-1ZjB1vlo_muHHGNOzrSqJP2OP2NSB5zRuO1i28pO7mu-',"Content-Type": "application/json"}
     
    @staticmethod
    def good(r):
        assert (r.status_code in range(200, 204))



