from src.utils import constants as const
from src.database.operations import db_connection, insert_player_data
import requests


headers = {
    "api_key": f"{const.APY_KEY}"
}

account_id = input("Enter with the account id: ")

players_url = f"https://api.opendota.com/api/players/{account_id}"

response_player = requests.request("GET", players_url, headers=headers)
player = response_player.json()

cursor = db_connection()

player_account_id = player['profile']['account_id']
player_personaname = player['profile']['personaname']

print(f'{player_account_id} - {player_personaname}')

########################## HEROES ##########################

player_hero_url = f"https://api.opendota.com/api/players/{account_id}/heroes"

response_player_heroes = requests.request("GET", player_hero_url, headers=headers)
player_heroes = response_player_heroes.json()

for hero in player_heroes:
    if hero.get('games') > 0:
        hero_id = hero.get('hero_id')
        games = hero.get('games')
        win = hero.get('win')



        print(f'Hero_id: {hero_id} - Games: {games} - Wins: {win}')



