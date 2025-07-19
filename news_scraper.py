
import requests
from bs4 import BeautifulSoup

# Target website (change URL as needed)
URL = "https://www.bbc.com/news"

# Set headers to simulate a real browser visit
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch the page content
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all h3 headline tags (BBC uses <h3> for headlines)
    headlines = soup.find_all('h3')

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines):
            if headline.text.strip() != "":
                file.write(f"{i+1}. {headline.text.strip()}\n")

    print("✅ Headlines saved to 'headlines.txt'")
else:
    print(f"❌ Failed to fetch page, status code: {response.status_code}")
