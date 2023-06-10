import csv
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Dictionary list to store the extracted data
    data = []

    # Find div elements with the specified classes
    div_classes = [
        {"class": "css-18rodr0"}, # price
        {"class": "css-kjafn5"}, #all the contents
        {"class": "css-uwwqev"}, # image link
        {"class": "_6w1e54 _9scj1k _fycs5v _ks15vq _fr1tw0 _h3ftgi"}, #title of apartment
        ]
    for div_class in div_classes:
        div_elements = soup.find_all("div", div_class)
        if div_class == {"class": "_6w1e54 _9scj1k _fycs5v _ks15vq _fr1tw0 _h3ftgi"}:
            # Extract title from div elements
            titles = [div.get_text() for div in div_elements]
            data.append(("Title", titles))
        elif div_class == {"class": "css-18rodr0"}:
            # Extract price from div elements
            prices = [div.get_text() for div in div_elements]
            data.append(("Price", prices))
        elif div_class == ("h3",{"class": "css-197fqpq"}):
            # Extract bhk from div elements
            bhk = [div.get_text() for div in div_elements]
            data.append(("BHK", bhk))
        elif div_class == {"class": "css-kjafn5"}:
            # Extract othercontent from div elements
            othercontents = [div.get_text() for div in div_elements]
            data.append(("other_contents", othercontents))  
        elif div_class == {"class": "css-uwwqev"}:
            # Extract image links from div elements
            image_links = [div.get_text() for div in div_elements]
            data.append(("image_links", image_links))  

    # Save the extracted data to a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item[0]])
            writer.writerow(item[1])

    print("Scraping completed. Data saved in 'scraped_data.csv' file.")

# URL of the website to scrape
url = "https://housing.com/in/buy/searches/P6rjzh7de86crx689"
# Call the scraping function
scrape_website(url)
