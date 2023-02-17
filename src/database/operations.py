import pyodbc


def db_connection():
    server = r'LAPTOP-MSQ1G76J\SQLEXPRESS'
    database = 'db_dota_rpa'

    driver_name = ''
    driver_names = [driver for driver in pyodbc.drivers() if driver.endswith(' for SQL Server')]
    if driver_names:
        driver_name = driver_names[0]
    if driver_name:
        conn_str = f'DRIVER={driver_name};'
        connection = pyodbc.connect(conn_str + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
    else:
        print('Cannot connect.')

    return connection.cursor()


cursor = db_connection()


def insert_hero_data(cursor, hero_id, hero_name, hero_attack_type, hero_roles):
    cursor.execute(
        f'''
        INSERT INTO Heroes 
            (HeroID, HeroName, HeroAttackType, HeroRoles)
        VALUES
            ({hero_id}, '{hero_name}', '{hero_attack_type}', '{hero_roles}');
        ''')
    cursor.commit()

######################## PLAYERS ########################


def insert_player_data(cursor, player_account_id, player_personaname, hero_id, hero_games, hero_wins):
    hero_name = f'SELECT HeroName FROM Heroes WHERE HeroID = {hero_id};'
    cursor.execute(
        f'''
        INSERT INTO Players 
            (PlayerAccountID, PlayerName, FK_HeroID, HeroName, HeroGames, HeroWins) 
        VALUES 
            ({player_account_id}, {player_personaname}, {hero_id}, '{hero_name}', '{hero_games}', '{hero_wins}');
        ''')