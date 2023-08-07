# Generated by Selenium IDE
import pytest
import time
import json
import requests
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils import  request_utils, utils
from Utils.rpatch import rpatch 
import sys


'''
>> api
>> pytest -vs /Users/yuhuili/test/api/Tests/web/test_spyc_email_exposure.py --durations=25 -v --junitxml=/tmp/pytest_results/test_resultsB57.xml --env qa --ff
>> pytest -vs /Users/yuhuili/test/api/Tests/web/test_spyc_email_exposure.py -v --env qa --ff

ac = ActionChains(self.driver)
menu = self.driver.find_element(By.XPATH,"//a[contains(text(), 'WHAT WE OFFER')]")
ac.move_to_element(menu).perform()
#self.driver.find_element(By.XPATH,"//span[contains(@class,'elementor-icon-list-text') and contains(text(),'Enterprise Protection')]").click()
self.driver.find_element(By.XPATH,"//span[contains(@class,'elementor-icon-list-text') and contains(text(),'Fraud Prevention')]").click()




#self.driver.find_element(By.XPATH,"//span[contains(text(), 'Enterprise Protection')]").click()
#self.driver.find_element(By.XPATH,"//span[contains @class='elementor-icon-list-text' and contains text()='Enterprise Protection']").click()
#self.driver. find_element(By.XPATH,"//span[@class='elementor-icon-list-text'] and contains(text(), 'Enterprise Protection')]").click()
#self.driver.find_element(By.LINK_TEXT,"Enterprise Protection").click())



driver.find_element(By.XPATH, "//h1[contains(@class, 'mb-33')]")



driver.find_element_by_xpath("//div[@class='fc-day-content' and text()='15']")

driver.findElement(By.xpath("//div/input[(@formcontrolname='nic_no') and contains(@class,'ng-invalid')]");

driver.findElement(By.xpath("//div/input[(@formcontrolname='nic_no') and contains(@class,'ng-invalid')]");

contains_class_match = driver.find_element(By.XPATH, "//h1[contains(@class, 'mb-33')]")
  <span class="elementor-icon-list-text">Enterprise Protection <br><small>Stop cybercriminals from comprising your business</small></span>

<span class="elementor-icon-list-text">Enterprise Protection <br><small>Stop cybercriminals from comprising your business</small></span>


pytest -vs /Users/yuhuili/test/api/Tests/web/test_spyc_email_exposure.py --durations=25 -v --junitxml=/tmp/pytest_results/test_resultsB57.xml --env qa --ff
'''

class Test_spycloud_email_exposure():

  def spyc_personal_email_exposure(self,email):
    hdr = {"Content-Type": "application/json"}
    pdict = {
    "operationName": "FreemailReport",
    "variables": {
      "email": email,
      "executionType": "CYE-FE: https://spycloud.com"
    },
    "query": "query FreemailReport($email: String!, $executionType: String!) {\n  freemailReport(email: $email, executionType: $executionType) {\n    personalIdentityExposureRisk {\n      isPresent\n      count\n      message\n      otherMessages\n      errorMessage\n      __typename\n    }\n    personalBreachExposures {\n      isPresent\n      count\n      message\n      otherMessages\n      errorMessage\n      __typename\n    }\n    personalMostRecentExposure {\n      isPresent\n      count\n      message\n      otherMessages\n      errorMessage\n      __typename\n    }\n    __typename\n  }\n}"
    }
    r = requests.post("https://cye-api.spycloud.com/graphql",json=pdict,headers=hdr )
    rpatch(r)
    return r


  def spyc_email_hybrid(self,email,domain=False):
    if domain == False:
      self.driver.get("https://spycloud.com")
      report_start = 'Your Personal Risk'
      report_end   = 'Exposures'
    else:  
      self.driver.get("https://spycloud.com/check-your-exposure/")
      report_start = 'Your Company Risk'
      report_end   = 'Credentials'
    time.sleep(5)
    
    #


    #  
    self.driver.set_window_size(1200, 1000)
    self.driver.find_element(By.ID,"cye-prax-input").send_keys(email)
    self.driver.find_element(By.ID,"cye-prax-button").click()
    time.sleep(5)
    # poll 
    thinking = 'Checking your email against billions of recaptured darknet data assets'
    for inx in range(20):
      z = ''
      try:
        z = self.driver.find_element(By.XPATH, "/html/body").text
      except:
        pass

      if thinking in z:
        print("thinking ..")
        time.sleep(5)
      else:
        print('bam ... ')  
        break

    z = self.driver.find_element(By.XPATH, "/html/body").text
    pprint(z)
    if 'your real-time darknet exposure details' in z:
      zlist = z.split('\n')
      zst = zlist.index(report_start)
      zend = zlist.index(report_end)
      data = zlist[zst:zend]
      print("+++ >>>>>>>>",zlist[zst:zend])
    else:
      print("--- something is wrong")  


    
    #
    # verify displayed data is indeed consistent with the api call == spyc_personal_email_exposure 
    #   
    if domain == False:
      r = self.spyc_personal_email_exposure(email)
      assert r.getVal('data.freemailReport.personalIdentityExposureRisk.otherMessages') in data
      assert str(r.getVal('data.freemailReport.personalBreachExposures.count')) in data
      assert r.getVal('data.freemailReport.personalMostRecentExposure.otherMessages') in data
    else:
      r = data  
    #  
    return r 



  def test_rick_weth_yahoo(self,init_driver):
    email = "rick_weth@yahoo.com"
    r = self.spyc_email_hybrid(email)
    # now verify via some know values (we may have an issue with the api)
    assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.count') == 42)
    assert(r.getVal('data.freemailReport.personalBreachExposures.count') == 11)
    assert(r.getVal('data.freemailReport.personalMostRecentExposure.otherMessages') == '4 years ago')
    assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.otherMessages') == 'LOW')



  def test_raweth_gmail(self,init_driver):
    email = "raweth@gmail.com"
    r = self.spyc_email_hybrid(email)
    # now verify via some know values (we may have an issue with the api)
    assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.count') == 10)
    assert(r.getVal('data.freemailReport.personalBreachExposures.count') == 3)
    assert(r.getVal('data.freemailReport.personalMostRecentExposure.otherMessages') == '5 years ago')
    assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.otherMessages') == 'LOW')



  def test_domain_email(self,init_driver):
    email = "rweth@filoli.com"
    data = self.spyc_email_hybrid(email,domain=True)
    cook = ''
    r = self.spyc_domain_email_exposure(email,cook)

 



  # NOT WORKING
  def spyc_domain_email_exposure(self,email,cookie):
    hdr = {"Content-Type": "application/json","Authority":"cye-api.spycloud.com","Cookie":cookie}
    pdict = {
      "operationName": "BasicReport",
      "variables": {
        "email": email,
        "executionType": "CYE-FE: https://spycloud.com"
      },
      "query": "query BasicReport($email: String!, $executionType: String!) {\n  basicReport(email: $email, executionType: $executionType) {\n    domainCompanyExposureRisk {\n      isPresent\n      count\n      otherMessages\n      message\n      errorMessage\n      __typename\n    }\n    domainMostRecentExposure {\n      isPresent\n      otherMessages\n      message\n      errorMessage\n      count\n      __typename\n    }\n    domainCompanyBreachExposures {\n      isPresent\n      count\n      message\n      errorMessage\n      otherMessages\n      __typename\n    }\n    domainExactPasswordReuse {\n      isPresent\n      count\n      message\n      errorMessage\n      otherMessages\n      __typename\n    }\n    domainExecutiveCredentialExposures {\n      isPresent\n      count\n      message\n      errorMessage\n      __typename\n    }\n    domainNumberBreachAppearances {\n      isPresent\n      count\n      message\n      errorMessage\n      __typename\n    }\n    companyStolenCookies {\n      isPresent\n      count\n      message\n      errorMessage\n      __typename\n    }\n    domainMalwareExposuresInfectedEmployees {\n      isPresent\n      message\n      errorMessage\n      __typename\n    }\n    personalIdentityExposureRisk {\n      isPresent\n      count\n      otherMessages\n      message\n      errorMessage\n      __typename\n    }\n    personalNumberBreachAppearances {\n      isPresent\n      count\n      message\n      errorMessage\n      __typename\n    }\n    personalBreachExposures {\n      isPresent\n      count\n      message\n      errorMessage\n      __typename\n    }\n    personalMostRecentExposure {\n      isPresent\n      otherMessages\n      message\n      errorMessage\n      __typename\n    }\n    personalIDLinkCorrelation {\n      isPresent\n      message\n      errorMessage\n      __typename\n    }\n    customerMalwareInfectedConsumerRecords {\n      isPresent\n      message\n      errorMessage\n      __typename\n    }\n    __typename\n  }\n}"
    }
    r = requests.post("https://cye-api.spycloud.com/graphql",json=pdict,headers=hdr )
    rpatch(r)
    return r



  # This is a great way to blow an hour up!
  '''
  cookies = self.driver.get_cookies() 
  for acookie in cookies:
    print("%s=%s;" % (acookie['name'],acookie['value']))
  utils.bkpoint()

  r = self.spyc_domain_email_exposure('rweth@malwarebytes.com',self.driver.get_cookies())
  # actual cookie from chrome
  >>> pprint(xx)
  ('_gcl_au=1.1.1866141944.1685558660; '
   '_rdt_uuid=1685558659867.78cf3832-4dcb-4d84-8fa7-1533a1a9b344; '
   '__utmc=183290084; _fbp=fb.1.1685558660086.1077831891; '
   'hubspotutk=95f4ec601ef76af308139cde73fe8b3f; __hssrc=1; '
   '_gid=GA1.2.828293049.1685558661; '
   '__utma=183290084.592352732.1685558660.1685558660.1685562576.2; '
   '__utmz=183290084.1685562576.2.2.utmcsr=cye.spycloud.com|utmccn=(referral)|utmcmd=referral|utmcct=/; '
   '__hstc=188594551.95f4ec601ef76af308139cde73fe8b3f.1685558660839.1685558660839.1685562576808.2; '
   '_ga_GJSB7W2DK5=GS1.1.1685558659.1.1.1685562616.19.0.0; '
   '_ga=GA1.2.592352732.1685558660; '


   # whats missisng from python get cookie
   # gives an error response in content 
   >> '__utmt_sfga=1; '
   >> '_gat_UA-84143732-1=1; '
   >> '__Host-device=s%3A12b550c3-af58-4e43-a985-88d1bc163638.WtCYZlmUwdFabmIhHz1XFrckPYyYnhlE81uHR5qDy%2BA; '
   >> '__utmb=183290084.2.10.1685562576; '
   >> '__hssc=188594551.2.1685562576808; )



  Cookie2:
  xx = "_gcl_au=1.1.1483787046.1685585965; 
  _rdt_uuid=1685585965506.0a60a105-8ed7-4603-91ca-7c4d51748679; 
  __utma=183290084.398791065.1685585965.1685585966.1685585966.1; 
  __utmc=183290084; _
  _utmz=183290084.1685585966.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); 
  __utmt_sfga=1; 
  _gid=GA1.2.594348218.1685585966; 
  __hstc=188594551.c98d41fce6849d0f1aaa1fbc19ad9dd8.1685585965602.1685585965602.1685585965602.1; 
  hubspotutk=c98d41fce6849d0f1aaa1fbc19ad9dd8; 
  __hssrc=1; _fbp=fb.1.1685585965669.56929893; 
  __Host-device=s%3A2c3f0981-9104-48e7-8447-4ec53b8ee7eb.QFoFN%2Fws%2BurLtRANYS358Y7p0L6ZSYClCwUnPr5AwBQ; 
  __hssc=188594551.2.1685585965603;__utmb=183290084.3.10.1685585966;_ga=GA1.1.398791065.1685585965;_ga_GJSB7W2DK5=GS1.1.1685585965.1.1.1685586089.60.0.0"


    >>> r
    <Response [200]>
    >>> rpatch(r)
    >>> r.pprint()
    {'data': None,
     'errors': [{'extensions': {'code': 'FORBIDDEN',
                                'response': {'error': 'Forbidden',
                                             'message': 'Forbidden resource',
                                             'statusCode': 403}},
                 'message': 'Forbidden resource'}]}


'''
