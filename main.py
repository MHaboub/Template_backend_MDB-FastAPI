from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from template import route

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=['*']
)


@app.get("/")
def read_Root():
    return {"haboub":"YA MAALEM"}

app.include_router(route.router)