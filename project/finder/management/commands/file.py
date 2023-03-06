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

    div = soup.find('div', class_='jn1ow0-0 bqYbNV')
    trs = div.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        print(tds[0].text)

    # data_of_plants = {}
    #
    # data_of_plants['name_of_plant'] = soup.find('h1', class_='hidden-xs').text
    # data_of_plants['homeland'] = soup.find()
    # data_of_plants['soil'] = soup.find()
    # data_of_plants['size'] = soup.find()
    # data_of_plants['flowering_time'] = soup.find()
    # data_of_plants['leaf_color'] = soup.find()
    # data_of_plants['light_level'] = soup.find()
    # data_of_plants['irrigation_level'] = soup.find()
    # data_of_plants['level_of_care'] = soup.find()
    # data_of_plants['humidity'] = soup.find()
    # data_of_plants['feeding'] = soup.find()
    # data_of_plants['temperature'] = soup.find()
    # data_of_plants['pic_of_plant'] = soup.find()
    # data_of_plants['content_or_description'] = soup.find()

    # print(data_of_plants)


    # list_of_page = ['https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewer']
    # for page in range(2, 62):
    #     list_of_page.append(f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&page={page}sort=-viewers')
    # print(list_of_page)

def main():
    get_description('html')


if __name__=='__main__':
    main()