import json

with open('test.json','r+' ,encoding='utf-8')as f:
    js=json.load(f)
    print(dict( js['format']['money']['map']))
    print(check_row_clo('C',7,js['format']['money']))
    js['format']['money']['format']=set()
    

__check_cell__('B','A:C,C')

def check_row_clo(x,y,format):
    format=format['map']
    for row in format.keys():
        if __check_cell__(x,row) and __check_cell__(y,format[row]):
            return True
    return False

def __check_cell__(x,string):
    x=str(x)
    if string=='*':
        return True
    else:
        strs=string.split(',')
        if x in strs:
            return True
        else :
            for area in [ar for ar in strs if ':' in ar]:
                a0=area.split(':')[0].upper()
                a1=area.split(':')[1].upper()
                if a0<=x.upper() and a1>=x.upper() and len(a0)<=len(x) and len(a1)>=len(x):
                    return True
    return False




def dict_Data_cleaning(dict_str):
    pass
