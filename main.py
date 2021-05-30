from database.conn import Database

from fastapi import FastAPI

from pydantic import BaseModel   #import BaseModel for receive request body: Json obj

import uvicorn

app = FastAPI()

new_database = Database()

class Infomation_Insert(BaseModel):    #Implement BaseModel Class
    fullname : str
    age      : int


new_database.create_table()   #call create table function in class Database

app.get('/fetch/{uid}')
async def fetch_data(uid: int):
    return new_database.fetch_data(uid)

app.post('/insert')
async def insert_data(data: Infomation_Insert):
    return new_database.insert_data(data)

app.patch('/update/{uid}')
async def update_data(uid: int, age: int):
    return new_database.update_data(uid, age)

app.delete('/delete/{uid}')
async def delete_data(uid: int):
    return new_database.delete_data(uid)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)


# this is just the implementation of psycopg2 in FastAPI.
# Suitable for basic training

### However, Psycopg2 is not suitable for use with the API due to the risks associated with SQL Injection.


# Using SQLAlchemy is recommended, Learn more at: https://fastapi.tiangolo.com/tutorial/sql-databases/


    


