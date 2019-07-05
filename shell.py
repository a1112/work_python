import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-sql','--sql',help='database config,test,（t)test,(s)show,show help.',nargs=2)
parser.add_argument("-v", "--verbose",help="查看版本",
                    action="store_true")
parser.add_argument("-V", "--version",help="查看版本",
                    action="store_true")
parser.add_argument("-py","--python",help="开发者调试工具",
                    action="store_true")
parser.add_argument('-cfg','--config',help="ini文件编辑阅读工具，",
                    action="store_true")
parser.add_argument('-run',help='使用ini文件运行程序')
args = parser.parse_args()
import logging
import sql_shell
import py_shell
import cfg_shell
import config
from toors import get_log_lerver
def call_py_shell():
        print('欢迎来到开发者模式，您可以直接执行python语句：输入q退出')
        py_shell.pyshell()
def call_sql_shell():
        print('欢迎使用sql shell')
def call_cfg_shell():
        print('欢迎使用cfg_shell')
        cfg_shell.call_cfg_shell()

if args.verbose or args.version:
    print("            init_Trasen 1.0\n功能开发中。。。。。。")
if args.config==True:
        call_cfg_shell()
if args.python ==True:
        call_py_shell()
# parser = argparse.ArgumentParser()
# parser.add_argument('-sql',help='database config,test,（t)test,(s)show,show help.',nargs=2)
# parser.add_argument("-v", "--verbose",help="查看版本",
#                     action="store_true")
# parser.add_argument("-V", "--version",help="查看版本",
#                     action="store_true")
# parser.add_argument("-py","-python",help="开发者调试工具",
#                     action="store_true")
# parser.add_argument('-cfg','-config',help="ini文件编辑阅读工具，",
#                     action="store_true")
# parser.add_argument('echo',help='test')

logging.basicConfig(level=get_log_lerver(config.log_level),
                    format=config.log_format,   
                    datefmt=config.log_datefmt,   
                    filename=config.log_filename,   
                    filemode=config.log_filemode,
                    style=config.log_style)
'''_____________________________________________________'''
# def call_py_shell():
#         print('欢迎来到开发者模式，您可以直接执行python语句：输入q退出')
#         py_shell.pyshell()
# def call_sql_shell():
#         print('欢迎使用sql shell')
# def call_cfg_shell():
#         print('欢迎使用cfg_shell')
#         cfg_shell.call_cfg_shell()
'''_____________________________________________________'''
# if args.verbose or args.version:
#     print("            init_Trasen 1.0\n功能开发中。。。。。。")
# if args.cfg==True:
#         call_cfg_shell
# if args.py ==True:
#         call_py_shell()

'''_____________________________________________________'''
if args.sql!=None and args.sql[0]=='test':
    database_str=sql_shell.get_database_str(args.sql[1])
    engine=sql_shell.create_engine(database_str,echo=True)
    print(engine)
    try:
        conn = engine.connect()
    except ConnectionRefusedError as e:
        print(e)
        logging.error(e)
    except sql_shell.sqlalchemy.exc.OperationalError as e:
        print(e)
        logging.error(e)
        print('连接参数有误。。。。。。')
    else:
        print('连接成功。  ')
        shell_code=input('输入shell进入sql指令系统1.0')
        if shell_code=='shell':
            sql_shell.call_shell()
'''_____________________________________________________'''