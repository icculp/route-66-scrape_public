from bs4 import BeautifulSoup

tester = '<span class="street-address">437918 US-60</span>, <span class="locality">Vinita</span>, <span class="region">OK</span> <span class="postal-code">74301-7644</span>, <span class="country-name">USA</span>'

soup = BeautifulSoup(tester, features="html.parser")

Address = soup.find("span", {"class": "street-address"}).text if soup.find("span", {"class": "street-address"}) is not None else "NULL"
City = soup.find("span", {"class": "locality"}).text if soup.find("span", {"class": "locality"}) is not None else "NULL"
State = soup.find("span", {"class": "region"}).text if soup.find("span", {"class": "region"}) is not None else "NULL"
Zip = soup.find("span", {"postal-code"}).text if soup.find("span", {"class": "postal-code"}) is not None else "NULL"

print(Address)
print(City)
print(State)
print(Zip)
