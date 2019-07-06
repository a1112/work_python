import logging
import os
import shlex
def call_file_shell():
    codes=input('file->>>{0}>'.format(os.getcwd))
    codes=shlex.shlex(codes)
    print('test')
    
