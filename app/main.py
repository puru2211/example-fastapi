from fastapi import FastAPI,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import mysql.connector
from typing import Optional
import random
import mysql.connector

# Replace these values with your actual database connection details
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'fastapi',
    'raise_on_warnings': True
}

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")




app = FastAPI()

class Post(BaseModel):
    title: str
    content:str
    published:bool=True
    rating: Optional[int]=None

my_posts = [{"title":"new title1","content":"New content1","id":1},{"title":"new title2","content":"New content2","id":2},{"title":"new title3","content":"New content4","id":4}]

@app.get("/")
def root():
    return my_posts

@app.post("/posts")
def posts(new_post:Post):
    return "hello python programming"


