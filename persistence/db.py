import arango
from arango.database import StandardCollection, StandardDatabase
from loguru import logger
from settings import ARANGO_ENDPOINT, DATABASE_NAME, COLLECTION_NAME, ARANGO_PASSWORD


logger.info(
    f"connecting to {ARANGO_ENDPOINT}, db: {DATABASE_NAME}, coll: {COLLECTION_NAME}")
client = arango.ArangoClient(hosts=ARANGO_ENDPOINT)

_sys_db: StandardDatabase = client.db(password=ARANGO_PASSWORD)
if not _sys_db.has_database(DATABASE_NAME):
    _sys_db.create_database(DATABASE_NAME)

db = client.db(DATABASE_NAME, password=ARANGO_PASSWORD)

if db.has_collection(COLLECTION_NAME):
    dreams_collection: StandardCollection = db.collection(COLLECTION_NAME)
else:
    dreams_collection: StandardCollection = db.create_collection(
        COLLECTION_NAME)

dreams_collection.add_hash_index(fields=["id"], unique=False)

logger.info("dreams collection ready")
