import requests
import sys


def check_website(url):
    try:
        response = requests.get(url)

        if 200 <= response.satus_code < 300:
            print(f'The website at {url} is working.')

        else:
            print(f'the website at {url} returned a status code {response.status_code}. The website may not function.')

    except requests.exception.requestException:
        print(f'An error occurred while trying to reach {url}. The website may not be functional.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: Python check_website.py <URL>')
    else:
        url = sys.argv[1]
        check_website(url)
