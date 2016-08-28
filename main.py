# This program is an interactive app that allows the user to input their zip
# code and obtain the weather in their location.

import requests
import sys

from bs4 import BeautifulSoup

from utils import remove_tabs_new_lines, user_response, Weather

# sys.setdefaultencoding('utf-8')


def main():
    print_header()

    while True:
        zipcode = user_response('Enter your zip code...')
        html = get_html_for_zip(zipcode)
        weather = parse_html(html)

        print(u"Weather in {city}: {temp}, {cond}, with {hum}% humidity".format(
            city=weather.city,
            temp=weather.temp,
            cond=weather.cond,
            hum=weather.humidity
        ))


def print_header():
    """Prints header for the app."""
    print('-'*50)
    print('-'*50)
    print('\n')
    print('Weather App'.center(50, ' '))
    print('\n')
    print('-'*50)
    print('-'*50)


def get_html_for_zip(zipcode):
    """Returns the HTML response from wunderground.com for a given :zipcode:."""
    r = requests.get(
        'https://www.wunderground.com/weather-forecast/{}'.format(zipcode))
    return r.text


def parse_html(html):
    """Parses :html: response and returns a :Weather: namedtuple containing
    weather information."""
    soup = BeautifulSoup(html, 'html.parser')
    # print soup
    return Weather(
        city=location_from_soup(soup),
        temp=temp_from_soup(soup),
        cond=cond_from_soup(soup),
        humidity=humidity_from_soup(soup)
    )


def location_from_soup(soup):
    """Gets location from wunderground soup result."""
    loc = soup.find(id='location').find('h1').get_text()
    return remove_tabs_new_lines(loc)


def temp_from_soup(soup):
    """Gets temperature from wunderground soup result."""
    temp = soup.find('div', {'id': 'curTemp'}).get_text()
    return remove_tabs_new_lines(temp)


def cond_from_soup(soup):
    """Gets weather conditions from wunderground soup result."""
    cond = soup.find('div', {'id': 'curCond'}).find(
        'span', 'wx-value').get_text()
    return remove_tabs_new_lines(cond)


def humidity_from_soup(soup):
    """Gets humidity from wunderground soup result."""
    humidity = soup.find('span',
                         {'class': 'wx-data',
                          'data-variable': 'humidity'}).find('span').get_text()
    return humidity

if __name__ == '__main__':
	main()
