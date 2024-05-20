
# import os
# import sqlalchemy
# from yaml import load, Loader
# from flask import Flask


# app = Flask(__name__)
# def init_connect():
#     # if os.environ.get('GAE_ENV') != 'standard':
#     #     variables = load(open("app.yaml"), Loader=Loader)
#     #     env_variables = variables['env_variables']
#     #     for var in env_variables:
#     #         os.environ [var] = env_variables[var]

#     pool = sqlalchemy.create_engine(
#         sqlalchemy.engine.url.URL(
#         drivername="mysql+pymysql",
#         username='root',
#         password='password', database='projectdb',
#         host='35.184.94.222',
#         port=0,
#         query={"charset": "utf8"}
#         ))
#     return pool
    
# db = init_connect()
# conn = db.connect()
# result = conn.execute("show databases;").fetchall()
# # print([x for x in result])
# print(str(conn))
# print("hello")