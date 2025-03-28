# import os
# import tempfile
# from functools import reduce

# from tinydb import TinyDB, Query

# db_dir_path = tempfile.gettempdir()
# db_file_path = os.path.join(db_dir_path, "students.json")
# student_db = TinyDB(db_file_path)


# def add(student=None):
#     queries = []
#     query = Query()
#     queries.append(query.first_name == student.first_name)
#     queries.append(query.last_name == student.last_name)
#     query = reduce(lambda a, b: a & b, queries)
#     res = student_db.search(query)
#     if res:
#         return 'already exists', 409

#     doc_id = student_db.insert(student.to_dict())
#     student.student_id = doc_id
#     return student.student_id


# def get(student_id=None, subject=None):
#     student = student_db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student['student_id'] = student_id
#     print(student)
#     return student


# def delete(student_id=None):
#     student = student_db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student_db.remove(doc_ids=[int(student_id)])
#     return student_id

import os
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId

# Configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:UxQQYfaaSvjaiPQhTthwsNsijnQgQvtg@junction.proxy.rlwy.net:40820')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'test')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'students')

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def add(student=None):
    try:
        result = collection.insert_one(student.to_dict())
        student.student_id = str(result.inserted_id)
        return student.student_id
    except DuplicateKeyError:
        return 'already exists', 409

def get(student_id=None):
    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if not student:
            return 'not found', 404
        student['student_id'] = str(student['_id'])
        student.pop('_id')
        return student
    except Exception:
        return 'invalid id', 400

def delete(student_id=None):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id
