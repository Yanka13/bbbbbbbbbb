import requests


def quote():
    url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
    call = requests.get(url).json()[0]
    return f"{call['author']} says : {call['quote']}"
