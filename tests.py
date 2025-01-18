import requests

url = "https://createuserapi.p.rapidapi.com/oneuser/62eb582a65b6ede1753bc96a"

headers = {
	"x-rapidapi-key": "4a095f021dmsh2a63e4192e5da2fp1ceabajsna0ab8168b202",
	"x-rapidapi-host": "createuserapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

