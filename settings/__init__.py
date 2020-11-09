import os
import dotenv

dotenv.load_dotenv()

HOST: str = os.environ.get("HOST", "0.0.0.0")
PORT: int = os.environ.get("PORT", 5000)

ARANGO_ENDPOINT: str = os.environ.get(
    "ARANGO_ENDPOINT", "http://127.0.0.1:8529")
ARANGO_PASSWORD: str = os.environ.get("ARANGO_PASSWORD", 'root')

DATABASE_NAME: str = os.environ.get("DATABASE_NAME", "cases")

COLLECTION_NAME: str = "cases_v1"
