import config
import configparser
import shlex
from toors import get_absolute_path
from toors import get_absolute_path
configs={}

def call_cfg_shell():
    defaulte=configparser.ConfigParser()
    ini_file_name='initTrasen.ini'
    absolute_path=get_absolute_path(ini_file_name)
    check=False
    mod='default'
    defaulte.read(absolute_path)
    while True:
        line=input('-cfg->>>')
        if line=='q':
            break
        try :
            codes=shlex.shlex(line)
            codes=list(codes)
        except BaseException as e:
            print(e)
        else:
            if len(codes)>=1:
                instruct1=pop_one_code(codes)
                if 'read'==instruct1:
                    if codes==[]:
                        pass
                    else:
                        file_path=get_absolute_path(pop_one_code(codes))
                        if file_path!=None and codes==[]:
                            defaulte.read(file_path)
                        if pop_one_code(codes).lower()=='true':
                            defaulte=configparser.RawConfigParser()
                            defaulte.read(file_path)
                if 'show'==instruct1 or 'get'==instruct1:
                    if codes==[]:
                        print(defaulte.sections())
                    else :
                        section=pop_one_code(codes)
                        if codes==[]:
                            show(section,config=defaulte)
                        else:
                            show(section,pop_one_code(codes),config=defaulte)
                if 'set' == instruct1:
                    if codes==[]:
                        print('set sesection options = value')
                    else:
                        section=pop_one_code(codes)
                        section=get_config_str(section,'',defaulte)
                        if codes==[]:
                            if check:
                                defaulte[section]={}
                            else:
                                print('不存在，拒绝修改')
                        else:
                            isoptions=pop_one_code(codes)
                            if isoptions=='=':
                                value=' '.join(codes)
                                if defaulte.has_section(section):
                                    defaulte[value]=defaulte[section]
                                    defaulte.remove_section(section)
                                elif check:
                                    defaulte[section]=get_ini(codes)
                                else:
                                    print('拒绝修改')
                            else:
                                options=isoptions
                                section,options=get_config_str(section,options,defaulte)
                                print("dwbug++"+options)
                                if codes != [] and pop_one_code(codes)=='=':
                                    if defaulte.has_option(section,options):
                                        defaulte[section][options]=' '.join(codes)
                                    elif defaulte.has_section(section):
                                        if check:
                                            defaulte[section][options]=' '.join(codes)
                                        else:
                                            print('字段不存在，拒绝修改')
                elif 'all'==instruct1:
                    show(deep=True,config=defaulte)
                    
                elif instruct1 in ['-h','-help']:
                    get_help()
                elif "config"==instruct1:
                    print('file: {0}'.format(absolute_path))
                    print('mod: ')
                    print('check: '+check+'是否检验属性存在')
        finally:
            pass

def get_ini(codes):
    return {} 
def isfunc():
    pass
def commit(config,file_name=None,encoding=None):
    if file_name!=None:
        with open(file_name,'w'):
            config.write(file_name,encodeig=encoding)
    else:
        pass
def pop_one_code(codes):
    if codes!=[]:
        return _get_shlex_str(codes.pop(0))
    else:
        return codes
def _get_shlex_str(code):
    if len(code)>1 and code[0] in get_herd_end() and code[-1] in get_herd_end() and code[0]==code[-1]:
        return _get_shlex_str(code[1:-1])
    else:
        return code
def get_herd_end():
    return ['\'','\"','(',')','[',']','‘','“','【','】','（','）']
def get_config_str(section='',options='',config=None):
    if section!='':
        try:
            size_s=int(section)
        except ValueError as e:
            section=section
        else:
            if config!=None and size_s>=0 and size_s<len(config):
                section=config.sections()[size_s]
            else:
                section=section
    else :
        raise ValueError('错误使用')
    if options !='':
        try:
            size_o=int(options)
        except ValueError as e:
            options=options
        else:
            if config.has_section(section) and size_o>=0 and size_o<len(config[section]):
                options=config.options(section)[size_o]
            else:
                options=options
    return [section,options]


def read(file_name):
    file_name=get_absolute_path(file_name)
    conf=configparser.ConfigParser()
    conf.read(file_name)
    return conf
def show(section='',options='',config=None,deep=False):
    section,options=get_config_str(section,options,config)
    try:
        if section!='' and options=='' :
            if config.has_section(section):
                print('''[{0}]'''.format(section))
                for option in config[section]:
                    print('\t{0}={1}'.format(option,config[section][option]))
            else:
                print('{0}属性未找到'.format(section))
        elif section!='' and options!='':
            if config.has_option(section,options):
                print('{0}={1}'.format(options,config[section][options]))
            else:
                print('[{0}][{1}]属性未找到'.format(section,options))
        elif section!='' and options!='' and (not config.has_section(section) or not config.has_option(section,option)):
            print('属性不存在。')
        elif deep:
            for line in config:
                print('[{0}]'.format(line))
                if deep and type(config) is configparser.ConfigParser:
                    for row in config[line]:
                        print('\t{0}={1}'.format(row,config[line][row]))
        else:
            print('超出预期')
    except configparser.InterpolationSyntaxError as e:
        print(e)
        print('特殊字符，请使用configparser.RawConfigParser,暂时不处理')
codestack=[]
def get_help():
    print('read:    读取ini文件 read finename line_read(可选，按行读，true/false)')
    print('show/get 按照参数读，')
    print('set 更改值，可使用索引简化')
    print('add 添加')
    print('config,查看，修改参数')
    print('save 保存')
def parsr(code):
    if code=='(':
        pass
