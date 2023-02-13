from utils import constants as const
import requests

url = const.BASE_URL


headers = {
	"api_key": f"{const.APY_KEY}",
	"players": "214372155"
}

response = requests.request("GET", url, headers=headers)

print(response.text)