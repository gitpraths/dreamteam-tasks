import requests
from bs4 import BeautifulSoup

def verify_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

     
        links = soup.find_all("a", href=True)
        for link in links:
            link_url = link['href']
            if not link_url.startswith("http"):
                continue  
            try:
                link_response = requests.get(link_url)
                if link_response.status_code != 200:
                    print(f"Broken link: {link_url} (Status code: {link_response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Error checking link {link_url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to load page {url}: {e}")

if __name__ == "__main__":
    webpage_url = input("Enter the URL of the webpage to verify links: ").strip()
    verify_links(webpage_url)