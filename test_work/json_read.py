import json

with open('test.json','r+' ,encoding='utf-8')as f:
    js=json.load(f)
    print(dict( js['format']))




def dict_Data_cleaning(dict_str):
    pass
