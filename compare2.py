import numpy
import sys
import PIL.Image as Image
import time
import contextlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

t0=time.clock()

desired_cap = {'os': 'Windows', 'os_version': '8', 'browser': 'chrome', 'browser_version': '31.0'}


driver = webdriver.Remote(
    command_executor='http://arslpnpi1:ngUasHjNZDJVHTAxXX8Y@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)
driver.get("http://test.sad.affectv.co/build/53077dc9c2590814b73252d1/demo.html")
driver.maximize_window()
time.sleep(5)
# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/object/embed")))
driver.get_screenshot_as_file('/home/vlad/PycharmProjects/img_compare/screenshotimage.png')
driver.quit()

def main():
    t1=time.clock()
    img1 = Image.open('screenshotimage2.png')
    img2 = Image.open('screenshotimage.png')
    img1.crop((0,0,160,600)).save('pscreen.png')
    img2.crop((0,0,160,600)).save('pscreen2.png')
    im1 = Image.open('pscreen.png')
    im2 = Image.open('pscreen2.png')


    if im1.size != im2.size or im1.getbands() != im2.getbands():
        return -1

    s = 0
    # raise Exception('exeption')
    for band_index, band in enumerate(img1.getbands()):
        m1 = numpy.array([p[band_index] for p in im1.getdata()]).reshape(*im1.size)
        m2 = numpy.array([p[band_index] for p in im2.getdata()]).reshape(*im2.size)
        s += numpy.sum(numpy.abs(m1-m2))
    print s
    if s>25000:
        raise Exception('different')
    print(time.clock()-t1)
    print(time.clock()-t0)

if __name__ == "__main__":
    sys.exit(main())
