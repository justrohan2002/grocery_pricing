from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_driver_path = Service("C:\Development\chromedriver.exe")

# driver = webdriver.Chrome(service=chrome_driver_path)

driver.get(
    "https://www.bigbasket.com/pc/fruits-vegetables/organic-fruits-vegetables/?nc=&%20Vegetables&t_pg=%2Fnov-t1-home-page%2F&t_p=nov-t1-2022&t_s=Fruits%20&t_pos_sec=6&t_pos_item=1&t_ch=desktop")

price = driver.find_elements(by=By.CLASS_NAME, value="discnt-price")

all_prices = []

for p in price:
    all_prices.append(p.text)

names = driver.find_elements(by=By.CLASS_NAME, value="prod-name")
all_names = []

for n in names:
    all_names.append(n.text.split("\n")[1])

res = {all_names[i]: all_prices[i] for i in range(len(all_names))}

with open("my_file.text", mode="w") as file:
    file.write("Product:Price")
    for key, value in res.items():
        file.write("\n")
        file.write(f"{key}:{value}")
        file.write("\n")

driver.close()
