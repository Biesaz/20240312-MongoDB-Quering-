# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import List


# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database


# def get_database_collection(database: Database, collection_name: str) -> Collection:
#     collection = database[collection_name]
#     return collection


# if __name__ == "__main__":
#     mongodb_host = "localhost"
#     mongodb_port = 27017
#     database_name = "workers"
#     collection_name = "employees_salary"

#     client = MongoClient(mongodb_host, mongodb_port)
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     collection = get_database_collection(db, collection_name)

#     # print(collection.find({},{}))

#     query = {"age":{"$gt": 40, "$lt": 55}, "name": "Robert"}

#     response = (collection.find(query,{"_id": 0, "salary": 1}))
#     for documents in response:
#         print(documents)

##############################################################################################################################################

# Create a python script that would generate a sequence of 1000 random numbers from 1 to 1000000. 
# A number sequence from 0 to 9 represents letters from A to J.
# (lets say we have 101 = BAB) . All those 1000 values should be written to database (number and it's representation) 
# Please find: 
# - All documents where number is 100,1000,10000
# - All documents where numbers are at least triple or four digits
# - What is the dominant letter within  five and 6 digits area range. 
# - Tell me the sum on numbers where majority letters are : (letter 1, letter 2, letter 3)
# - Show me the lowest and highest number and their representations

# from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import List
# import random

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def get_database_collection(database: Database, collection_name: str) -> Collection:
#     collection = database[collection_name]
#     return collection

# def number_to_letters(number):
#     letters = "ABCDEFGHIJ"
#     number_str = str(number)
#     result = ""
#     for digit in number_str:
#         result += letters[int(digit)]
#     return result

# if __name__ == "__main__":
#     mongodb_host = "localhost"
#     mongodb_port = 27017
#     database_name = "numbers"
#     collection_name = "representation"
#     client = MongoClient(mongodb_host, mongodb_port)
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)
#     collection = get_database_collection(db, collection_name)

#     random_numbers = [random.randint(1, 1000000) for _ in range(1000)]
#     for number in random_numbers:
#         representation = number_to_letters(number)
#         collection.insert_one({"number": number, "representation": representation})

# response1 = collection.find({"number": {'$in': [100, 1000, 10000]}})
# print("Query 1 Results:")
# for document in response1:
#     print(document)

# # response2 = collection.find({'number': {'$gte': 1000}})
# # print("Query 2 Results:")
# # for document in response2:
# #     print(document)
    
# # Query 1: Find all documents where number is 100, 1000, or 10000
# query_1 = collection.find({"number": {"$in": [100, 1000, 10000]}})
# print("Query 1 Results:")
# for document in query_1:
#     print(document)

# # Query 2: Find all documents where numbers are at least triple or four digits
# query_2 = collection.find({"number": {"$gte": 1000}})
# print("\nQuery 2 Results:")
# for document in query_2:
#     print(document)

# # Query 3: Find the dominant letter within the five and six digits area range
# query_3_result = collection.aggregate([
#     {"$match": {"number": {"$gte": 10000, "$lt": 1000000}}},
#     {"$group": {"_id": {"$substr": ["$representation", 0, 1]}, "count": {"$sum": 1}}},
#     {"$sort": {"count": -1}},
#     {"$limit": 1}
# ])
# print("\nQuery 3 Results:")
# for result in query_3_result:
#     print(f"Dominant Letter: {result['_id']}")

# # Query 4: Calculate the sum of numbers where majority letters are (letter 1, letter 2, letter 3)
# query_4_result = collection.aggregate([
#     {"$group": {"_id": {"$substr": ["$representation", 0, 1]}, "total": {"$sum": "$number"}}},
#     {"$sort": {"total": -1}},
#     {"$limit": 3}
# ])
# query_4_letters = [result["_id"] for result in query_4_result]
# query_4_sum = collection.aggregate([
#     {"$match": {"representation": {"$regex": f"^[{''.join(query_4_letters)}]"}}},
#      {"$group": {"_id": None, "total_sum": {"$sum": "$number"}}}
# ])
# print("\nQuery 4 Results:")
# for result in query_4_sum:
#     print(f"Sum of numbers where majority letters are {query_4_letters}: {result['total_sum']}")

# # Query 5: Find the lowest and highest number and their representations
# lowest_number = collection.find_one({}, sort=[("number", 1)])
# highest_number = collection.find_one({}, sort=[("number", -1)])
# print("\nLowest Number:")
# print(lowest_number)
# print("\nHighest Number:")
# print(highest_number)

############################### Alberto ############################
# Create a python script that would generate a sequence of 1000 random numbers from 1 to 1000000 . A number sequence from 0 to 9 represents letters from A to J.
# (lets say we have 101 = BAB) . All those 1000 values should be written to database (number and it's representation)
# Please find:
# - All documents where number is 100,1000,10000
# - All documents where numbers are at least triple or four digits
# - What is the dominant letter within  five and 6 digits area range.
# - Tell me the sum on numbers where majority letters are : (letter 1, letter 2, letter 3)
# - Show me the lowest and highest number and their representations

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
import random


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def create_document(alphabet) -> Dict:
    number = random.randint(1, 1000000)
    num_str = str(number)
    letters = "".join(alphabet[int(x)] for x in num_str)

    return {"number": number, "letters": letters}


# print(create_document(alphabet))

if __name__ == "__main__":
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "mongo2_task1"
    collection_name = "numbers_letters"

    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    collection = db[collection_name]

    ##### CREATE DATABASE #####
    # for _ in range(1000):
    #     document = create_document(alphabet)
    #     inserted_id = insert_document(collection, document)
    #     print(f"Pair added: {document['number']} {document['letters']}")

    ##### QUERIES #####

    # 1.- All documents where number is 100,1000,10000

    # query = {"number": {"$in": [533409, 150042, 977361]}}
    # response = collection.find(query, {"_id": 0})
    # for i in response:
    #     print(i)

    # 2.- All documents where numbers are at least triple or four digits

    # query = {"number": {"$gt": 99, "$lt": 10000}}
    # response = collection.find(query, {"_id": 0})
    # for i in response:
    #     print(i)

    # 3.- What is the dominant letter within  five and 6 digits area range.

    # query = {"number": {"$gt": 9999, "$lt": 1000000}}
    # response = collection.find(query, {"_id": 0})
    # all_letters = "".join(x["letters"] for x in response)
    # dominant_letter = []

    # for letter in alphabet:
    #     count = len([1 for x in all_letters if x == letter])
    #     dominant_letter.append((letter, count))
    # max_tuple = max(dominant_letter, key=lambda x: x[1])
    # print(max_tuple)

    # 4.- Tell me the sum on numbers where majority letters are : (letter 1, letter 2, letter 3)

    # response = collection.find({}, {"_id": 0})
    # desired_letter = "C"
    # desired_letter_sum = 0
    # for i in response:
    #     letters_list = [x for x in i["letters"]]
    #     unique_letters_set = sorted(set(letters_list))
    #     letters_frequency_dict = {}
    #     for item in unique_letters_set:
    #         letters_frequency_dict[item] = letters_list.count(item)
    #     if letters_frequency_dict.get(desired_letter) == max(letters_frequency_dict.values()):
    #         desired_letter_sum += i["number"]
    # print(desired_letter_sum)

    # 5.- Show me the lowest and highest number and their representations

    response = collection.find({}, {"_id": 0})
    min_value = min(response, key=lambda x: x["number"])
    print(f"Lowest number: {min_value}")

    response = collection.find({}, {"_id": 0})
    max_value = max(response, key=lambda x: x["number"])
    print(f"Highest number: {max_value}")


