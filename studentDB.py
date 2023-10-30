from pymongo import MongoClient
import pandas as pd
from dateutil import parser
from datetime import datetime

class StudentDB():
    def __init__(self):
        # connection variables
        self.mongodb_uri = "mongodb://localhost:27017"
        self.database_name = "SmartGurucool"
        self.collection_name = "students"
        self.csv_path = "Student_DB.csv"

    def load_data_from_csv(self):
        try:
            # reading the csv
            self.df = pd.read_csv(self.csv_path)

            # converting date strings to Python datetime objects
            self.df["Joined_On"] = pd.to_datetime(self.df["Joined_On"])
            self.df["S_DOB"] = pd.to_datetime(self.df["S_DOB"])

            # converting phone numbers to string format and also adding + in front
            def add_plus(phone_no):
                return "+" + phone_no
            self.df["Personal_Phone"] = self.df["Personal_Phone"].astype(str).apply(add_plus)
            self.df["Parent_Phone"] = self.df["Parent_Phone"].astype(str).apply(add_plus)

            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # converting the dataframe to list of dictionaries (one dictionary per row)
            self.data = self.df.to_dict(orient="records")

            # inserting the data into MongoDB collection
            self.collection.insert_many(self.data)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()
            return "Data loaded in MongoDB successfully."

    def get_all_students(self):
        try:
            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # mongodb query to get student data
            result = self.collection.find(
                {
                },
                {
                    "Name":1,
                    "Email_ID":1,
                    "Student_Rating":1,
                    "S_DOB":1,
                    "Country":1,
                    "Personal_Phone":1,
                    "_id":0
                }
            )

            students = []
            for student in result:
                student["S_DOB"] = parser.parse(str(student["S_DOB"])).strftime("%B %d, %Y")
                students.append(student)
            return students

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()

    def rating_more_than_7(self):
        try:
            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # mongodb query to get student data
            result = self.collection.find(
                {
                    "Student_Rating":{"$gt":7}
                },
                {
                    "Name":1,
                    "Email_ID":1,
                    "Student_Rating":1,
                    "S_DOB":1,
                    "Country":1,
                    "Personal_Phone":1,
                    "_id":0
                }
            )

            students = []
            for student in result:
                student["S_DOB"] = parser.parse(str(student["S_DOB"])).strftime("%B %d, %Y")
                students.append(student)
            return students

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()

    def rating_less_than_7(self):
        try:
            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # mongodb query to get student data
            result = self.collection.find(
                {
                    "Student_Rating":{"$lt":4}
                },
                {
                    "Name":1,
                    "Email_ID":1,
                    "Student_Rating":1,
                    "S_DOB":1,
                    "Country":1,
                    "Personal_Phone":1,
                    "_id":0
                }
            )

            students = []
            for student in result:
                student["S_DOB"] = parser.parse(str(student["S_DOB"])).strftime("%B %d, %Y")
                students.append(student)
            return students

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()

    def born_after_june_01_1999(self):
        try:
            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # mongodb query to get student data
            result = self.collection.find(
                {
                    "S_DOB":{
                        "$gt":datetime(1999,6,1)
                    }
                },
                {
                    "Name":1,
                    "Email_ID":1,
                    "Student_Rating":1,
                    "S_DOB":1,
                    "Country":1,
                    "Personal_Phone":1,
                    "_id":0
                }
            )

            students = []
            for student in result:
                student["S_DOB"] = parser.parse(str(student["S_DOB"])).strftime("%B %d, %Y")
                students.append(student)
            return students

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()

    def query_database(self,user_query):
        try:
            # creating mongoDB client
            self.client = MongoClient(self.mongodb_uri)

            # accessing the specified database and connection
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # mongodb query to get student data
            result = self.collection.find(
                user_query,
                {
                    "Name":1,
                    "Email_ID":1,
                    "Student_Rating":1,
                    "S_DOB":1,
                    "Country":1,
                    "Personal_Phone":1,
                    "_id":0
                }
            )

            students = []
            for student in result:
                student["S_DOB"] = parser.parse(str(student["S_DOB"])).strftime("%B %d, %Y")
                students.append(student)
            return students

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # closing the mongoDB connection
            self.client.close()

    def drop_database(self):
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        
        # Drop the specified database
        try:
            client.drop_database(self.database_name)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            return "Database has been dropped."

# students = StudentDB()
# print(students.load_data_from_csv())
# print(students.get_all_students())
# print(students.rating_more_than_7())
# print(students.rating_less_than_7())
# print(students.born_after_june_01_1999())
# print(students.drop_database())
# print(students.query_database({"Country":"Hong Kong"}))