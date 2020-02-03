import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
# import re
import csv
import time
import multiprocessing as mp

os.makedirs('./pic/', exist_ok=True)
os.makedirs('./doc/', exist_ok=True)
chrome_options = Options()
chrome_options.add_argument("--headless")  # define headless


def pic(result):
    img = []
    img_div = result.find_all('div', {'class': 'Virus_1-1-28_BZcgRf'})
    img.append(img_div[0].find_all('img'))
    img_url = img[0][0].get('src')
    r = requests.get(img_url)
    with open('./pic/0.png', 'wb') as f:
        f.write(r.content)
    print("Pic Done!")


def find_sheng():
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia")
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[5]/div/span").click()
    html = driver.page_source
    result = BeautifulSoup(html, features='lxml')
    driver.close()

    # pic(result)
    sheng = []
    forms = result.find_all('tr')
    for form in forms:
        sheng.append(form.find_all('td'))
    for i in range(len(sheng)):
        for j in range(len(sheng[i])):
            sheng[i][j] = sheng[i][j].get_text()
    with open('./doc/sheng.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['地区', '确诊', '治愈', '死亡'])
        for i in sheng:
            writer.writerow(i)
    f.close()
    print('Find_Sheng Done!')


def find_shi():
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia")
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[3]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[5]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[7]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[9]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[11]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[13]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[15]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[17]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[19]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[21]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[23]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[25]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[27]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[29]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[31]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[33]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[35]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[37]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[39]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[41]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[43]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[45]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[47]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[49]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[51]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[53]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[55]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[57]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[61]/td/div/span[2]").click()
    driver.find_element_by_xpath("//div[@id='ptab-0']/div[6]/div[2]/table/tbody/tr[64]/td/div/span[2]").click()
    html = driver.page_source
    result = BeautifulSoup(html, features='lxml')
    driver.close()

    shi = []
    forms = result.find_all('tr', {'class': "VirusTable_1-1-77_2AH4U9"})
    for form in forms:
        shi.append(form.find_all('td'))
    for i in range(len(shi)):
        for j in range(len(shi[i])):
            shi[i][j] = shi[i][j].get_text()
    with open('./doc/shi.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['地区', '确诊', '治愈', '死亡'])
        for i in shi:
            writer.writerow(i)
    print('Find_Shi Done!')


def find_info():
    driver = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia")
    driver.find_element_by_xpath("//div[@id='ptab-3']/div[2]/div[11]/span").click()
    html = driver.page_source
    result = BeautifulSoup(html, 'lxml')
    driver.close()

    info = []
    forms = result.find_all('div', {'class': "Virus_1-1-77_2SKAfr"})
    for form in forms:
        info.append(form.find_all('div', {'style': "position: relative;"}))
        # info.append(form.find_all('div', {'class': "Virus_1-1-28_2myqYf"}))
        # info.append(form.find_all('div', {'class': "Virus_1-1-28_TB6x3k"}))
    for i in range(len(info)):
        for j in range(len(info[i])):
            info[i][j] = info[i][j].get_text()
    with open('./doc/information.txt', 'w', encoding="utf-8") as f:
        for i in info:
            for j in i:
                f.writelines(j+'\n')
    f.close()
    print('Find_Info Done!')


if __name__ == '__main__':
    # while 1:
    #     pool = mp.Pool(4)
    #     pool.apply_async(find_sheng)
    #     pool.apply_async(find_shi)
    #     pool.apply_async(find_info)
    #     pool.close()
    #     pool.join()
    #     time.sleep(5)
    find_sheng()
    find_shi()
    find_info()
