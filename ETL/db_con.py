#!/usr/bin/python3

from sqlalchemy import create_engine

def db_connection():
  return create_engine("postgresql+psycopg2://postgres:admin@localhost/blockchain_dai_transactions")
