from fastapi import FastAPI
from dotenv import load_dotenv

from .routes_config import routes_config

## ENV
load_dotenv()

## FASTAPI INIT
app = FastAPI()

## REGISTER ROUTES
routes_config(app)
