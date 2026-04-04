from html.parser import HTMLParser
from urllib.request import urlopen, Request
from urllib import parse
import json

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Look for anchor tags
        if tag == "a":
            for (key, value) in attrs:
                if key == "href":
                    # Combine relative URLs with base URL
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links.append(newUrl)

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        
        # Create a request with a User-Agent to avoid 403 Forbidden errors
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        try:
            response = urlopen(req)
            # Check if the content is HTML
            if "text/html" in response.getheader("Content-Type"):
                htmlBytes = response.read()
                htmlString = htmlBytes.decode("utf-8")
                self.feed(htmlString)
                return htmlString, self.links
            else:
                return "", []
        except Exception as e:
            # Silently handle errors (like 404s) so the crawler keeps going
            return "", []

def crawl(url, word):
    visitedUrl = []
    foundUrl = []
    numberVisited = 0
    foundWord = False
    
    parser = LinkParser()
    
    # scan the starting URL
    print(f"Scanning start URL: {url}")
    data, links = parser.getLinks(url)
    
    # Add the starting URL to the list to check
    if url not in links:
        links.append(url)

    # Loop through links found
    for link in links:
        # Limit the crawl to avoid infinite loops for this example
        if numberVisited > 20:
            break
            
        if link not in visitedUrl:
            visitedUrl.append(link)
            numberVisited += 1
            
            try:
                print(f"{numberVisited} Scanning: {link}")
                
                # Fetch content of the specific link
                page_content, _ = parser.getLinks(link)
                
                # Check if the word is in this specific page's content
                if word.lower() in page_content.lower():
                    foundWord = True
                    foundUrl.append(link)
                    print(f"\nSUCCESS! The word '{word}' was found at {link}\n")
                else:
                    print("Matches Not Found")
                    
            except Exception as e:
                print(f"Failed to read {link}")

    print("-" * 20)
    if not foundWord:
        print(f"The word '{word}' was not found in the scanned pages.")
    
    print(f"Finished. Crawled {numberVisited} pages.")
    print("Found URLs JSON:")
    # Use standard json.dumps instead of a custom function
    print(json.dumps(foundUrl, indent=4))

# --- Execution ---
# Note: Wikipedia is a good, safe site to test crawlers on.
crawl("https://www.wikipedia.org/", "Login")
