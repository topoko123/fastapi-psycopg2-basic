from typing import Dict
import psycopg2 as p2

class Database:
    def __init__(self):
        try:
            self.connection = p2.connect(
                host   =  'localhost',
                database = 'sample',
                user     = 'postgres',
                password = '<your-password>',
                port     = '5432'
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print('cannot connect to database')


    def create_table(self):
        create_table_command = """CREATE TABLE employee (
            id serial primary key,
            fullname varchar(50),
            age int
        )"""
        self.cursor.execute(create_table_command)
        self.connection.close()
        return 'create table success!!'

    def insert_data(self, data: Dict) :
        insert_query = '''INSERT INTO employee (
            fullname,
            age
        ) VALUES (
            %s,
            %s
        )'''
        self.cursor.execute(insert_query, (data.fullname, data.age))
        return 'insert success'

    def fetch_data(self, uid: int) :
        get_query = 'SELECT * FROM employee WHERE id=%s'
        self.cursor.execute(get_query, (uid, ))
        response_data = self.cursor.fetchall()
        return response_data

    def delete_data(self, uid: int):
        delete_query = 'DELETE FROM employee WHERE id=%s'
        self.cursor.execute(delete_query, (uid, ))
        return 'delete success'

    def update_data(self, uid: int ,new_age: int):
        update_query = 'UPDATE employee SET age=%s WHERE id=%s'
        new_data = (new_age, uid)
        self.cursor.execute(update_query, new_data)
        row_count = self.cursor.rowcount
        return f'Number of rows updated: {row_count}'
