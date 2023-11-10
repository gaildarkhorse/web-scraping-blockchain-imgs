import json
import os
import time
import glob
from sanitize_filename import sanitize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import linkPy 

issue_created = False
extension_paths = [
    "adblocker.crx",
    "XBlocker 1.0.4",
    "XBlocker 1.0.4 - langpack"
]
#######################################################################################################
chrome_options = webdriver.ChromeOptions()
    
chrome_options.add_argument("--user-data-dir=")
    
unpacked_extension_paths = []
for extension_path in extension_paths:
    if extension_path.endswith(".crx"):
        crx_extension_path = os.path.abspath(extension_path)
        print(crx_extension_path)
        chrome_options.add_extension(extension_path)
    else:
        unpacked_extension_path = os.path.abspath(extension_path)
        print(unpacked_extension_path)
        unpacked_extension_paths.append(unpacked_extension_path)

# Join the unpacked extension paths with commas
unpacked_extensions_argument = ",".join(unpacked_extension_paths)
chrome_options.add_argument("--load-extension=" + unpacked_extensions_argument)
chrome_options.add_argument("--start-maximized")

download_path = r'C:\BlockchainImg'
cache_path=download_path+r'\cache'
download_path_keer = r'C:\BlockchainImg'
chrome_options.add_experimental_option('prefs', {
"download.default_directory": download_path, # change default directory for downloads
"download.prompt_for_download": False, # to auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True # it will not show PDF directly in chrome
})
chrome_options.add_argument(f"user-data-dir={cache_path}")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://pngtree.com/so/blockchain")

for index in range(21, 53):
    print(f">>>>>>>>>>>>>>>>> {index}")
    #wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/main/div/section/div/ul/li[{index}]/div/figure/a'))).click()
    #parent_element = driver.find_element(By.XPATH, f'/html/body/div/main/div/section/div/ul/li[{index}]/div/figure/a')
    try:
        parent_element = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, f'/html/body/div/main/div/section/div/ul/li[{index}]/div/figure/a'))
            )
    except TimeoutException:
        print(">>> Time Out Exception Occured")
    
    try:
        url = parent_element.get_attribute('href')
    except TimeoutException:
        print(">>> Time Out Exception Occured")        
    
    try:
        driver.get(url)
    except:
        print(">>> get contents error")
    try:
        _element = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, f'/html/body/div/main/div/article/div[1]/div[2]/div[1]/div[2]/div/div/figure'))
            )
    except TimeoutException:
        print(">>> Time Out Exception Occured")
        
    subelement = _element.find_element(By.TAG_NAME, 'img')
    props = subelement.get_attribute('src')
    driver.get(props)
    print(props)
    time.sleep(3)
    #driver.switch_to.window(driver.window_handles[0])
    driver.back()
    time.sleep(3)
    driver.back()
#select = Select(driver.find_element(By.XPATH, '/html/body/div/main/div/article/div[1]/div[2]/div[1]/div[2]/div/div/figure'))
#wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div/article/div[1]/div[2]/div[1]/div[2]/div/div/figure'))).click()

print(">>>>>>>>>>>>>>", _element)
time.sleep(5)
#/html/body/div/main/div/section/div/ul/li[53]/div/figure/a
#/html/body/div/main/div/section/div/ul/li[21]/div/figure/a
#/html/body/div/main/div/article/div[1]/div[2]/div[1]/div[2]/div/div/figure
#element = driver.find_element_by_xpath('//*[@id="__main"]/div/section/div/ul/li[2]/div/figure/a')
# Wait for the page to load completely
time.sleep(10)





