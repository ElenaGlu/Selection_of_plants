from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time

list_of_page = ['https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewer']
for page in range(2, 63):
    list_of_page.append(f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&page={page}sort=-viewers')


def get_data(html):
    list_of_all_links = []
    counter = 0
    driver = webdriver.Chrome()
    for url in list_of_page:
        counter += 1
        if counter % 10 == 0:
            counter = 0
            time.sleep(30)
            driver.quit()
            driver = webdriver.Chrome()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for link in soup.find_all('a', class_='title'):
            list_of_all_links.append('https://leplants.ru' + link.get('href'))
    driver.quit()
    print(list_of_all_links)

    js = json.dumps(list_of_all_links)
    with open("data.json", "a") as file:
        file.write(js)

# def get_description(html):
#     driver = webdriver.Chrome()
#     url = 'https://leplants.ru/cupressus/'
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
#
#     main_data_plants = []
#     description_table = soup.find('div', class_='jn1ow0-0 bqYbNV')
#     trs = description_table.find_all('tr')
#     for tr in trs:
#         tds = tr.find_all('td')
#         main_data_plants.append(tds[0].text)
#     main_data_plants.extend([None for _ in range(11 - len(main_data_plants))])
#
#     all_data_plants = {'name_of_plant': soup.find('h1', class_='hidden-xs').text,
#                        'pic_of_plant': soup.find('div', class_='item active').find('img').attrs['src'],
#                        'homeland': main_data_plants[0], 'soil': main_data_plants[1], 'size': main_data_plants[2],
#                        'flowering_time': main_data_plants[3], 'leaf_color': main_data_plants[4],
#                        'light_level': main_data_plants[5], 'irrigation_level': main_data_plants[6],
#                        'level_of_care': main_data_plants[7], 'humidity': main_data_plants[8],
#                        'feeding': main_data_plants[9], 'temperature': main_data_plants[10],
#                        'content_or_description': soup.find('div', class_='sc-4e9jew-13 cmbLRJ').text
#                        }
#     print(all_data_plants)


def main():
    get_data('html')


if __name__ == '__main__':
    main()
