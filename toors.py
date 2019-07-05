# coding=utf-8
import sys
import sqlalchemy
from sqlalchemy import create_engine
import getpass
import configparser
from os import path
from os import listdir
from os import chdir
from subprocess import check_call
from subprocess import CalledProcessError
import tkinter.messagebox
import tkinter as tk
import glob
import shlex
import logging
import hashlib
import config
window=tk.Tk()
window.withdraw()

def get_file_list(str):
    '''config文件获得,分隔的多文件'''
    return list(filter(None,(','+str).split(',') ) )
def get_Trasen_dir():
    '''得到Trasen文件目录'''
    try:
        path_name=path.realpath(__file__)
    except NameError as e:
        return 'F:\Trasen'
    f_name=path_name.split("\\")
    if('Trasen'in f_name):
        while f_name!=[]:
            if('Trasen'==f_name.pop()):
                f_name.append('Trasen')
                return '\\'.join(f_name)
                break
    else:
        logging.ERROR('无法获取Trasen目录 ')
        tk.messagebox.showerror(title='注意', message='注册失败：'+path.dirname(path_name)+'不是Trasen子目录')
        exit(0)

def call_cmd(bat_file):
    check_call(bat_file,shell=True)
    logging.INFO(bat_file+'执行完成')
def get_log_lerver(lever):
    lever=lever.lower()
    if lever=='debug':
        return logging.DEBUG
    elif lever=='critlcal':
        return logging.CRITICAL
    elif lever=='error':
        return logging.ERROR
    elif lever=='warning':
        return logging.WARNING
    return logging.INFO
def get_crypt_module(cry_name):
    '''sha1, sha224, sha256, sha384, sha512, blake2b,blake2s. md5'''
    cry_name=cry_name.lower()
    if cry_name=='sha1':
        return hashlib.sha1()
    elif cry_name=='sha224':
        return hashlib.sha224()
    elif cry_name=='sha256':
        return hashlib.sha256()
    elif cry_name=='sha384':
        return hashlib.sha384()
    elif cry_name=='sha512':
        return hashlib.sha512()
    elif cry_name=='sha3_224':
        return hashlib.sha3_224()
    elif cry_name=='sha3_256':
        return hashlib.sha3_256()
    elif cry_name=='sha3_384':
        return hashlib.sha3_384()
    elif cry_name=='sha3_512':
        return hashlib.sha3_512()
    elif cry_name=='blake2b':
        return hashlib.blake2b()
    elif cry_name=='blake2s':
        return hashlib.blake2s()
    else:
        return hashlib.md5()

Trasen_tree=[]
def traverse(file_dir=None,Relative_path=''):
    if file_dir==None:
        file_dir=get_Trasen_dir()
    fs = listdir(file_dir)
    for f1 in fs:
        Trasen_tree.append(Relative_path+f1)
        tmp_path = path.join(file_dir,f1)
        if not path.isdir(tmp_path):
            pass
        else:
            if Relative_path=='':
                traverse(tmp_path,f1+'\\')
            else:
                traverse(tmp_path,Relative_path+f1+'\\')
traverse()
def GetFile_crypt(filename):
    path=check_file_and_get_path(filename)
    if not path:
        print('check_file_and_get_path')
        logging.error(filename+'不存在，无法计算MD5')
    elif not os.path.isfile(filename):
        logging.warn(filename+'不是文件，无法计算MD5')
    else:
        myhash =get_crypt_module(config.check_file_cfgs_module)
        logging.debug('加密检验：'+config.check_file_cfgs_module)
        with open(filename,'rb') as f:
            while True:
                b = f.read(8096)
                if not b:
                    break
                myhash.update(b)
        return myhash.hexdigest()

def make_check_all_file(file_name):
    with open(config.check_file_cfgs_make_all_check_file_filename,'w') as f:
        make_chech_cfg=configparser.ConfigParser()
        print('debug')
        make_chech_cfg['CHECK']={}
        for file in [files for files in Trasen_tree if files in get_file_list(check_file_cfgs['make_all_check_file_types']) or check_file_cfgs['make_all_check_file_types']=='*'] :
            crypt=GetFile_crypt(file)
            if crypt!=None:
                make_chech_cfg['CHECK'][file]=crypt
            logging.info(file+'概要生成成功')
        make_chech_cfg.write(f)
def make_check_file_from_ini(ini_file):
    pass
def check_file_and_get_path(file_name):
    if not file_name in Trasen_tree:
        logging.error(file_name+'不存在')
        return None
    else:
        return path.join(Trasen_dir,file_name)
def chech_file_crypt(file_name, outline):
    return GetFile_crypt(file_name)== outline
def get_absolute_path(file_path):
    if    path.isfile(file_path):
        return file_path
    elif path.isfile(path.join(Trasen_dir,file_path)):
        return path.join(Trasen_dir,file_path)
    else:
        logging.error('文件不存在')
        print('文件不存在')
        return None
Trasen_dir=get_Trasen_dir()
chdir(Trasen_dir)
Trasen_globs=glob.glob('*')
