#!/usr/bin/env python3

"""Python script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    method_stats = ""
    for method in methods:
        count = logs.count_documents({'method': method})
        method_stats += f"\n\tmethod {method}: {count}"
    
    status_check_count = logs.count_documents({
        "$and": [
            {"method": "GET"},
            {"path": "/status"}
        ]
    })
    
    total_logs_count = logs.count_documents({})
    
    display = f"{total_logs_count} logs\nMethods:{method_stats}\n{status_check_count} status check"
    print(display)
