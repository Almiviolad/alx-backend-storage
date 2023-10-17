#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs:"""
def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs:"""
    doc = {}
    for key, value in kwargs.items():
        doc[key] = value
    result = mongo_collection.insert_one(doc)
    return result.inserted_id
