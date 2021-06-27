from os import getenv


def load_parameters() -> dict:
    """ Loads all .env parameters.
    Returns:
        dict: an object with the .env informations.
    """
    try:
        return {"username": getenv("MONGO_USERNAME"),
                "password": getenv("MONGO_PASSWORD"),
                "database": getenv("MONGO_DATABASE"),
                "collection": getenv("MONGO_COLLECTION"),
                "port": int(getenv("MONGO_PORT")),
                "host": getenv("MONGO_HOSTNAME")}
    except:
        return None
