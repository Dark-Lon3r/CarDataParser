import requests

from bs4 import BeautifulSoup as BS


header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


def search_car_func(num):
    r = requests.get(f"https://checkcar.com.ua/{num}", headers=header)
    soup = BS(r.text, 'html.parser') 

    try:
        car_title = soup.find('h1', class_='car-title').text.strip()
        vin_code = soup.find('span', class_ = 'vin').text.strip()
        description = soup.find('div', class_ = 'car-description mt-2 ng-star-inserted').text.strip()
        info = soup.find_all('tr', class_ = 'ng-star-inserted')
        search_car = soup.find('h3', class_ = 'second-accordion-title ng-star-inserted').text.strip()
        owner_car_count = soup.find('mat-accordion', class_='mat-accordion additional-accordion mat-accordion-multi').text.strip()


        info_list = []


        for tr in info:
            td_elements = tr.find_all('td')
            values = [td.text.strip() for td in td_elements]
            info_list.append(' '.join(values))

        return car_title, vin_code, description, search_car, owner_car_count, info_list

    except:
        return None