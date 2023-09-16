import os
from concurrent.futures import ThreadPoolExecutor
from screenshot import capture_screenshot
import threading

if __name__ == "__main__":

    websites = ["https://jobs.dou.ua/", "https://petstore.swagger.io/", "https://google.com"]

    output_dir = "screenshots"
    os.makedirs(output_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=3) as executor:
        for website in websites:
            executor.submit(capture_screenshot, website, output_dir)

    print("Всі скріншоти створено та збережено в директорії 'screenshots'.")

    # V2
    # first = threading.Thread(target=capture_screenshot, args=("https://jobs.dou.ua/", output_dir, 4,), name="first")
    # first.start()
    # second = threading.Thread(target=capture_screenshot, args=("https://petstore.swagger.io/", output_dir, 1,), name="second")
    # second.start()
    # third = threading.Thread(target=capture_screenshot, args=("https://google.com", output_dir, 3,), name="third")
    # third.start()
