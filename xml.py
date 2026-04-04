import csv
import requests
import xml.etree.ElementTree as ET

def load_rss(url, filename):
    resp = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(resp.content)
    print(f"RSS feed loaded and saved to '{filename}'")

def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []

    # Note: Tags like pubDate are usually case-sensitive in XML
    allowed_fields = {'guid', 'title', 'pubDate', 'description', 'link'}

    for item in root.findall('.//item'):
        news = {}
        for child in item:
            tag = child.tag.split('}')[-1]
            if tag in allowed_fields:
                news[tag] = child.text
                
            # Handling media content if available
            if tag == 'content' and 'url' in child.attrib:
                news['media'] = child.attrib['url']

        if news:
            newsitems.append(news)

    return newsitems

def save_to_csv(newsitems, filename):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)
    print(f"Data Saved to '{filename}'.")

def main():
    # Example RSS feeds
    rss_url = "https://feeds.feedburner.com/50WordStories"
    # rss_url="https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    # rss_url="http://feeds.bbci.co.uk/news/rss.xml"
    
    xml_filename = 'topnewsfeed.xml'
    csv_filename = 'topnews.csv'  # Fixed the accidental 'x' here

    try:
        load_rss(rss_url, xml_filename)
        newsitems = parse_xml(xml_filename)

        if newsitems:
            save_to_csv(newsitems, csv_filename)
        else:
            print("No items found in the RSS feed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()




pip install requests
