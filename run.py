import uvicorn
from main import app

host="0.0.0.0"
port=8888
reload=True
if __name__ == "__main__":
    uvicorn.run("__main__:app", host=host, port=port, reload=reload)