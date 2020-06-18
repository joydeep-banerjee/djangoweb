import requests

class Dictionary:

  def __init__(self, word):
    self.word = word

  def display(self):
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ self.word +"?key=38597f83-8fdf-4da0-ba26-04484fa3e0d3"
    response = requests.get(url).json()

    print("Short defination: --")

    for res in response:
      print(", ".join(res["shortdef"]))

string = raw_input("Enter word :")
# print(string)
d = Dictionary(string)
d.display()
#https://dictionaryapi.com/products/json#sec-2.syns