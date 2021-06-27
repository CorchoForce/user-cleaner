import pymongo
from datetime import datetime


def connect_to_mongo(user: str, password: str, database: str, port: int, host: str) -> pymongo.MongoClient:
    """ Connect to mongo using the Atlas uri
    Args:
        user (str): user login
        password (str): user password
        database (str): database to connect
        port (int): mongo cluster port
        host (str): mongo host name
    Returns:
        MongoClient: the client to be used in the database/collection access
    """
    base_uri = "mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}/{MONGO_DB}"
    try:
        connection_string = base_uri.format(
            MONGO_USERNAME=user, MONGO_PASSWORD=password, MONGO_HOSTNAME=host, MONGO_DB=database)
        return pymongo.MongoClient(connection_string, port)
    except:
        return None


def get_mongo_database(connection: pymongo.MongoClient, database_name: str) -> pymongo.database.Database:
    """ Access the database
    Args:
        connection (MongoClient): Mongo connection to the database
        database_name (str): database to be accessed
    Returns:
        Database: the Database object
    """
    try:
        return connection.get_database(database_name)
    except:
        return None


def get_mongo_collection(database: pymongo.database.Database, collection_name: str) -> pymongo.collection.Collection:
    """ Access the collection
    Args:
        database (Database): Database that contains the collection_name
        collection_name (str): collection to be accessed
    Returns:
        Collection: the Collection object
    """
    try:
        return database.get_collection(collection_name)
    except:
        return None


def delete_document_on_mongo(collection: pymongo.collection.Collection, query: dict) -> bool:
    """ Deletes one document to the collection
    Args:
        collection (pymongo.collection.Collection): collection object to insert the document
        query (dictionary): Query used to find the object and delete it in the collection
    Returns:
        bool: True if document was deleted correctly
    """
    print("[Debug] Deleting document on mongo")
    try:
        collection.delete_one(query)
        print("[Debug] User deleted")
        return True
    except:
        print("[Warn] Couldn't delete the user")
        return False


def get_all_invalid_users(collection: pymongo.collection.Collection) -> list:
    """ Gets a list of existing ThesisId on Mongo
    Args:
        collection (pymongo.collection.Collection): collection object to get the invalid users
    Returns:
        list: the list of ThesisId
    """
    try:
        return list(collection.find({"verified": False}))
    except:
        return None


def delete_invalid_users(collection: pymongo.collection.Collection) -> None:
    """ Delete all the users that the created time is bigger than 7 days and are not valid
    Args:
        collection (Collection): collection object to delete the invalid users
    """
    users = get_all_invalid_users(collection)
    for user in users:
        created_date = user.get(
            "createdAt", datetime.strptime('2021/01/01', '%Y/%m/%d'))
        if ((datetime.now() - created_date).days >= 7):
            delete_document_on_mongo(collection, {"_id": user["_id"]})


def access_collection(parameters: dict) -> tuple:
    """ Access the mongo 
    Args:
        parameters (dict): dictionary object to with the env parameters
    Returns:
        tuple: the first element is a boolean (True if there's no error) and the second element is a collection object.
    """
    if (parameters is None):
        return (False, None)

    client = connect_to_mongo(
        parameters["username"], parameters["password"],
        parameters["database"], parameters["port"],
        parameters["host"]
    )
    db = get_mongo_database(client, parameters["database"])
    collection = get_mongo_collection(db, parameters["collection"])

    return (collection is None, collection)
