from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from typing import List
from crop import Crop
import json
from rich import print

class CropService():
    def __init__(self) -> None:
        pass

    def fetch_crop_prices(driver: WebDriver) -> List[Crop]:

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try: 
            driver.get("https://www.scic.ca/ci/prices")
            title = driver.title
            assert title , 'Prices | SCIC'
            table = driver.find_element(By.XPATH, '//*[@id="main"]/div/article/table[1]')

            rows = table.find_elements(By.TAG_NAME, 'tr')

            records : List[Crop] = list()
            for row in rows:
                row_data = row.find_elements(By.TAG_NAME, 'td')
                if row_data:
                    records.append(
                        Crop(
                            name=row_data[0].text,
                            base_grade=row_data[1].text,
                            base_dollar_t=float(row_data[2].text.replace(',','')) if len(row_data[2].text) > 0 else 0,
                            low_price_dollar_t=float(row_data[3].text.replace(',','')) if len(row_data[3].text) > 0 else 0,
                            base_dollar_bu=float(row_data[4].text.replace(',','')) if len(row_data[4].text) > 0 else 0,
                            low_price_dollar_bu=float(row_data[5].text.replace(',','').replace(' #','')) if len(row_data[5].text) > 0 else 0,
                        )
                    )
            return records 

        except Exception as e:
            print(e)
            return None
        finally:
            driver.close()
    