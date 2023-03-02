from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(html):
    driver = webdriver.Chrome()
    url = 'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewers'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    list_of_page=[]
    for page in range(1,62):
        if page == 1:
            list_of_page.append('https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewers')
        else:
            list_of_page.append(f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&page={page}sort=-viewers')

        for link in soup.find_all('a', class_='title'):

        print('https://leplants.ru' + link.get('href'))
def main():
    get_data('html')

if __name__=='__main__':
    main()