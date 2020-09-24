from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

# tested on newegg as an example
url = ''

# opening up connection, grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

# create a csv
filename = "products.csv"
f = open(filename, "w")

headers = "brand, price, shipping\n"

f.write(headers)

# loop pages
i = 0

while True:
    i += 1

    url_i = url + "&page=" + str(i)
    uClient = uReq(url_i)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div",{"class":"item-container"})

    for container in containers:

        brand = container.div.div.a.img["title"]

        title_container = container.findAll("a", {"class":"item-title"})
        product_name = title_container[0].text

        shipping_container = container.findAll("li", {"class":"price-ship"})
        shipping = shipping_container[0].text.strip()

        price_container = container.findAll("li", {"class":"price-current"})
        price = price_container[0].text[:7]

        print("brand:" + brand)
        # print("product_name:" + product_name)  // product_name.replace(",", "|")
        print("shipping:" + shipping)

        f.write(brand + "," + price + "," + shipping + "\n")

    page_soup = soup(page_html, "html.parser")

f.close()