import requests
from bs4 import BeautifulSoup


#функція для USD 
def get_currency_rate():
    url = "https://minfin.com.ua/currency/usd"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    rates = soup.find_all("div", class_="sc-1x32wa2-9")
    buy = rates[0].text.strip()
    sell = rates[1].text.strip()
    return buy, sell

#функція для EUR 
def get_euro():
    url = "https://minfin.com.ua/currency/eur"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    rates = soup.find_all("div", class_="sc-1x32wa2-9")
    buy = rates[0].text.strip()
    sell = rates[1].text.strip()
    return buy, sell




buy_rate, sell_rate = get_currency_rate()
euro_buy, euro_sell = get_euro()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#рядок для запису
line_usd = f"{now} | USD | купівля {buy_rate} грн | продаж {sell_rate} грн"
line_eur = f"{now} | EUR | купівля {euro_buy} грн | продаж {euro_sell} грн"

print("Курс доллара:")
print("Покупка:", buy_rate, "грн")
print("Продажа:", sell_rate, "грн")

print("\nКурс евро:")
print("Покупка:", euro_buy, "грн")
print("Продажа:", euro_sell, "грн")

# Збереження в файл 
with open("курси_валют.txt", "a", encoding="utf-8") as файл:
    файл.write(line_usd + "\n")
    файл.write(line_eur + "\n")
    файл.write("-" * 50 + "\n")   # роздільник для зручності
files.download("курси_валют.txt")
print("\nДані збережено в файл: курси_валют.txt")