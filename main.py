import os
from service import app

HOST: str = os.environ.get("HOST", "0.0.0.0")
PORT: str = os.environ.get("PORT", "5000")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
