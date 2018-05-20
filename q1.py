import os
import requests
from bs4 import BeautifulSoup
def qari_links(url):
	req =requests.get(url)
	soup = BeautifulSoup(req.content,'lxml')
	links=[]
	for link in soup.find_all("a"):
		links.append(link["href"])
	return links
def mp3_links(qari):
	req =requests.get("https://download.quranicaudio.com/quran/%s" % qari)
	soup = BeautifulSoup(req.content,'lxml')
	links=[]
	for l in soup.find_all("a"):
		links.append(l.get("href"))
	download_mp3(qari,links)
def download_mp3(qari,links):	

	os.makedirs(qari)
	os.chdir(qari)
	i=-26
	while i<0:
		mp3_req=requests.get("https://download.quranicaudio.com/quran/%s/%s" % (qari,links[i]),stream =True)	
		with open(links[i],"wb") as f:
			f.write(mp3_req.content)
		i+=1
	os.system("mp3wrap second_Half.mp3 *.mp3")
	os.system("rm [!second]*.mp3")
	os.chdir("../")	
url="https://download.quranicaudio.com/quran/"
links=qari_links(url)
i=1
while(i<len(links)-1):
	mp3_links(links[i])
	i+=1
