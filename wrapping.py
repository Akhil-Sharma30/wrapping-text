
from bs4 import BeautifulSoup
import requests as req


url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
input1 = req.get(url)
#print(input1.text)



soup = BeautifulSoup(input1.text,'lxml')
x = soup.find_all("table", class_="wikitable sortable")
#print(len(x))
our_table = x[1]



print(type(our_table))
rows = our_table.findAll("tr")
headers = rows[0]
#print(headers)
data_rows = rows[1:20]



def tr_to_list(data, head=False):
    tag = "th" if head else "td"
    data_points = data.findAll(tag)[0:6]

    return list(map(lambda x: x.getText(), data_points))



headers_list = tr_to_list(headers, head=True)
data = []
for row in data_rows:
    data.append(tr_to_list(row))
    
special_char = '*\n,"""'
out_list1 = [''.join(filter(lambda i: i not in special_char, string)) for string in headers_list]
# = [''.join(filter(lambda j: j not in special_char, string)) for string in data]

data= [out_list1] + data
#Write CSV
import csv

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
