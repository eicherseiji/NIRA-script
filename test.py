from bs4 import BeautifulSoup
import requests
import csv
import time
import random

rows = []
jobs = []
keys = ['\b', "Bank", "Banking", "Finance"]
siteURL = "http://www.simplyhired.com"
baseURL = "http://www.simplyhired.com/search?q=%s&l="
testURL = "http://www.simplyhired.com/search?q=system+engineer+bank+&l="

def getCompanies(oldSoup):
	menu = oldSoup.find("div", class_="dropdown-submenu")
	items = menu("a", class_="dropdown-item")
	for item in items:
		row.append(item.string)
		href = item.get('href')
		if href != None:
			url = siteURL + href
			r = requests.get(url)
			data = r.text
			localSoup = BeautifulSoup(data, 'html.parser')
			sentence = localSoup.find("div", class_="posting-text")
			if sentence != None:
				numberOfJobs = sentence.string
				number = numberOfJobs.split(' ')[-1]
				row.append(number)				
			else:
				print("rude")
				row.append('0') #no matches found
		time.sleep(random.randrange(20,60))
with open('jobs.csv') as infile:
	lines = csv.reader(infile)
	for line in lines:
		word = line[0]
		if word != '':
			word = word.replace(' ', '+')
			jobs.append(word)

for job in jobs:
	for key in keys:
		search = job + "+" + key
		row = [search.replace('+', ' ')]
		url = baseURL % search
		r = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, 'html.parser')
		sentence = soup.find("div", class_="posting-text")		
		if sentence != None:
			numberOfJobs = sentence.string
			number = numberOfJobs.split(' ')[-1]
			row.append(number)
			getCompanies(soup)
			print("Finished %s!" % search)
		else:
			print("rude")
			row.append("No Matches Found") #no matches found
		rows.append(row)

with open('test.csv', 'w', encoding="utf-8", newline='') as infile:
	rowWriter = csv.writer(infile)
	for row in rows:
		rowWriter.writerow(row)