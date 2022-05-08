from app import db
from os import system
system("rm apsara.db")
db.create_all()
