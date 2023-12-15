import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor
import os

results = []


# 获取元素
def get_element(driver, type, value, mult, second=10):
    # 最多等待10秒
    wait = WebDriverWait(driver, second)
    wait.until(EC.presence_of_element_located((type, value)))
    if mult:
        return driver.find_elements(type, value)
    else:
        return driver.find_element(type, value)


def scroll_down(driver):
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


def login(driver, cityId):
    driver.get(
        "https://m.tujia.com/passport/RegisterPage?srcurl=https%3A%2F%2Fm.tujia.com%2Fhotel_city{0}".format(cityId))
    username = get_element(driver, By.CLASS_NAME, "tel-number", False)
    usernameInput = get_element(username, By.TAG_NAME, "input", False)
    password = get_element(driver, By.CLASS_NAME, "input-password", False)
    passwordInput = get_element(password, By.TAG_NAME, "input", False)
    checkbox = get_element(driver, By.CLASS_NAME, "tj-checkbox", False)
    submit = get_element(driver, By.CLASS_NAME, "btn-login", False)
    usernameInput.send_keys("19163540634")
    time.sleep(1)
    checkbox.click()
    passwordInput.send_keys("shanshan22")
    time.sleep(1)
    submit.click()

def start(cityId, cityName, areaName):
    driver = webdriver.Chrome()
    # 先跳转登录页
    login(driver, cityId)

    # 延迟100秒，判断是否已经跳转到首页
    play_btn = get_element(driver, By.CLASS_NAME, "city-label", False, 100)
    time.sleep(2)
    if len(areaName) != 0:
        time.sleep(1)
        play_btn.click()
        search_input = get_element(driver, By.CLASS_NAME, "search-input", True)
        search_input[1].send_keys(areaName)
        time.sleep(1)
        search_input[1].send_keys(Keys.ENTER)
    time.sleep(2)
    url = driver.current_url.replace("/?", "") + "/7-0,200/"
    driver.execute_script("window.location.replace('{0}')".format(url))
    # 滚动加载10页
    for _ in range(1):
        scroll_down(driver)
    lists = get_element(driver, By.CLASS_NAME, "unit-item-padding", True)
    hrefs = []
    for item in lists:
        href = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        hrefs.append(href)
    get_details(driver, hrefs)
    driver.quit()

    # 写入文件
    fileName = "datas/{0}.json".format(cityName + areaName)
    write_file(fileName)
    return results


def write_file(fileName):
    with open(fileName, "w") as f:
        json.dump(results, f)


def read_file(fileName):
    with open(fileName, "r") as f:
        return json.load(f)


def craw_detail(driver, href):
    # 获取图片或者视频
    swipe = get_element(driver, By.CLASS_NAME, "header-swiper-content", False)
    time.sleep(2)
    # 酒店名称
    nameDiv = get_element(driver, By.CLASS_NAME, "basic-info-title", False)
    nameSpan = get_element(nameDiv, By.TAG_NAME, 'span', False)
    name = nameSpan.text.strip()
    # 酒店地址
    address = get_element(driver, By.CLASS_NAME, "txt-addr", False).text.strip()
    around = get_element(driver, By.CLASS_NAME, "txt-traff", False).text.strip()
    swipe.click()
    imgs, videoUrl = get_media(driver)
    results.append({
        "link": href,
        "name": name,
        "address": address,
        "around": around,
        "imgs": imgs,
        "videoUrl": videoUrl
    })


def get_details(driver, hrefs):
    print(hrefs)
    # 不开启多线程，就一个页签慢慢打开
    for href in hrefs:
        driver.execute_script("window.open('{0}', '_blank');".format(href))
        # 获取所有窗口句柄
        all_handles = driver.window_handles
        # 切换到新打开的页签
        new_tab_handle = all_handles[1]
        driver.switch_to.window(new_tab_handle)
        craw_detail(driver, href)
        # 关闭当前页签
        driver.close()

        # 切换回原来的页面
        driver.switch_to.window(all_handles[0])
        time.sleep(1)


# 获取媒体文件
def get_media(driver):
    imgs = []
    videoUrl = ""
    # 判断是否存在播放按钮，如果有则去抓取视频，否则抓取图片
    playBtn = driver.find_elements(By.CLASS_NAME, "play-button")
    if len(playBtn) > 0:
        video = get_element(driver, By.TAG_NAME, "source", False)
        videoUrl = video.get_attribute("src")
    else:
        images = get_element(driver, By.CLASS_NAME, "cont-img", True)
        for img in images:
            imgUrl = img.get_attribute("data-src")
            imgs.append(imgUrl)
    return imgs, videoUrl


def get_data(cityId, cityName, areaName):
    fileName = "datas/{0}.json".format(cityName + areaName)
    if os.path.exists(fileName):
        return read_file(fileName)
    else:
        return start(cityId, cityName, areaName)


if __name__ == "__main__":
    login(webdriver.Chrome(), 44)
