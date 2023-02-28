from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(html):
    driver = webdriver.Chrome()
    url = 'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share&lfilter=type%3A7&sort=-viewers'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    print(1)
    for link in soup.find_all('a', class_='title'):
        print('https://leplants.ru' + link.get('href'))
def main():
    get_data('html')

if __name__=='__main__':
    main()