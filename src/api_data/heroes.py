from src.utils import constants as const
import requests


def api_request_heroes(headers):
    heroes_url = const.HEROES_URL

    response = requests.request("GET", heroes_url, headers=headers)
    heroes = response.json()

    return heroes


def heroes_filter(heroes):
    hero_id = heroes.get('id')
    hero_name = heroes.get('localized_name').replace("'", '')
    hero_attack_type = heroes.get('attack_type')
    hero_roles = str(heroes.get('roles')).replace('[', '').replace(']', '').replace("'", '')

    return hero_id, hero_name, hero_attack_type, hero_roles
