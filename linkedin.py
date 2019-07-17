import os
import time
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def is_in_page(selector):
    try:
        if "@" in selector:
            return driver.find_element_by_xpath(selector)
        return driver.find_element_by_css_selector(selector)
    except Exception:
        print(selector + ' Not found')
        return False


def click_if_exist(path_locator):
    element = is_in_page(path_locator)
    if element:
        element.click()
        return element
    return False


def type_if_exist(path_locator, keys_to_send):
    element = click_if_exist(path_locator)
    if element:
        element.send_keys(keys_to_send)


# driver = webdriver.Remote("firefox:4444")
driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://www.linkedin.com/learning/login?redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2F&trk=sign_in&upsellOrderOrigin=trk_default_learning")
driver.maximize_window()
try:
    for iframe in driver.find_elements_by_tag_name("iframe"):
        driver.switch_to.frame(iframe)
        if is_in_page('input#username'):
            break
        else:
            driver.switch_to.default_content()
except:
    print('no se puede cambiar a iframe')

type_if_exist('input#username', 'user@mail')
time.sleep(3)
type_if_exist('input#password', 'password')
time.sleep(4)
type_if_exist('input#password', Keys.ENTER)
time.sleep(8)
driver.switch_to.default_content()
courses = [
    'python-para-data-science-y-big-data-esencial',
    'istio-y-kubernetes-esencial',
    'kubernetes-para-desarrolladores-esencial',
    'kubernetes-para-administradores-it-esencial',
]
baseVideoPath = '/home/user/path'
for course in courses:
    time.sleep(8)
    numVideo = 1
    print('https://www.linkedin.com/learning/' + course)
    driver.get('https://www.linkedin.com/learning/' + course)
    time.sleep(10)
    if is_in_page('.course-toc__item-content.t-14.t-black.t-normal') == False:
        driver.get('https://www.linkedin.com/learning/' + course)
        time.sleep(15)
    try:
        os.mkdir(baseVideoPath + '/' + course)
    except:
        print('no se puede crear dir')
    try:
        for iframe in driver.find_elements_by_tag_name("iframe"):
            driver.switch_to.frame(iframe)
            if is_in_page('.course-toc__item-content.t-14.t-black.t-normal'):
                break
            else:
                driver.switch_to.default_content()
    except:
        print('no se puede cambiar a iframe')
    if is_in_page('.course-toc__item-content.t-14.t-black.t-normal'):
        videos = driver.find_elements_by_css_selector('.course-toc__item-content.t-14.t-black.t-normal')
        for video in videos:
            title = str(video.text)
            title = title.replace('/', '-')
            title = title.replace('\\', '-')
            print(title)
            video.click()
            time.sleep(8)
            mp4 = ''
            numVideoCasted = ''
            if numVideo < 10:
                numVideoCasted = '0' + str(numVideo)
            else:
                numVideoCasted = numVideo
            if is_in_page('.vjs-tech'):
                mp4 = is_in_page('.vjs-tech').get_attribute('src')
                print(mp4)
                urllib.request.urlretrieve(mp4, baseVideoPath + '/' + course + '/' + numVideoCasted + '-' + title + '.mp4')
            else:
                video.click()
                time.sleep(12)
                if is_in_page('.vjs-tech'):
                    mp4 = is_in_page('.vjs-tech').get_attribute('src')
                    print(mp4)
                    urllib.request.urlretrieve(mp4, baseVideoPath + '/' + course + '/' + numVideoCasted + '-' + title + '.mp4')
            time.sleep(15)
            numVideo = numVideo + 1
    driver.switch_to.default_content()

driver.close()
