from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    "C://chromedriver_win32//chromedriver.exe"
)  # PATh TO CHROME DRIVER

driver.get("https://www.oberlo.in/blog/motivational-quotes")
time.sleep(5)


html_list = driver.find_element_by_xpath('//*[@id="article-content"]/div[1]')
items = html_list.find_elements_by_tag_name("ol")
amount_ol = 0
for item in items:
    amount_ol += 1
print(amount_ol)
k = 1
for i in range(1, amount_ol):
    ol = driver.find_element_by_xpath(
        '//*[@id="article-content"]/div[1]/ol[' + str(i) + "]"
    )
    items = ol.find_elements_by_tag_name("li")
    amount_li = 0
    for item in items:
        amount_li += 1
    for j in range(1, amount_li, 1):
        text = driver.find_element_by_xpath(
            '//*[@id="article-content"]/div[1]/ol['
            + str(i)
            + "]/li["
            + str(j)
            + "]/span"
        ).text
        text.encode("utf-8")
        with open(
            "D:/ContentC/VideoContents for D4B/TXT/" + str(k) + ".txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(text)
        file.close()
        k += 1
