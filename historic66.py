#!/usr/bin/env python3
"""
    Web scraper for Route 66 places of interest
"""
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def information():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--disable-dev-shm-usage')
    op.add_argument('--no-sandbox')

    page_number = 1
    name_url = {}
    name_address = {}

    while (1):
        try:
            # url for each point of interest page
            url = 'https://www.historic66.com/points-of-interest/?filter=active&state=oklahoma&list=' + str(page_number)
            browser = webdriver.Chrome(options=op)
            browser.implicitly_wait(3)
            browser.get(url)
            print("page number: {}".format(page_number))
            for i in range(1, 10):
                select_link = 'body > main > section.content-section > div > div.tabs-block.filter-block > div > div.tabs-panes.content-block-main.border-content > div.left-content.content-ajax > div > div.gallery-block-filter.flex-blocks > a:nth-child(' + str(i) + ')'
                selector = 'body > main > section.content-section > div > div.tabs-block.filter-block > div > div.tabs-panes.content-block-main.border-content > div.left-content.content-ajax > div > div.gallery-block-filter.flex-blocks > a:nth-child(' + str(i) + ') > span'
                selected_name = browser.find_element_by_css_selector(selector).text
                selected_link = browser.find_element_by_css_selector(select_link).get_attribute('href')
                print("selected_name: {} selected_link: {}".format(selected_name, selected_link))

                name_url.update({selected_name: selected_link})

            page_number += 1
        except Exception as e:
            print("Error {}".format(e))
            break
        finally:
            browser.quit()

    for name, url in name_url.items():
        try:
            browser = webdriver.Chrome(options=op)
            browser.implicitly_wait(1)
            browser.get(url)
            address = browser.find_element_by_css_selector('body > main > section.content-section > div > div.poi-detail.border-content.content-block-main > div.left-content > div.padding-carousel.border-block > div.information-poi > div > div:nth-child(2) > p').text
            print("name: {} address: {}".format(name, address))
            name_address.update({name: address})
        except Exception as e:
            print("Error {}".format(e))
            break
        finally:
            browser.quit()

        return name_address

filename = 'historic66.json'
jayson = information()
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(jayson, f)
