
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

def list_to_xlsx(data_list, filename="out/output.xlsx"):
	filepath = os.path.abspath(filename)
	df = pd.DataFrame(data_list)
	df.to_excel(filepath, index=False)

def parse_pages():
	url_f = "https://www.propertyfinder.ae/en/find-agent/search?page="
	headers = {'User-Agent': 'Mozilla/5.0'}
	i = 0
	out_str = ""
	try:
		while True:
			i += 1
			print(f"Парсю {i} страницу...")
			url = url_f+str(i)
			soup = BeautifulSoup(requests.get(url, headers=headers).content, "lxml")
			if soup.find("img", {"alt":"Coming soon on desktop!"}):
				print("ДАННОЙ СТРАНИЦЫ НЕ СУЩЕСТВУЕТ")
				break
			print(f'Добавляю {len(soup.findAll("a", {"role":"listitem"}))} анкет')
			for el in soup.findAll("a", {"role":"listitem"}):
				out_str += f'https://www.propertyfinder.ae{el.get("href")}\n'
	except KeyboardInterrupt:
		print("Сохраняю то, что есть сейчас...")
	finally:
		with open(os.path.abspath("cache/urls.txt"), "w") as f:
			f.write(out_str)

def parse_ankets():
	out = []
	with open(os.path.abspath("cache/urls.txt")) as f:
		ankets = f.read().split("\n")
	try:
		for anket in ankets:
			if anket.strip() != "":
				print(f"Парсю {anket}")
				d = {}
				headers = {'User-Agent': 'Mozilla/5.0'}
				soup = BeautifulSoup(requests.get(anket, headers=headers).content, "lxml")
				d["ФИО"] = soup.find("h1").text
				try:
					d["Агенство"] = soup.find("img", {"data-testid":"agent-broker-image"}).findParent().findParent().findParent().findParent().findAll("span")[-1].text
				except:
					d["Агенство"] = soup.find("a", string="About Company").findParent().findAll("span")[-1].text
				d["Национальность"] = soup.find("span", {"style":"box-sizing:border-box;display:inline-block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:relative;max-width:100%"}).findParent().text.replace("Nationality:", "")
				d["Языки"] = soup.find("span", {"style":"box-sizing:border-box;display:inline-block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:relative;max-width:100%"}).findParent().findParent().findAll("div")[-1].findAll("span")[-1].text
				d["whatsapp"] = soup.find("a", {"data-testid":"whatsapp-btn"}).get("href")
				d["телефон"] = soup.find("a", {"data-testid":"phone-btn"}).get("href")
				out.append(d)
	except KeyboardInterrupt:
		print("Я остановлен")
	finally:
		print("Сохраняю в xlsx")
		list_to_xlsx(out)
		print("Сохранено!")


def main():
	if not os.path.isdir("cache"):
		os.mkdir("cache")
	if not os.path.isdir("out"):
		os.mkdir("out")
	if not os.path.exists(os.path.abspath("cache/urls.txt")):
		parse_pages()
	parse_ankets()

if __name__ == '__main__':
	main()