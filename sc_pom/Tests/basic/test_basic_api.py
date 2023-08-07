import time,copy,sys
import pytest
from Utils import  utils
import requests
from Utils.rpatch import rpatch

class Vars:
    lico = None






'''
>> api
>> pytest -vs /Users/yuhuili/test/api/Tests/basic/test_basic_api.py --durations=25 -v --junitxml=/tmp/pytest_results/test_resultsB.xml --env=chrome
'''


#pytest -vs /Users/yuhuili/test/api/Tests/basic/test_basic_api.py --durations=25 -v --junitxml=/tmp/pytest_results/test_resultsB.xml --env qa --ff




  
'''
test3
MD5 5e812c8bbe35f535743083b1657aefb8
SHA-1   084d6e569037a55cec08277ad6ddebb54559ff90
SHA-256 40940c8c430e960a86a9cea1410780b17a8ba346ed567632b42af8f59c0fb5a3
'''
def __test_vit_call(apic):
        #h1 = 'DC17DC8D6C575A7237F55F486C1AB268'  
        #h1 = 'C75BAB523987F4E99E566A8CE01E94EA'
        h1 = '5E812C8BBE35F535743083B1657AEFB8'
        r = apic.vti_get_query(h1)
        r.pprint()





def test_clear_manifest_then_populate_it(apic):
        # clear out the global manifest object
        r = apic.clear_manifest_ids()
        r.good()
        #
        #
        # create the object/data for test_suite_x add that id to global manifest object
        #
        pdict = {
           "name": "test_suite_x",
           "data": {
              "uuid":utils.generate_uuid_string(),
           }
        }
        r = apic.rest_api_post_add_object(pdict)
        r = apic.add_manifest_id(r.getVal('id'))

        #
        #
        # create the object/data for test_suite_y add that id to global manifest object
        #
        pdict = {
           "name": "test_suite_y",
           "data": {
              "uuid":utils.generate_uuid_string(),
           }
        }
        r = apic.rest_api_post_add_object(pdict)
        r = apic.add_manifest_id(r.getVal('id'))
        utils.bkpoint()



'''
we pretend this data has come from another upstream test suite
'''
def test_x_ipc_data(apic): 
   r = apic.rest_api_get_object(apic.req_id)
   id_list = r.getVal('data.ids')
   for id in id_list:
        r = apic.rest_api_get_object(id)
        if r.getVal('name') == 'test_suite_x':
                print ('the data we want is %s' % r.getVal("data.uuid") )



def test_y_ipc_data(apic): 
   r = apic.rest_api_get_object(apic.req_id)
   id_list = r.getVal('data.ids')
   for id in id_list:
        r = apic.rest_api_get_object(id)
        if r.getVal('name') == 'test_suite_y':
                print ('the data we want is %s' % r.getVal("data.uuid") )






