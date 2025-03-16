import json
import psycopg2
import requests

def get_db_connection() -> psycopg2.extensions.connection:
    with open("config.json") as f:
        conf = json.load(f)
    DATABASE = conf["DATABASE"]
    USER = conf["USER"]
    PASSWORD = conf["PASSWORD"]
    HOST = conf["HOST"]
    PORT = conf["PORT"]
    conn = psycopg2.connect(
        dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT
    )
    return conn


def get_all_tails(adres: str) -> set:
    tails = set()
    while len(tails) != 16:
        tails.add(tuple(map(tuple, requests.get(adres).json()['message']['data'])))
    return tails


def get_coords(adres: str) -> dict:
    return requests.get(f'{adres}/coords').json()


def insert_adres(conn: psycopg2.extensions.connection, adres: str):
    cur = conn.cursor()
    cur.execute("insert into tests(adres) values %s", (adres, ))
    conn.commit()


def get_adres_id(cur: psycopg2.extensions.cursor, adres: str):
    cur.execute("select id from tests where adres = %s", (adres, ))
    return cur.fetchall()


def insert_coords(conn: psycopg2.extensions.connection, test_id, data: dict):
    cur = conn.cursor()
    cur.execute("insert into coords values %s",
                (test_id, *data['listener'], *data['sender'], *data['price']))
    conn.commit()

