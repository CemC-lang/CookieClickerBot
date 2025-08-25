from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time
import schedule

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Store Section
store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
value_text = [a.text for a in store_items]

# if a > 0
  #append.array und dan mit max die größte Anzahl raussuchen
item_value = []
def convert_item_string_into_int():
    for b in range(len(value_text) - 1):
        tem_string = ""
        for item_string in value_text[b]:
            if item_string.isdigit():
                tem_string += item_string
        item_value.append(int(tem_string))

convert_item_string_into_int()
def check_item_options():
    money = driver.find_element(By.CSS_SELECTOR, '#money')
    money = convert_money_into_int(money.text)
    zu = 0
    for a in range(len(item_value)):
        if money > item_value[a]:
            zu = a + 1
    store_item = driver.find_element(By.CSS_SELECTOR, value=f'#store  > div:nth-child({zu})')
    store_item.click()

def convert_money_into_int(money):
    money_string = ""
    for a in money:
        if a.isdigit():
            money_string += a
    return int(money_string)


schedule.every(5).seconds.do(check_item_options)
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
end = time() + (5*60)
while time() < end:
    cookie.click()
    schedule.run_pending()

cps = driver.find_element(By.CSS_SELECTOR, "#cps")
print(cps.text)
driver.quit()






