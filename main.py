# coding=utf-8
import argparse
import sys
import sqlalchemy
from sqlalchemy import create_engine
import configparser
from os import path
from subprocess import check_call
from subprocess import CalledProcessError
import tkinter.messagebox
import tkinter as tk
import glob
import pymssql
import shlex
import os
import logging
import hashlib
import sys
from toors import *
import config
'''tk初始化'''
#log_base

ok_list=[]
error_dict={}
'''
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
 
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
 
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
 
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
'''
if args.sql[0]=='test':
    if args.sql[1]=='test':
        sql_test()
    


#A  bat run 
for bat_file in config.bat_files:
    try:
        print(bat_file)
        logging.debug(bat_file)
        call_cmd(bat_file)
    except CalledProcessError as e:
        logging.error(bat_file+'指令失败')
        logging.error(e)
        print(e)
        error_dict[bat_file]=e
    else:
        ok_list.append(bat_file)
        logging.info(bat_file+'指令成功')
if 'true'==config.check_file_cfgs_make_all_check_file:
    make_check_all_file(Trasen_dir)