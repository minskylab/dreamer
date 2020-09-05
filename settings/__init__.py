import os
import dotenv

dotenv.load_dotenv()

HOST: str = os.environ.get("HOST", "0.0.0.0")
PORT: int = os.environ.get("PORT", 5000)

ARANGO_URL: str = os.environ.get("ARANGO_URL", "http://127.0.0.1:8529")
DATABASE_NAME: str = os.environ.get("DATABASE_NAME", "dreams")
PASSWORD: str = os.environ.get("PASSWORD", 'root')

COLLECTION_NAME: str = "dreams_v1"
