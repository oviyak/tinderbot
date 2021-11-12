from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

#oviyarockz@hotmail.com
driver = webdriver.Chrome(executable_path="C:/Users/oviya/Downloads/chromedriver_win32/chromedriver.exe")

#FB login
driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1636746815103%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3227e785341dd%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff11e8fdfe15eec%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Df1654dcd983a634%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28477779366f88%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff11e8fdfe15eec%2526relation%253Dopener%2526frame%253Df381d8486bd4268%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28477779366f88%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff11e8fdfe15eec%26relation%3Dopener%26frame%3Df381d8486bd4268%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0")
time.sleep(10)

#tinder page
driver.get("https://tinder.com/")

#Login

driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(2)

#login with FB
driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(10)

#ALlow location
driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(5)

#enable something
driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div/div/div[3]/button[1]').click()
act=ActionChains(driver)

#AUtomatatic right arrow
act.send_keys(Keys.RIGHT).perform()


# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span').click()

for i in range(5):
    time.sleep(3)
    act.send_keys(Keys.RIGHT).perform()
    time.sleep(3)
driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[2]/button[2]').click()
time.sleep(3)
for i in range(5):
    time.sleep(3)
    act.send_keys(Keys.RIGHT).perform()
    time.sleep(3)

