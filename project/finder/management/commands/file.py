import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from finder import models
from django.core.management.base import BaseCommand


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


def get_description_items():
    list_basic_info_plants = []
    counter = 0
    s = Service('/home/elena/pythonProject/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print(os.getcwd())
    with open('finder/management/commands/data.json', 'r') as read_json:
        json_urls = json.load(read_json)
        for link in json_urls:
            driver.get(link)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            list_add = []
            table_data_plants = []

            description_table = soup.find('div', class_='jn1ow0-0 bqYbNV')
            trs = description_table.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                for tds_item in tds:
                    uls = tds_item.find_all('ul', class_='jn1ow0-3 jkDIse')
                    for ul in uls:
                        lis = ul.find('li')
                        list_add.append(lis.text)
                if len(list_add) > 0:
                    table_data_plants.append(list_add)
                    list_add = []
                else:
                    table_data_plants.append(tds[0].text)
            table_data_plants.extend([None for _ in range(11 - len(table_data_plants))])

            size = table_data_plants[2].split()
            if len(size) > 2:
                min_height = size[1]
                max_height = size[3]
            else:
                min_height = 0
                max_height = size[1]

            basic_info_plants = {'name_of_plant': soup.find('h1', class_='hidden-xs').text,
                                 'pic_of_plant': soup.find('div', class_='item active').find('img').attrs['src'],
                                 'homeland': table_data_plants[0], 'soil': table_data_plants[1],
                                 'min_height': min_height, 'max_height': max_height,
                                 'flowering_time': table_data_plants[3], 'leaf_color': table_data_plants[4],
                                 'light_level': table_data_plants[5], 'irrigation_level': table_data_plants[6],
                                 'level_of_care': table_data_plants[7], 'humidity': table_data_plants[8],
                                 'feeding': table_data_plants[9], 'temperature': table_data_plants[10],
                                 'content_or_description': str(soup.find('div', class_='sc-4e9jew-13 cmbLRJ'))
                                 }
            list_basic_info_plants.append(basic_info_plants)
            counter += 1
            if counter == 2:
                driver.quit()
                break

        return list_basic_info_plants


def create_plant_instances(list_basic_info_plants):
    list_plant_instances = []
    for item in list_basic_info_plants:
        list_plant_instances.append(models.HousePlants(**item))
    models.HousePlants.objects.bulk_create(list_plant_instances)


def main():
    get_description_items()
    # links = get_links_pagination()
    # get_links_to_all_items(links)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # main()
        create_plant_instances(get_description_items())


