from bs4 import BeautifulSoup
from selenium import webdriver
import json


def get_links_pagination():
    list_links_pagination = [
        'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7'
        '&sort=-viewer']
    for page in range(2, 63):
        list_links_pagination.append(
            f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type'
            f'%3A7&page={page}sort=-viewers')
    return list_links_pagination


def get_links_to_all_items(list_links_pagination=None):
    list_links_to_all_items = []
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 600)
    for url in list_links_pagination:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for link in soup.find_all('a', class_='title'):
            list_links_to_all_items.append('https://leplants.ru' + link.get('href'))
    driver.quit()

    js = json.dumps(list_links_to_all_items)
    with open("data.json", "a") as file:
        file.write(js)



def get_description(html):
    driver = webdriver.Chrome()
    url = 'https://leplants.ru/cupressus/'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    main_data_plants = []
    description_table = soup.find('div', class_='jn1ow0-0 bqYbNV')
    trs = description_table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        main_data_plants.append(tds[0].text)
    main_data_plants.extend([None for _ in range(11 - len(main_data_plants))])

    all_data_plants = {'name_of_plant': soup.find('h1', class_='hidden-xs').text,
                       'pic_of_plant': soup.find('div', class_='item active').find('img').attrs['src'],
                       'homeland': main_data_plants[0], 'soil': main_data_plants[1], 'size': main_data_plants[2],
                       'flowering_time': main_data_plants[3], 'leaf_color': main_data_plants[4],
                       'light_level': main_data_plants[5], 'irrigation_level': main_data_plants[6],
                       'level_of_care': main_data_plants[7], 'humidity': main_data_plants[8],
                       'feeding': main_data_plants[9], 'temperature': main_data_plants[10],
                       'content_or_description': soup.find('div', class_='sc-4e9jew-13 cmbLRJ').text
                       }
    print(all_data_plants)


def main():
    # links = get_links_pagination()
    # get_links_to_all_items(links)


if __name__ == '__main__':
    main()
