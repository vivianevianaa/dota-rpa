from src.api_data import heroes
from src.api_data import players
from src.database import operations as db
from src.utils import constants as const

headers = const.HEADERS
cursor = db.db_connection()

account_id = input("Enter with the account id: ")


def persisting_heroes():
    try:
        # Retrieving and persisting from Heroes endpoint
        heroes_endpoint = heroes.api_request_heroes(headers)
        for hero in heroes_endpoint:
            hero_id, hero_name, hero_attack_type, hero_roles = heroes.heroes_filter(hero)
            db.insert_hero_data(cursor, hero_id, hero_name, hero_attack_type, hero_roles)

        cursor.commit()
    except Exception as e:
        print(e)


def persisting_player():
    try:
        # Retrieving and persisting data from Players endpoints
        players_endpoint = players.api_request_player(account_id, headers)
        players_heroes_endpoint = players.api_request_player_heroes(account_id, headers)
        player_account_id, player_name = players.player_filter(players_endpoint)

        for player_hero in players_heroes_endpoint:
            if player_hero.get('games') > 0:
                player_hero_id, player_hero_games, player_hero_win = players.player_hero_filter(player_hero)
                db.insert_player_data(cursor, player_account_id, player_name, player_hero_id, player_hero_games, player_hero_win)
                cursor.commit()
    except Exception as e2:
        print(e2)

persisting_heroes()
persisting_player()