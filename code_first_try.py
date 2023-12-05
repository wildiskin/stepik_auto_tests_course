from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
try:
    browser.get('https://www.google.com/search?q=%D0%BA%D0%B0%D0%BA+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D1%81%D1%8B%D1%80%D1%83%D1%8E+%D1%81%D1%82%D1%80%D0%BE%D0%BA%D1%83+python&oq=%D0%BA%D0%B0%D0%BA+%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D1%81%D1%8B%D1%80%D1%83%D1%8E+%D1%81%D1%82%D1%80%D0%BE%D0%BA%D1%83+&gs_lcrp=EgZjaHJvbWUqBwgCECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDc2MTlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8')
    sleep(5)
finally:
    browser.quit()