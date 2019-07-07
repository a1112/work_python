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
#A  bat run 
