#Создаём сущность терминал на портале "Smartpay"
# ключи для терминала используем "Получить с KDH"
import Loginpage.test_login_page

def test_create_pos_with_kdh(self):
    self.test_positive_login()
    self.driver.find_element_by_tag_name('i').click()
    self.driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys("automerchant")
    self.driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys("autobusinesstype")
    self.driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys("autobusinesstype")
