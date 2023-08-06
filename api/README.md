demo api a simple interface to to specific clients 
   1) www.virustotal.com simple get with authorization header 
   2) https://api.restful-api.dev/objects no headers but post patch get with some interesting
      built up aggregate calls

Usage:
   git clone git@github.com:swars-xwing/demo-api.git  # must have ssh key in repository
   cd to local work area root ==  cd  ../test/api
   # run simple actual test
   pytest -vs ../test/api/Tests/basic/test_basic_api.py --env qa


simple we browser:
pytest -vs /Users/yuhuili/test/sc_pom/Tests/web/test_main.py --env prod



results (i.e):
yuhuili@Yuhuis-MacBook-Pro api % pytest -vs /Users/yuhuili/test/api/Tests/basic/test_basic_api.py --env qa
============================================================================= test session starts ==============================================================================
platform darwin -- Python 3.9.6, pytest-7.3.1, pluggy-1.0.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/yuhuili/test/api
collected 4 items                                                                                                                                                              

Tests/basic/test_basic_api.py::test_vit_call {'data': [{'attributes': {'authentihash': '839eb3542f13d82bfdb88f27ccede2959ae97074f1c8880681e95a0d46d6a69e',
                          'creation_date': 1660922324,
                          'crowdsourced_yara_results': [{'author': '@bartblaze',
		                                                         'description': 'Identifies '
		           :
		           :                                              				

           'id': '40940c8c430e960a86a9cea1410780b17a8ba346ed567632b42af8f59c0fb5a3',
           'links': {'self': 'https://www.virustotal.com/api/v3/files/40940c8c430e960a86a9cea1410780b17a8ba346ed567632b42af8f59c0fb5a3'},
           'type': 'file'}],
 'links': {'self': 'https://www.virustotal.com/api/v3/search?query=5E812C8BBE35F535743083B1657AEFB8'}}
PASSED

Tests/basic/test_basic_api.py::test_clear_manifest_then_populate_it 200
PASSED

Tests/basic/test_basic_api.py::test_x_ipc_data the data we want is 590fd093-e6a9-4217-90ed-8edc9abb5d01
PASSED

Tests/basic/test_basic_api.py::test_y_ipc_data the data we want is 11896a03-6d56-423f-9694-ab6ee960228a
PASSED

================ 4 passed in 7.69s ================================================ 