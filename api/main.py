import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .routes_config import routes_config

## ENV
load_dotenv()

## FASTAPI INIT
app = FastAPI()

## REGISTER ROUTES
routes_config(app)
