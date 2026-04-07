import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  


queue = ["https://quotes.toscrape.com/"]  
visited = set()
target_word = "einstein" 

while queue:
    url = queue.pop(0)  
    if url in visited or not url.startswith("http"):
        continue
    
    try:
        print(f"Crawling: {url}")
        html = requests.get(url, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        visited.add(url)

        
        if target_word.lower() in soup.get_text().lower():
            print(f" The word '{target_word}' was found here!")

       
        for a in soup.find_all("a", href=True):
            raw_link = a["href"]
            
            
            full_link = urljoin(url, raw_link) 
            
            if full_link not in visited:
                queue.append(full_link)
                
    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

    if len(visited) > 10: 
        break



pip install requests beautifulsoup4
