import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = "https://www.amazon.com/s?k=laptops"

# Send a GET request to the webpage
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all product containers on the page
    product_containers = soup.find_all('div', class_='s-result-item')

    # Create a list to store the product information
    products = []

    # Loop through each product container
    for container in product_containers:
        # Find the product name
        product_name = container.find('span', class_='a-size-medium a-color-base a-text-normal').text

        # Find the product price
        product_price = container.find('span', class_='a-price-whole').text

        # Find the product rating
        product_rating = container.find('span', class_='a-icon-alt').text

        # Create a dictionary to store the product information
        product_info = {
            'Product Name': product_name,
            'Product Price': product_price,
            'Product Rating': product_rating
        }

        # Add the product information to the list
        products.append(product_info)

    # Create a CSV file and write the product information to it
    with open('product_info.csv', 'w', newline='') as csvfile:
        fieldnames = ['Product Name', 'Product Price', 'Product Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)

    print("Product information has been successfully scraped and stored in product_info.csv")

else:
    print("Failed to retrieve the webpage")