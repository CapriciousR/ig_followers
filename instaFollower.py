from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstaFollower:
    def __init__(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=edge_options)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        
    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_field = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
    
        self.driver.implicitly_wait(10)
        login_info_popup = self.driver.find_element(By.XPATH, value='//div[contains(text(), "Not now")]')
        login_info_popup.click()
        
        self.driver.implicitly_wait(2)
        notif_popup = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Not Now')]")
        notif_popup.click()
        
        # reminder_popup = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        # reminder_popup.click()
        
    def find_followers(self, acc_name):
        search_button = self.driver.find_element(By.XPATH, value='//span[contains(text(), "Search")]')
        search_button.click()
        self.driver.implicitly_wait(2)
        search_input = self.driver.find_element(By.TAG_NAME, value='input')
        search_input.send_keys(acc_name)
        search_input.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(8)
        account = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div')
        account.click()
        self.driver.implicitly_wait(5)
        following = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a')
        user_cnt = int(self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span').text)
        following.click()
        self.driver.implicitly_wait(4)
        users_dialog = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", users_dialog)
            self.driver.implicitly_wait(2)
        
        