import logging
import sqlalchemy
from sqlalchemy import create_engine
import getpass
import shlex
from toors import get_absolute_path
engine=None
conn=None
'''_____________________________________________________'''

def print_help():
    '''help text'''
    print('begin_sql    开始执行原生sql 语句\n\
        end_sql    结束sql语句\n\
        exec    执行文件(.txt,.sql)的sql语句,可附加编码参数，文件名，编码以字符串提供\n\
        ')
'''_____________________________________________________'''
def get_database_str(database_type):
    database_type= database_type.lower()
    if database_type=='mysql':
        return sql_test('mysql+pymysql')
    elif database_type=='sqlserver':
        return sql_test('mssql+pymssql')
    elif database_type=='sqlite':
        dbname=input('数据库')
        return 'sqlite:///'+dbname
    else :
        logging.error('暂不支持该数据库')
        print('暂不支持该数据库')
        return None
        '''
        !!!!!!!!!!!!!!!!!!!!!!!!!!
        
        '''
def sql_test(database_type):
    host=input('数据库地址')
    user=input('用户')
    password = getpass.getpass("密码:")
    dbname=input('数据库')
    port=input('port')
    if port==''and database_type=='mssql+pymssql':
        port= '1433'
    if port==''and database_type=='mysql+pymysql':
        port= '3306'
    return database_type+'://'+user+':'+password+'@'+host+':'+port+'/'+dbname
def call_begain_sql():
    sql_str=''
    while True:
        in_str=input()
        if in_str=='end_sql':
            run_sql(sql_str)
            break
        else:
            sql_str=sql_str+in_str+'\n'
    
'''_____________________________________________________'''


def call_shell():
    print('欢迎！输入-help获得帮助')
    while True:
        shell=input()
        if shell=='-help':
            print_help()
        elif shell=='begin_sql':
            call_begain_sql()
        elif shell=='exit':
            break
        elif 'create'in repr(shell.lower()).split(' ')[0]:
            shellcode=shlex.shlex(shell,punctuation_chars=True)
        
        elif 'exec'==repr(shell.lower()).split(' ')[0]:
            shellcode=shlex.shlex(shell,punctuation_chars=True)
            absolute_path=get_absolute_path(shellcode[1])
            encoding=None
            if len(shellcode)>=3:
                encoding=shellcode[1]
            run_sql(conn,file=absolute_path,encoding=encoding)
        elif 'insert' in repr(shell.lower()).split(' ')[0]:
             shellcode=shlex.shlex(shell,punctuation_chars=True)

        elif 'exec_py'==shell:
            pass

def run_sql(con,sql_code=None,file=None,encoding=None):
    try:
        if not sql_code:
            con.execute(sql_code,encoding=encoding)
        elif not file:
            con.execute(_get_sql_from_file(file,encoding=encoding))
    except BaseException as e:
        print(e)

def _get_sql_from_file(file_path,encoding=None):
    code=''
    with open(file_path,'r',encoding=encoding) as f:
        for line in f.readlines():
            code=code+line
    return code