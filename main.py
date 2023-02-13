from utils import constants as const
import requests

heroes_url = const.HEROES_URL

headers = {
	"api_key": f"{const.APY_KEY}",
}

response = requests.request("GET", heroes_url, headers=headers)
content = response.json()


hero_id = content[0]['id']
hero_name = content[0]['localized_name']
hero_attack_type = content[0]['attack_type']
hero_roles = content[0]['roles']

print(f'{hero_id} - {hero_name} - {hero_attack_type} - {hero_roles}')
