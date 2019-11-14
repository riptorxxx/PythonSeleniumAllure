import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import time

#pc - Позитивный сценарий
#nc - Негативный сценарий
#pytest -v Loginpage\test_login_page.py --alluredir ./results
#allure serve ./results

@allure.feature('Open Page')
@allure.story('Open SmartPay Portal')
@allure.severity('blocker')

class TestLPage:

    def setup(self):
        self.driver = webdriver.Firefox(executable_path="C:/Users/de_ivanov/Documents/IdeaProjects/drivers/geckodriver.exe")
        self.driver.maximize_window()
        url = "http://10.129.106.73:8080"
        smartpay_portal = "//div[2]/p[2]/a"

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, smartpay_portal))
            )
            self.driver.find_element_by_xpath(smartpay_portal).click()
        except Exception as ex:
            print ('Connection Failed', ex)
            return ex.with_traceback()
        else:
            print('Successful opened'+ url)

        with allure.step('Take Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            print('Success open SmartPay-Portal')
    pass

    def teardown(self):
        self.driver.close()
    pass

#Тест на проверку входа в SmartPay-Portal с некорректным Login
    def test_nc_wrong_login(self):
        self.driver.find_element_by_name("login").send_keys("neadmin")
        self.driver.find_element_by_name("password").send_keys("admin")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        with allure.step('Take Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='EnterWithBadLogin', attachment_type=AttachmentType.PNG)
            print('Bad Login screenshot created')

    #Проверяем отображение модального окна при вводе неправильного логина

        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='info-modal']/div/div"))
            )
        except Exception as ex:
            print ("modal-notification not found \n")
            return ex.with_traceback()

        else:
            print('Success negative test case. Authorization Error - bad login')

#Тест на проверку входа в SmartPay-Portal с некорректным Password
    def test_nc_wrong_password(self):
        self.driver.find_element_by_name("login").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("neadmin")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        with allure.step('Take Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='EnterWithBadLogin', attachment_type=AttachmentType.PNG)
            print('Bad Password screenshot created')
        #Проверяем отображение модального окна при вводе неправильного логина
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='info-modal']/div/div"))
            )
        except Exception as ex:
            print ("modal-notification not found \n")
            return ex.with_traceback()
        else:
            print('Success negative test case. Authorization Error - bad password')

#Тест на проверку входа в SmartPay-Portal с корректными Login & Password
    def test_pc_login(self):
        self.driver.find_element_by_name("login").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("admin")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_all_elements_located((By.XPATH, "//dx-data-grid[@id='terminals-grid']/div/div[6]"))
            )
        except Exception as ex:
            print('Not displayed elements')
            return ex.with_traceback()

        time.sleep(1)
        with allure.step('Take Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='TerminalPage', attachment_type=AttachmentType.PNG)
            print('Success Enter SmartPay-Portal.')
    pass


