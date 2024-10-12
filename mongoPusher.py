import json
import pymongo
def convert_to_json(obj_list, filename='output.json'):
    # Check if obj_list is a list
    if isinstance(obj_list, list):
        # Convert each object in the list to a dictionary
        dict_list = [obj.__dict__ for obj in obj_list]
    else:
        # If it's not a list, assume it's a single object
        dict_list = [obj_list.__dict__]

    # Write the JSON data to a file
    with open(filename, 'w') as f:
        json.dump(dict_list, f, indent=2)

        
def add_to_mongodb_atlas(obj):
    try:
        # Convert class object to dictionary
        obj_dict = obj.__dict__

        # Set up MongoDB connection
        client = pymongo.MongoClient("mongodb+srv://rakshithg:SIbj21ewFW44vGMk@cluster0.ds15t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client["Datafied_Emails"]
        collection = db["Email_data"]

        # Insert the object into MongoDB
        result = collection.insert_one(obj_dict)

        if result.acknowledged:
            print(f"Successfully inserted document with ID: {result.inserted_id}")
        else:
            print("Failed to insert document")

    except Exception as e:
        print(f"An error occurred: {str(e)}")