import os
import pyArango as arango

ARANGO_URL: str = os.environ.get("ARANGO_URL")

conn = arango.Connection(arangoURL=ARANGO_URL)
