#!/usr/bin/env python3
"""Contains Python function that changes all topic
of a school document based on the name:"""
def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics 
    of a school document based on the name:"""
    search = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(search, new_values)
