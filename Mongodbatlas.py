def conectar_mongo():
    # Reemplaza <username>, <password>, y <cluster-url> con la información de tu clúster
    client = MongoClient("mongodb+srv://wpacheco:07vDM9IYENrJfwUa@clustermongo.oz271.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongo")
    db = client['sunat_db']
    collection = db['sunat_info']
    return collection
