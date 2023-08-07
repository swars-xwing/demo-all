import pytest
from Pages.MainPage import MainPage
from Tests.test_base import BaseTest
from Utils import  request_utils, utils
from selenium.webdriver.common.by import By
import re,time


class Test_Main(BaseTest):

	def _test_wwo_enterprise_protection(self,mainp):
	   	mainp.main_home()
	   	mainp.menu_wwo_select('Enterprise Protection')	
	   	_patt = 'https://.*/solutions/enterprise-protection/'
	   	assert re.match(_patt,self.driver.current_url) != None



	def test_wwo_fraud_prevention(self,mainp):
		mainp.main_home()
		utils.bkpoint()
		mainp.menu_wwo_select('Fraud Prevention')	
		_patt = 'https://.*/use-case/fraud-prevention/'
		time.sleep(3)
		assert re.match(_patt,self.driver.current_url) != None
		pass_img = mainp.get_elem(mainp.pass_img)

		demo = mainp.get_elem(mainp.req_a_demo)
		utils.bkpoint()
		mainp.do_click(mainp.eng_learn_more)
		utils.bkpoint()






	def _test_wwo_cybercrime_investigations(self,mainp):
		mainp.main_home()
		mainp.menu_wwo_select('Cybercrime Investigations')	
		_patt = 'https://.*/products/cybercrime-investigations/'
		assert re.match(_patt,self.driver.current_url) != None




	def _test_pers_yahoo_email(self,mainp):
		r = mainp.spyc_email_hybrid('rick_weth@yahoo.com',domain=False)
		# now verify via some know values (we may have an issue with the api)
		assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.count') == 42)
		assert(r.getVal('data.freemailReport.personalBreachExposures.count') == 11)
		assert(r.getVal('data.freemailReport.personalMostRecentExposure.otherMessages') == '3 years ago')
		assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.otherMessages') == 'LOW')
		utils.bkpoint()




	def _test_pers_gmail_email(self,mainp):
		r = mainp.spyc_email_hybrid('raweth@gmail.com',domain=False)
		# now verify via some know values (we may have an issue with the api)
		assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.count') == 10)
		assert(r.getVal('data.freemailReport.personalBreachExposures.count') == 3)
		assert(r.getVal('data.freemailReport.personalMostRecentExposure.otherMessages') == '5 years ago')
		assert(r.getVal('data.freemailReport.personalIdentityExposureRisk.otherMessages') == 'LOW')
		utils.bkpoint()


	def test_buss_mwb_email(self,mainp):
		data = mainp.spyc_email_hybrid('rweth@malwarebytes.com',domain=True)





	#<img decoding="async" width="339" height="283" src="https://spycloud.com/wp-content/uploads/2023/07/outcome-cc.svg" class="attachment-full size-full wp-image-56571" alt="">
	#z = self.driver.find_element(By.CLASS_NAME,"attachment-full.size-full.wp-image-.")
	#z = self.driver.find_element(By.XPATH,"//img[contains(@class,'attachment-full.size-full.wp-image-') and contains(text(),'%s')]" % text)
	'''
	z = self.driver.find_element(By.CLASS_NAME,"attachment-large.size-large")
	z = self.driver.find_element(By.CLASS_NAME,"attachment-large.size-large.wp-image-56579")
	z = self.driver.find_element(By.XPATH,"//img[contains(@class,'attachment-large.size-large.wp-image-56579')]")
	<img decoding="async" width="358" height="356" src="https://spycloud.com/wp-content/uploads/2023/07/outcome-password.svg" class="attachment-large size-large wp-image-56579" alt="">


	z = self.driver.find_element(By.CLASS_NAME,"attachment-large.size-large.wp-image-56579")
	z = self.driver.find_element(By.XPATH,"//img[@class='attachment-large.size-large.wp-image-56579']")

	z = self.driver.find_element(By.XPATH,"//[@class='attachment-large.size-large.wp-image-56579']")
	'''

	#>>>>>>>>
	#x = self.driver.find_element(By.XPATH, "//img[contains(@class,'attachment-large size-large') and contains(@src,'outcome-password.svg')]")
	#
	#rxp .. tag,class,src





