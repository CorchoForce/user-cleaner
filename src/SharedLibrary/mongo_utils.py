import pymongo

def connect_to_mongo(base_uri, user, password, database, port, host):
    """ Connect to mongo using the Atlas uri
    Args:
        base_uri (str): uri to be filled with the user informations
        user (str): user login
        password (str): user password
        database (str): database to connect
        port (int): mongo cluster port
        host (str): mongo host name
    Returns:
        MongoClient: the client to be used in the database/collection access
    """
    try:
        connection_string = base_uri.format(
            MONGO_USERNAME=user, MONGO_PASSWORD=password, MONGO_DB=database, MONGO_HOSTNAME=host)
        return pymongo.MongoClient(connection_string, port)
    except:
        return None


def get_mongo_database(connection, database_name):
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


def get_mongo_collection(database, collection_name):
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


def delete_document_on_mongo(collection, query):
    """ Deletes multiple document to the collection
    Args:
        collection (Collection): collection object to insert the document
        query (dictionary): Query used to find the object and delete it in the collection
    Returns:
        bool: True if document was deleted correctly
    """
    print("[Debug] Deleting document on mongo")
    try:
        collection.delete_many(query)
        print("[Debug] Document deleted")
        return True
    except:
        print("[Warn] Couldn't delete the document")
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


    """ Access the mongo 
    Args:
        parameters (dictionary): dictionary object to with the env parameters
    Returns:
        tuple: the first element is a boolean (True if there's no error) and the second element is a collection object.
    """
    if (parameters is None):
        return (False, None)

    client = connect_to_mongo(parameters["connection_url"], parameters["username"],
                              parameters["password"], parameters["database"], parameters["port"])
    db = get_mongo_database(client, parameters["database"])
    collection = get_mongo_collection(db, parameters["collection"])

    return (collection is not None, collection)
