from bs4 import BeautifulSoup as soup

import requests

_URL_PROXIES = 'https://free-proxy-list.net/'
_URL_TEST = 'https://httpbin.org/ip'


def get_proxies(only_https=True):

    # Get web page with list of free proxies
    proxy_web_site = _URL_PROXIES
    response = requests.get(proxy_web_site)

    # Parse web page using BeautifulSoup
    page_html = response.text
    page_soup = soup(page_html, "html.parser")

    # Extract container <div> element that contains the table with the list of proxies
    container = page_soup.find_all("div", {"class": "table-responsive"})[0]

    # Extract all <td> elements from the table within the container
    td_elements = container.find_all("td")

    proxies = set()

    # Each proxy row has 8 columns i.e. <td> elements
    ip_index = [8 * k for k in range(80)]

    # Iterate through each row set of <td> elements and extract proxy details
    for i in ip_index:

        ip = td_elements[i].text
        port = td_elements[i + 1].text
        https = td_elements[i + 6].text

        print(f'ip address {i}: {ip}, port: {port}, https: {https}')

        if not only_https or (https == 'yes' and only_https):
            proxy = ip + ':' + port
            proxies.add(proxy)

    return proxies


def check_proxies(proxies):

    working_proxies = set()

    for proxy in proxies:

        print(f'Trying to connect with proxy: {proxy}')

        try:

            response = requests.get(_URL_TEST, proxies={"http": proxy, "https": proxy}, timeout=5)

            print(f'Proxy {proxy} added: {response.json()}')

            working_proxies.add(proxy)

        except:

            print('Skipping. Connection error')

    return working_proxies


proxies = get_proxies()

print(f'{len(proxies)} proxies were found from {_URL_PROXIES}')

proxies = check_proxies(proxies)

print(len(proxies), proxies)

print(f'{len(proxies)} proxies are OK')
