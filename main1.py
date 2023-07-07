import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_results(search):
    url = "https://www.google.com/"
    browser = webdriver.Chrome()
    browser.get(url)
    
    # Wait until the search box is visible
    search_box = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(search)
    search_box.submit()
    
    # Wait until the search results are visible
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='g']//a"))
    )
    
    links = browser.find_elements(By.XPATH, "//div[@class='g']//a")
    results = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    
    browser.close()
    return results


s = input("Enter your search term: ")
get_results(s)
