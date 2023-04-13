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

    s = Service('/home/elena/pythonProject/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    with open('finder/management/commands/data.json', 'r') as read_json:
        json_urls = json.load(read_json)
        for link in json_urls:
            driver.get(link)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            list_with_li = []
            initial_dict = {}


            list_basic_info_plants = []


            table_about_plant = soup.find('div', class_='jn1ow0-0 bqYbNV')
            lines_with_tr = table_about_plant.find_all('tr')
            for tr in lines_with_tr:
                line_with_th = tr.find('th').text
                initial_dict[line_with_th] = None
                line_with_td = tr.find_all('td')
                for td_item in line_with_td:
                    line_with_ul = td_item.find_all('ul', class_='jn1ow0-3 jkDIse')
                    for ul_item in line_with_ul:
                        line_with_li = ul_item.find('li')
                        list_with_li.append(line_with_li.text)
                if len(list_with_li) > 0:
                    initial_dict[line_with_th] = list_with_li
                    list_with_li = []
                else:
                    initial_dict[line_with_th] = line_with_td[0].text


            for key in ['Родина','Возможные расцветки']:
                if isinstance(initial_dict[key], str):
                    initial_dict[key] = list(initial_dict[key])



            size = initial_dict[2].split()
            if len(size) > 3:
                min_height = size[1]
                max_height = size[3]
            else:
                min_height = 0
                max_height = size[1]

            basic_info_plants = {'name_of_plant': soup.find('h1', class_='hidden-xs').text,
                                 'pic_of_plant': soup.find('div', class_='item active').find('img').attrs['src'],
                                 'homeland': initial_dict[0], 'soil': initial_dict[1],
                                 'min_height': min_height, 'max_height': max_height,
                                 'flowering_time': initial_dict[3], 'leaf_color': initial_dict[4],
                                 'light_level': initial_dict[5], 'irrigation_level': initial_dict[6],
                                 'level_of_care': initial_dict[7], 'humidity': initial_dict[8],
                                 'feeding': initial_dict[9], 'temperature': initial_dict[10],
                                 'content_or_description': str(soup.find('div', class_='sc-4e9jew-13 cmbLRJ'))
                                 }
            list_basic_info_plants.append(basic_info_plants)
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
        main()
        create_plant_instances(get_description_items())
