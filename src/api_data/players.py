import requests


def api_request_player(account_id, headers):
    players_url = f"https://api.opendota.com/api/players/{account_id}"

    response_player = requests.request("GET", players_url, headers=headers)
    player = response_player.json()

    return player


def player_filter(player):
    player_account_id = player['profile']['account_id']
    player_name = player['profile']['personaname']

    return str(player_account_id), str(player_name)


def api_request_player_heroes(account_id, headers):
    player_hero_url = f"https://api.opendota.com/api/players/{account_id}/heroes"

    response_player_heroes = requests.request("GET", player_hero_url, headers=headers)
    player_heroes = response_player_heroes.json()

    return player_heroes


def player_hero_filter(player_hero):
    hero_id = player_hero.get('hero_id')
    games = player_hero.get('games')
    win = player_hero.get('win')

    return hero_id, games, win


