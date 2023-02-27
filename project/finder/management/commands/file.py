import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(link):
    response = requests.get(link)
    return response.text

def main():
    link='https://leplants.ru/choose-plant/'
    print(get_html(link))

if __name__=='__main__':
    main()