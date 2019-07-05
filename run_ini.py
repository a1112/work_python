import config
import configparser
from toors import *
def get_file_list(str):
    '''config文件获得,分隔的多文件'''
    return list(filter(None,(','+str).split(',') ) )
def runconfig(config_file=''):
    conf=configparser.RawConfigParser()#ConfigParse
    main_switch=conf['ini']
    if ''==config:
        conf.read('initTrasen.ini')
    else:
        conf.read(config_file)
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

    bat=conf['bat']
    bat_switch=bat['switch']
    bat_files=get_file_list(bat['bat_file'])
    regsvr32=conf['regsvr32']
    regsvr32_switch=regsvr32['switch']
    regsvr32_files=get_file_list(regsvr32['regsvr32_file'])
    sql_server=conf['sql server']
    sql_switch=sql_server['switch']
    sql_files=get_file_list(sql_server['sql_file'])

    check_file_cfgs_make_all_check_file_filename =check_file_cfgs['make_all_check_file_filename']
    check_file_cfgs_module=check_file_cfgs['module']
    if ini_switch=='on':
        if bat_switch=='on':
            for bat_file in bat_files:
                try:
                    call_cmd(bat_file)
                except BaseException as e:
                    logging.error(e)
                else:
                    logging.debug(bat_file+'执行完成')
        if regsvr32_switch=='on':
            for regsvr32_file in regsvr32_files:
                try:
                    call_cmd('regsvr32 {0}\\{1}'.format(Trasen_dir,regsvr32_file))
                except CalledProcessError as e:
                    logging.error(e)
                else:
                    logging.debug('regsvr32 {0}\\{1}'.format(Trasen_dir,regsvr32_file)+'执行完成')
        if sql_switch=='on':
            try:

                host=sqlserver_cfg['host']
                user=sqlserver_cfg['user']
                password=sqlserver_cfg['password']
            except Base
            port=sqlserver_cfg['port']
            charset=sqlserver_cfg['charset']
            sql_files=get_file_list(sqlserver_cfg['sql_files'])
            con=pymssql.connect(host,user,password,port,charset)
            if(con):
                logging.DEBUG('链接成功')
                with con.cursor() as cursor:
                    if sql_files:
                        for sql_file in sql_files:
                            try:
                                with open(sql_file,'r+',codeing='utf-8') as f:
                                    cursor.execute(f.read())
                            except pymssql.Error,e:
                                logging.ERROR(e)
            else:
                logging.error('连接失败')




