# Psycopg2 Basic on FastAPI

Package ทั้งหมดที่ต้องติดตั้ง
```sh
pip install fastapi
pip install uvicorn[standard]
pip install psycopg2
```
## สิ่งที่ควรรู้
- #### เป็นแค่การใช้งาน psycopg2 ใน FastAPI
- #### เหมาะสำหรับเรียนรู้พื้นฐาน
- #### อย่างไรก็ตาม Psycopg2 นั้นไม่ได้เหมาะสำหรับนำมาใช้ร่วมกับการทำ API เนื่องจากมีความเสี่ยงจะโดน SQL Injection
- #### แนะนำให้ไปใช้งาน SQLAlchemy แทน สามารถเรียนรู้เพิ่มเติมได้ที่ https://fastapi.tiangolo.com/tutorial/sql-databases/
-------------------------------------------------------------------------------------------------------------

All Package
```sh
pip install fastapi
pip install uvicorn[standard]
pip install psycopg2
```
## Notice
- #### this is just the implementation of psycopg2 in FastAPI
- #### Suitable for basic training
- #### However, Psycopg2 is not suitable for use with the API due to the risks associated with SQL Injection.
- #### Using SQLAlchemy is recommended, Learn more at: https://fastapi.tiangolo.com/tutorial/sql-databases/
