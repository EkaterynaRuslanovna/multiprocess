import os
from selenium import webdriver
import time


def capture_screenshot(url, output_dir, sec=0):
    time.sleep(sec)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    unique_identifier = str(hash(url))

    screenshot_path = os.path.join(output_dir, f"{unique_identifier}.png")
    driver.save_screenshot(screenshot_path)

    driver.quit()

