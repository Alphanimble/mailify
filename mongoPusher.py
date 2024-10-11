import json
def convert_to_json(obj_list):
    json_list= [json.dumps(x.__dict__) for x in obj_list] 
    return json_list
