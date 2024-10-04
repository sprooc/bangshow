from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import os
import requests

base_url = "https://bestdori.com/tool/explorer/asset/jp/characters/resourceset/"
cache_dir = os.path.join(os.path.expanduser("~"), ".bangshow")
os.makedirs(cache_dir, exist_ok=True)
output_path = cache_dir + "/pics"
res_elements = []

def get_images(driver, url):
    driver.get(url)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[data-v-ba1ebbcc]"))
    )

    img_elements = driver.find_elements(By.CSS_SELECTOR, "img[data-v-ba1ebbcc]")
    png_images = [img.get_attribute("src") for img in img_elements if img.get_attribute("src").endswith(".png")]
    return png_images

def download_image(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(path, "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def get_pics_char(driver, char_id):
    num_str = 'res' + str(char_id).zfill(3)

    res_contents = [text for text in res_elements if text.startswith(num_str)]
    os.makedirs(output_path, exist_ok=True)

    def res_get_images(res):
        png_urls = get_images(driver, base_url + res)
        res_path = os.path.join(output_path, res)
        os.makedirs(res_path, exist_ok=True)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            # Download images concurrently
            executor.map(lambda url: download_image(url, os.path.join(res_path, os.path.basename(url))), png_urls)

    for res in res_contents:
        res_get_images(res)

def get_pics(band_id=None, char_id=None):
    global res_elements
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Reuse the driver for multiple functions
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(base_url)

        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[data-v-4cb50f40][class='m-l-xs']"))
        )

        span_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-v-4cb50f40][class='m-l-xs']")
        res_elements.extend(span.text for span in span_elements)

        if band_id:
            for i in range(band_id * 5 - 4, band_id * 5 + 1):
                get_pics_char(driver, i)
        elif char_id:
            get_pics_char(driver, char_id)
        else:
            for i in range(1, 41):
                get_pics_char(driver, i)


