from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soap = BeautifulSoup(r.text, "html.parser")
results = soap.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        #print("Summary:", item.find("a").parent.parent.find("p").text)

        #children = item.children
        #for child in children:
         #   print("Child: ", child)

        children = item.find("h2")
        print("Next sibling of the hw is:", children.next_sibling)