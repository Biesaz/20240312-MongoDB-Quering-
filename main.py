# https://github.com/CodeAcademy-Online/python-new-material-level2/wiki/Mongo-DB---lesson-3:-Quering-%5BPart1%5D
# Mongo DB lesson 3: Quering [Part1]
# Mindaugeliseth edited this page on May 22, 2023 · 11 revisions
# Introduction
# We can query a MongoDB database using PyMongo with the find function to get all the results satisfying the given condition and also using the find_one function, which will return only one result satisfying the condition.

# The following is the syntax of the find and find_one:

# your_collection.find( {<< query >>} , { << fields>>} )
# Filter based on fields & conditions
# For instance, you have hundreds of fields and you want to see only a few of them. You can do that by just putting all the required field names with the value 1. For example:

# your_shop_collection.find_one( {}, { "week": 1, "checkout_price" : 1})
# On the other hand, if you want to discard a few fields only from the complete document, you can put the field names equal to 0. Therefore, only those fields will be excluded. Please note that you cannot use a combination of 1s and 0s to get the fields. Either all should be one, or all should be zero.

# your_shop_collection.find_one( {}, {"num_orders" : 0, "meal_id" : 0})
# Now, in this section, we will provide a condition in the first braces and fields to discard in the second. Consequently, it will return the first document with center_id equal to 55 and meal_id equal to 1885 and will also discard the fields _id and week:

# your_shop_collection.find_one( {"center_id" : 55, "meal_id" : 1885}, {"_id" : 0, "week" : 0} )
# Filter based on Comparison Operators
# NAME	DESCRIPTION
# $eq	It will match the values that are equal to a specified value.
# $gt	It will match the values that are greater than a specified value.
# $gte	It will match all the values that are greater than or equal to a specified value.
# $in	It will match any of the values specified in an array.
# $lt	It will match all the values that are less than a specified value.
# $lte	It will match all the values that are less than or equal to a specified value.
# $ne	It will match all the values that are not equal to a specified value.
# $nin	It will match none of the values specified in an array.
# $eq and $ne
# Here are code examples for filtering MongoDB using PyMongo with the $eq (equals) and $ne (not equals) operators:

# from typing import List
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["your_database_name"]
# collection = db["your_collection_name"]

# # Filtering using $eq operator
# def filter_by_equals(field_name: str, value: str) -> List[dict]:
#     query = {field_name: {"$eq": value}}
#     result = collection.find(query)
#     return list(result)

# # Example usage: Filter documents where the "age" field is equal to 25
# filtered_equals = filter_by_equals("age", "25")
# print(filtered_equals)


# # Filtering using $ne operator
# def filter_by_not_equals(field_name: str, value: str) -> List[dict]:
#     query = {field_name: {"$ne": value}}
#     result = collection.find(query)
#     return list(result)

# # Example usage: Filter documents where the "name" field is not equal to "John"
# filtered_not_equals = filter_by_not_equals("name", "John")
# print(filtered_not_equals)
# In the above code:

# The filter_by_equals function takes a field name and a value as parameters, creates a query using the $eq operator, executes the query using collection.find(), and returns a list of matching documents.
# The filter_by_not_equals function is similar but uses the $ne operator instead.
# The resulting documents are converted to a list using list(result) to make it easier to work with the results.
# The function calls demonstrate filtering by the age field equal to 25 and the name field not equal to John, respectively.
# By encapsulating the filtering logic in functions, you can reuse the code for different fields and values as needed. Additionally, converting the query results to a list provides a concrete data structure for further processing.

# $gt and $lt
# Here are code examples for filtering MongoDB using PyMongo with the $gt (greater than) and $lt (less than) operators:

# from typing import List
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["your_database_name"]
# collection = db["your_collection_name"]

# # Filtering using $gt operator
# def filter_by_greater_than(field_name: str, value: int) -> List[dict]:
#     query = {field_name: {"$gt": value}}
#     result = collection.find(query)
#     return list(result)

# # Example usage: Filter documents where the "age" field is greater than 25
# filtered_greater_than = filter_by_greater_than("age", 25)
# print(filtered_greater_than)


# # Filtering using $lt operator
# def filter_by_less_than(field_name: str, value: int) -> List[dict]:
#     query = {field_name: {"$lt": value}}
#     result = collection.find(query)
#     return list(result)

# # Example usage: Filter documents where the "rating" field is less than 4.5
# filtered_less_than = filter_by_less_than("rating", 4.5)
# print(filtered_less_than)
# In the above code:

# The filter_by_greater_than function takes a field name and a value (expected to be an integer) as parameters. It creates a query using the $gt operator, executes the query using collection.find(), and returns a list of matching documents.
# The filter_by_less_than function is similar but uses the $lt operator instead.
# The resulting documents are converted to a list using list(result) to make it easier to work with the results.
# The function calls demonstrate filtering by the age field greater than 25 and the rating field less than 4.5, respectively.


# import datetime
# from random import randint
# from faker import Faker
# from pymongo import MongoClient
# from pymongo.collection import Collection
# from typing import Dict, List


# class MongoDB:
#     def __init__(
#         self, host: str, port: int, db_name: str, collection_name: str
#     ) -> None:
#         self.client = MongoClient(host, port)
#         self.db = self.client[db_name]
#         self.collection = self.db[collection_name]

#     def find_documents(self, query: Dict) -> List[Dict]:
#         documents = self.collection.find(query)
#         return list(documents)

#     def update_one_document(self, query: Dict, update: Dict) -> int:
#         result = self.collection.update_one(query, {"$set": update})
#         return result.modified_count
    
#     def update_many_document(self, query: Dict, update: Dict) -> int:
#         result = self.collection.update_many(query, {"$set": update})
#         return result.modified_count

#     def delete_one_documents(self, query: Dict) -> int:
#         result = self.collection.delete_one(query)
#         return result.deleted_count

#     def delete_many_documents(self, query: Dict) -> int:
#         result = self.collection.delete_many(query)
#         return result.deleted_count

#     def insert_one_document(self, document: Dict) -> str:
#         result = self.collection.insert_one(document)
#         print(f"Printed result: {result}")
#         return str(result.inserted_id)
    
#     def insert_many_document(self, document: Dict) -> List[str]:
#         result = self.collection.insert_many(document)
#         print(f"Printed result: {result}")
#         return list(result.inserted_ids)

#     def create_random_person(self) -> str:
#         fake = Faker()
#         name = fake.first_name()
#         surname = fake.last_name()
#         age = randint(18, 65)
#         now = datetime.datetime.now()
#         year_salary = randint(15000, 25000)


#         document = {
#             "name": name,
#             "surname": surname,
#             "age": age,
#             "salary": year_salary,
#         }
#         result = self.collection.insert_one(document)
#         print(f"Inserted document with ID: {result.inserted_id}")
#         print(f"This person was inserted into the database: {document}")

#         return str(result.inserted_id)

#     def generate_data_base(self, numb_of_documents):
#         for _ in range(numb_of_documents):
#             self.create_random_person()


# if __name__ == "__main__":
#     mongodb = MongoDB(
#         host="localhost",
#         port=27017,
#         db_name="workers",
#         collection_name="employees_salary",
#     )

#     query = {"name": "Steven"}
#     results = mongodb.find_documents(query)
#     print("Matching documents:")
#     for result in results:
#         print(result)

#     query = {"name": "Steven"}
#     update = {"age": 99}
#     modified_count = mongodb.update_many_document(query, update)
#     print(f"Modified {modified_count} documents")

#     query = {"name": "Steven"}
#     deleted_count = mongodb.delete_many_documents(query)
#     print(f"Deleted {deleted_count} documents")


#     numb_of_documents = 500
#     mongodb.generate_data_base(numb_of_documents)
################################################################################

