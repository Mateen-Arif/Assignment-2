import requests
from bs4 import BeautifulSoup
l=[]
i=0
def find(link):
	w="Younis Khan"
	req=requests.get(link)
	soup=BeautifulSoup(req.content , 'lxml')
	if w in soup.text:
		print link
	else:
		return
	
	
def find_Read(s):
	req=requests.get(s)
	soup=BeautifulSoup(req.content , 'lxml')
	for link in soup.find_all("a"):
		if link.text=="Read More":
			s=link["href"]
			find(s)

def next_links(s):
	req=requests.get(s)
	soup=BeautifulSoup(req.content , 'lxml')
	for next in soup.find_all("li",{"class":"page-item"}):
		for n in next.find_all("a"):
			if n.text=="Next page":
				s=""
				s=n["href"]		
				
	return s


s="https://propakistani.pk/category/sports/"
i=1
while(i<5):
	find_Read(s)
	s=next_links(s)
	i+=1







