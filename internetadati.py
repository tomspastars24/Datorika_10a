import os
os.system('cls')
print("\n")


import requests
from bs4 import BeautifulSoup
from plyer import notification 



url= "https://www.timeanddate.com/worldclock/uk"

def get_weather_data(url):
    try:
        r=requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException  as e:
        print(f"Kļūda: {e}")
        return None

htmldata = get_weather_data(url)

if htmldata:
    soup = BeautifulSoup(htmldata, "html.parser")
    #print(soup.prettify())
    temp_elem = soup.find("span", id="ct")
    rain_elem = soup.find("span", id="ctdat")

    temperature = temp_elem.text if temp_elem else "Nav datu"
    mitrums = rain_elem.text if rain_elem else "Nav nokrišņu informācijas "

    result = f"Pašreizējais laiks Londonā: {temperature}\ndatums: {mitrums}"

    notification.notify(
        title = "Laiks Londonā",
        message = result,
        timeout = 10
    )
else:
    notification.notify(
        title = "Kļūda",
        message = "Nekas nav zināms!!!",
        timeout = 10
    )


# def get_weather_data(url):
#     try:
#         r=requests.get(url, timeout=10)
#         r.raise_for_status()
#         return r.text
#     except requests.exceptions.RequestException  as e:
#         print(f"Kļūda: {e}")
#         return None

# htmldata = get_weather_data(url)

# if htmldata:
#     soup = BeautifulSoup(htmldata, "html.parser")
#     temp_elem = soup.find("span", {"data-testid": "TemperatureValue"})
#     rain_elem = soup.find("span", {"data-testid": "PercentageValue"})

#     temperature = temp_elem.text if temp_elem else "Nav datu"
#     mitrums = rain_elem.text if rain_elem else "Nav nokrišņu informācijas "

#     result = f"Pašreizējā temperatūra Rīgā: {temperature}\nmitrums: {mitrums}"

#     notification.notify(
#         title = "Laika ziņas Rīgā",
#         message = result,
#         timeout = 10
#     )
# else:
#     notification.notify(
#         title = "Kļūda",
#         message = "Nekas nav zināms!!!",
#         timeout = 10
#     )
