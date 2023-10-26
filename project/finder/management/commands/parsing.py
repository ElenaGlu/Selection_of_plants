import json
from typing import List

from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib.request

from finder import models


def get_links_pagination() -> List[str]:
    """
    Returns a list of links in the form of strings for pagination.
    :return: Returns a list of links.
    """
    list_links_pagination = [
        'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7'
        '&sort=-viewer']
    for page in range(2, 63):
        list_links_pagination.append(
            f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type'
            f'%3A7&page={page}sort=-viewers')
    return list_links_pagination


def get_links_to_all_items(list_links_pagination: List[str])-> None:
    """
    Iterated through a list of links in the form of strings for pagination.
    Collect links to all items and adds them to a new list.
    Data from the new list is written to a json file.
    """
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
    with open("links.json", "a") as file:
        file.write(js)


def get_description_items() -> List[dict]:
    """
    Iterated by links in the form of strings in a json file.
    In each link, it collects data from a descriptive table and writes it to the dictionary.
    Conversion of string values of two dictionary objects to the list data type.
    Splitting a string into two values: min, max.
    Creating a dictionary with data from a table for each element.
    Creates a list from dictionaries.
    :return: returns a list of dictionaries.
    """

    s = Service('/home/elena/pythonProject/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    with open('links.json', 'r') as read_json:
        json_urls = json.load(read_json)
        for link in json_urls:
            driver.get(link)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            list_main_info_plant = []
            list_with_li = []
            initial_dict = {}
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

            temp_list = []
            for key in ['Родина', 'Возможные расцветки']:
                if isinstance(initial_dict.get(key, None), str):
                    temp_list.append(initial_dict[key])
                    initial_dict[key] = temp_list
                    temp_list = []

            size = initial_dict.get('Размер', None)
            if size:
                size = initial_dict.get('Размер', None).split()
                if len(size) > 3:
                    initial_dict['min_height'] = size[1]
                    initial_dict['max_height'] = size[3]
                else:
                    initial_dict['min_height'] = 0
                    initial_dict['max_height'] = size[1]

            main_info_plant = {'name_of_plant': soup.find('h1', class_='hidden-xs').text,
                               'pic_of_plant': soup.find('div', class_='item active').find('img').attrs['src'],
                               'min_height': initial_dict.get('min_height', None),
                               'max_height': initial_dict.get('max_height', None),
                               'homeland': initial_dict.get('Родина', None),
                               'soil': initial_dict.get('Почва', None),
                               'flowering_time': initial_dict.get('Время цветения', None),
                               'leaf_color': initial_dict.get('Возможные расцветки', None),
                               'light_level': initial_dict.get('Освещенность', None),
                               'irrigation_level': initial_dict.get('Полив', None),
                               'level_of_care': initial_dict.get('Сложность ухода', None),
                               'humidity': initial_dict.get('Влажность воздуха', None),
                               'feeding': initial_dict.get('Частота удобрения', None),
                               'temperature': initial_dict.get('Температура содержания', None),
                               'content_or_description': str(soup.find('div', class_='sc-4e9jew-13 cmbLRJ'))
                               }
            list_main_info_plant.append(main_info_plant)
        return list_main_info_plant


def create_plant_instances(list_main_info_plant: List[dict]) -> None:
    """
    Adding objects to the database.
    """
    list_plant_instances = []
    for item in list_main_info_plant:
        list_plant_instances.append(models.HousePlants(**item))
    models.HousePlants.objects.bulk_create(list_plant_instances)

def create_short_name() -> None:
    """
    Creating a new field and adding a short name to it.
    """
    list_short_name = []
    for item in models.HousePlants.objects.all():
        name = item.name_of_plant
        item.short_name = name.split('(')[0]
        list_short_name.append(item)
    models.HousePlants.objects.bulk_update(list_short_name, ['short_name'])


def download_main_img() -> None:
    """
    Uploading images by link from the database(local).
    """
    for item in models.HousePlants.objects.all():
        name_img = item.name_of_plant
        url_img = item.pic_of_plant
        full_path = '/home/elena/pythonProject/site/project/finder/static/main img/' + name_img + '.jpg'
        urllib.request.urlretrieve(url_img, full_path)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # create_short_name()
        # links = get_links_pagination()
        # get_links_to_all_items(links)
        # s = get_description_items()
        # create_plant_instances(s)
        # download_main_img()




