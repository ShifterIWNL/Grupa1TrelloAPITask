from fastapi import FastAPI
import Routers

app = FastAPI()


app.include_router(Routers.router, prefix="/trello", tags=["trello"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
