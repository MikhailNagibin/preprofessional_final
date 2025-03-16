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
