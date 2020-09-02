import arango
from arango.database import StandardCollection, StandardDatabase
from settings import ARANGO_URL, DATABASE_NAME, COLLECTION_NAME

client = arango.ArangoClient(hosts=ARANGO_URL, host_resolver="rocksdb")

_sys_db: StandardDatabase = client.db()
if not _sys_db.has_database(DATABASE_NAME):
    _sys_db.create_database(DATABASE_NAME)

db = client.db(DATABASE_NAME)

if db.has_collection(COLLECTION_NAME):
    dreams_collection: StandardCollection = db.collection(COLLECTION_NAME)
else:
    dreams_collection: StandardCollection = db.create_collection(
        COLLECTION_NAME)

dreams_collection.add_hash_index(fields=["id"], unique=False)
