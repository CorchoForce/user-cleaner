from os import getenv
from dotenv import load_dotenv, find_dotenv


def load_parameters() -> dict:
    """ Loads all .env parameters.
    Returns:
        dict: an object with the .env informations.
    """
    try:
        return {"connection_url": getenv("CONNECTION_URL"),
                "username": getenv("USERNAME"),
                "password": getenv("PASSWORD"),
                "database": getenv("DATABASE"),
                "collection": getenv("COLLECTION"),
                "port": int(getenv("PORT"))}
    except:
        return None
