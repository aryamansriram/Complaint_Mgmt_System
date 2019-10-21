from flask import *
from pymongo import MongoClient
import pprint
client = MongoClient()
db = client.javatpoint
employee = {"id": "101",  
"name": "Peter",  
"profession": "Software Engineer",  
}  
employees = db.employees
employees.insert_one(employee)
pprint.pprint(employees.find_one())  