from src.utils import constants as const
import requests

heroes_url = const.HEROES_URL

headers = {
    "api_key": f"{const.APY_KEY}",
}

response = requests.request("GET", heroes_url, headers=headers)
heroes = response.json()

for hero in heroes:
    hero_id = hero.get('id')
    hero_name = hero.get('localized_name')
    hero_attack_type = hero.get('attack_type')
    hero_roles = hero.get('roles')

    print(f'{hero_id} - {hero_name} - {hero_attack_type} - {hero_roles}')
