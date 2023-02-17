from src.utils import constants as const
from src.database.operations import db_connection, insert_hero_data
import requests


def api_request():
    heroes_url = const.HEROES_URL

    headers = {
        "api_key": f"{const.APY_KEY}",
    }

    response = requests.request("GET", heroes_url, headers=headers)
    heroes = response.json()

    return heroes


heroes = api_request()
cursor = db_connection()

def heroes_filter(heroes):
    for hero in heroes:
        hero_id = hero.get('id')
        hero_name = hero.get('localized_name').replace("'", '')
        hero_attack_type = hero.get('attack_type')
        hero_roles = str(hero.get('roles')).replace('[', '').replace(']', '').replace("'", '')

        insert_hero_data(cursor, hero_id, hero_name, hero_attack_type, hero_roles)

try:
    heroes_filter(heroes)
except Exception as e:
    print(e)