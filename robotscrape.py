import requests

def scrape_robots_txt(url):
    # Append "/robots.txt" to the given URL
    if not url.startswith("http"):
        url = "http://" + url
    if not url.endswith("/"):
        url += "/"
    robots_url = url + "robots.txt"
    
    try:
        # Send a GET request to retrieve the robots.txt file
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def main():
    # List of URLs to scrape
    urls = [
        "example.com",
        "google.com",
        "yahoo.com"
        # Add more URLs here
    ]

    for url in urls:
        robots_txt = scrape_robots_txt(url)
        if robots_txt:
            print(f"Robots.txt for {url}:\n{robots_txt}\n")
        else:
            print(f"No robots.txt found for {url}\n")

if __name__ == "__main__":
    main()
