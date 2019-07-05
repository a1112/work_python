import configparser
def get_file_list(str):
    '''config文件获得,分隔的多文件'''
    return list(filter(None,(','+str).split(',') ) )
conf=configparser.RawConfigParser()#ConfigParse
conf.read('initTrasen.ini')
ini=conf['ini']
ini_switch=ini['switch']
log_cfg=conf['log_base']
log_level=log_cfg['level']
log_format=log_cfg['format']
log_datefmt=log_cfg['datefmt']
log_filename=log_cfg['filename']
log_filemode=log_cfg['filemode']
log_style=log_cfg['style']

check_file_cfgs=conf['check_file_base']
check_file_cfgs_make_all_check_file=check_file_cfgs['make_all_check_file']

bat_files=get_file_list(conf['bat']['bat_file'])
regsvr32_files=get_file_list(conf['regsvr32']['regsvr32_file'])
sql_files=get_file_list(conf['sql server']['sql_file'])

check_file_cfgs_make_all_check_file_filename =check_file_cfgs['make_all_check_file_filename']
check_file_cfgs_module=check_file_cfgs['module']

def log_shell():
    pass