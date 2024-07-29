from django.apps import AppConfig
from api.utils.mongo_connect import MongoConnection
from decouple import config
from api.utils.embedding_generator import EmbeddingGenerator
from api.utils.faiss_search import FaissSearch 


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    global mongo_client
    global embedding_generator
    global faiss_search


    mongo_client = MongoConnection(config('MONGODB_CONNECTION_STRING'),
                               config('MONGODB_DATABASE'),
                               config('MONGODB_COLLECTION'))
    print("Created MongoClient")
    embeddding_generator = EmbeddingGenerator()
    print("Created EmbeddingGenerator")
    faiss_search = FaissSearch(embeddding_generator,config('EMBEDDINGS_PATH'),config('INDEX_PATH'))
    print("Created FaissSearch")