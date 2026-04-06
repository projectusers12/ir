import csv
import requests
import xml.etree.ElementTree as ET


url = ""
resp = requests.get(url)
with open('topnewsfeed.xml', 'wb') as f:
    f.write(resp.content)
print("RSS feed loaded and saved to XML.")


root = ET.parse('topnewsfeed.xml').getroot()
allowed_fields = {'guid', 'title', 'pubDate', 'description', 'link'}
newsitems = []

for item in root.findall('.//item'):
    news = {}
    for child in item:
        tag = child.tag.split('}')[-1] # Clean the tag name
        
        if tag in allowed_fields:
            news[tag] = child.text
        if tag == 'content' and 'url' in child.attrib:
            news['media'] = child.attrib['url']
            
    if news:
        newsitems.append(news)


if newsitems:
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
    with open('topn.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)
    print("Data successfully saved to 'topnews.csv'.")
else:
    print("No items found in the RSS feed.")



pip install requests
