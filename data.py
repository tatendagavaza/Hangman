from requests import get
response = get('https://random-word-api.herokuapp.com//word?number=15')
response.raise_for_status()
word_data = response.json()
