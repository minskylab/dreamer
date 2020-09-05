
from service import app
from settings import HOST, PORT
import uvicorn

if __name__ == "__main__":
    # app.run(host=HOST, port=PORT, debug=False)
    uvicorn.run(app, host=HOST, port=PORT)
