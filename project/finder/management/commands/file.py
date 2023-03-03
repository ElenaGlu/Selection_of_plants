from bs4 import BeautifulSoup
from selenium import webdriver

# def get_data(html):
#     driver = webdriver.Chrome()
#     url = 'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewers'
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
#
#     for link in soup.find_all('a', class_='title'):
#         print('https://leplants.ru' + link.get('href'))

def get_description(html):
    driver = webdriver.Chrome()
    url = 'https://leplants.ru/cupressus/'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()





    # plant1 = {'name_of_plant': '', 'homeland': '','soil': '','size': '','flowering_time': '',
    #       'leaf_color': '','light_level': '','irrigation_level': '','level_of_care': '',
    #       'humidity': '','feeding': '','temperature': '','pic_of_plant': '','content_or_description': '',}
    plant1 = {}
    plant1['name_of_plant'] = soup.find('h1', class_='hidden-xs').text
    print(plant1)


    # list_of_page=[]
    # for page in range(1,62):
    #     if page == 1:
    #         list_of_page.append('https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewers')
    #     else:
    #         list_of_page.append(f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&page={page}sort=-viewers')

def main():
    get_description('html')

if __name__=='__main__':
    main()