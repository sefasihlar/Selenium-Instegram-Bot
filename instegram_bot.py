from selenium import webdriver
import time
from user import user,password
from selenium.webdriver.common.keys import Keys
    
class instegram:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.browser = webdriver.Chrome()
    def Login(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.user)
        
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(4)

        self.browser.get(f"https://www.instagram.com/..name../")
        time.sleep(5)

       self.browser.find_element_by_xpath('//*[@id="mount_0_0_yM"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(5)
        dialog = self.browser.find_element_by_css_selector("div[role = dialog] ul ")
        fallowercaunt = len(dialog.find_elements_by_css_selector("li"))

        print(f"caunt:  {fallowercaunt}")
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(4)
            newcaunt = len(dialog.find_elements_by_css_selector("li"))
            sayac1=1
            while sayac1<=100:

                takipEt_button = self.browser.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{sayac1}]/div/div[2]/button'.format(sayac1=sayac1))
                
                if takipEt_button.text == "Takip Et":
                    takipEt_button.click()
                else:
                    pass
                
                time.sleep(2)
                
                sayac1+=1

            if fallowercaunt != newcaunt:
                pass
                fallowercaunt = newcaunt
                print(f"new cauntlar{newcaunt}")
                if newcaunt == "1000":
                    print("saymayı bitiriyoruz")
                    break
                    
                time.sleep(2)
            else:
                continue

        fallow = dialog.find_elements_by_css_selector("li")
    
        for users in fallow:
            link = users.find_element_by_css_selector("a").get_attribute("href")
            print(link)
            
x = instegram(user,password)
x.Login()
