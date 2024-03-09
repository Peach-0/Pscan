import argparse
import sys
from scan.subdomain import *
from scan.webdir import *
from scan.webport import *
from scan.ipport import *
from scan.finger import *
from lib.pscan_icn import *
from lib.pscan_exp import *
from lib.pscan_search import *
from lib.pscan_Initialization import *

icn()
Initialization_poc()

parser = argparse.ArgumentParser(prog='peach_scan',description=" = = * = = pscan = = * = = ")
subparsers = parser.add_subparsers(help='sub-command help')
parser_webdir = subparsers.add_parser('webdir', help='目录扫描模块')
parser_webport = subparsers.add_parser('webport', help='旁站扫描模块')
parser_subdomain = subparsers.add_parser('subdomain', help='子域名扫描模块')
parser_ipport = subparsers.add_parser('ipport', help='端口扫描模块')
parser_finger = subparsers.add_parser('finger', help='指纹识别模块')
parser_exp = subparsers.add_parser('exp', help='exp攻击模块')
parser_update = subparsers.add_parser('ru', help='重新初始化poc列表')
parser.add_argument('-v','--version',help='显示版本')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()
elif sys.argv[1] == "-h" or sys.argv[1] == "--help" :
    parser.print_help()
    sys.exit()
elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
    print('🌸\tpscan 1.1\t🌸')
if sys.argv[1] == "webdir" :
    parser_webdir.add_argument('-u','--url', help='目标url')
    parser_webdir.add_argument('-f','--file', help='字典文件',default='./dict/dicc/dicc.txt',required=False)
    parser_webdir.add_argument('-t','--theard',help='指定线程数',default=10,required=False)
    parser_webdir.add_argument('-s','--suffix', help='指定后缀')
    parser_webdir.add_argument('-ua','--useragent', help='指定浏览器ua')
    parser_webdir.add_argument('-c','--cookie', help='指定cookie')
    parser_webdir.add_argument('-o','--output', help='指定输出到某一文件中')
    parser_webdir.add_argument('-S','--sleep', help='设置延时,延时时间单位为秒,默认一秒',default=1,required=False)
    parser_webdir.add_argument('-C', '--code', help='指定状态码')
    parser_webdir.add_argument('-r', '--recursion', help='不进行递归',action='store_false')
    parser_webdir.add_argument('-p', '--porxy', help='设置代理')
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_webdir.print_help()
        sys.exit()
    args = parser.parse_args()
    webdir_scan(args)
elif sys.argv[1] == "webport" :
    parser_webport.add_argument('-u','--url', help='目标url')
    parser_webport.add_argument('-ua','--useragent', help='目标url')
    parser_webport.add_argument('-c','--cookie', help='指定cookie')
    parser_webport.add_argument('-o','--output', help='指定输出到某一文件中')
    parser_webport.add_argument('-S','--sleep', help='设置延时,延时时间单位为秒,默认一秒',default=1,required=False)
    parser_webport.add_argument('-t','--theard',help='指定线程数',default=20,required=False)
    parser_webport.add_argument('-p', '--porxy', help='设置代理')
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_webport.print_help()
        sys.exit()
    args = parser.parse_args()
    args.code = None
    args.recursion = False
    webport_scan(args)
elif sys.argv[1] == "subdomain":
    parser_subdomain.add_argument('-u','--url', help='目标url')
    parser_subdomain.add_argument('-f','--file', help='字典文件',default='./dict/Subdomain/16w.txt',required=False)
    parser_subdomain.add_argument('-t','--theard',help='指定线程数',default=20,required=False)
    parser_subdomain.add_argument('-o','--output',help='指定输出到某一文件中')
    parser_subdomain.add_argument('-S','--sleep', help='设置延时,延时时间单位为秒,默认一秒',default=1,required=False)
    parser_subdomain.add_argument('-m','--multilayer', help='设置多级子域名爆破')
    parser_subdomain.add_argument('-p','--porxy', help='设置代理')
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_subdomain.print_help()
        sys.exit()
    args = parser.parse_args()
    args.code = None
    args.recursion = False
    args.useragent = None
    args.cookie = None
    Subdomain_scan(args)
elif sys.argv[1] == 'finger':
    parser_finger.add_argument('-u','--url', help='目标ip地址')
    parser_finger.add_argument('-f','--file', help='对指定文件中的url进行批量指纹识别',default='./scan/cms_fingers.json',required=False)
    parser_finger.add_argument('-t','--theard',help='指定线程数',default=10,required=False)
    parser_finger.add_argument('-ua','--useragent', help='指定浏览器ua')
    parser_finger.add_argument('-c','--cookie', help='指定cookie')
    # parser_finger.add_argument('-d','--depth', help='深度扫描网站中的所能访问页面中是否存在关键词')
    # parser_finger.add_argument('-d','--depth', help='深度扫描网站中的所能访问页面中是否存在关键词',action='store_true')
    parser_finger.add_argument('-p','--porxy', help='设置代理')
    args = parser.parse_args()
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_finger.print_help()
        sys.exit()
    finger_scan(args)
#########################################################################################################################
elif sys.argv[1] == "ipport":
    parser_ipport.add_argument('-ip', help='目标ip地址')
    parser_ipport.add_argument('-port', help='指定端口')
    parser_ipport.add_argument('-t','--theard',help='指定线程数',default=10,required=False)
    parser_ipport.add_argument('-o','--output', help='指定输出到某一文件中')
    parser_ipport.add_argument('-S','--sleep', help='设置延时,延时时间单位为秒,默认一秒',default=1,required=False)
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_ipport.print_help()
        sys.exit()
    args = parser.parse_args()
    ipport_scan(args)
#########################################################################################################################
elif sys.argv[1] == 'exp':
    parser_exp.add_argument('-poc',help='指定poc')
    parser_exp.add_argument('-s','--search',help='搜索poc')
    parser_exp.add_argument('-url',help='目标URL')
    parser_exp.add_argument('-urlfile',help='URL集合文件')
    parser_exp.add_argument('-ip',help='目标IP')
    parser_exp.add_argument('-ipfile',help='IP集合文件')
    parser_exp.add_argument('-user',help='登录账号')
    parser_exp.add_argument('-pwd',help='登录密码')
    parser_exp.add_argument('-userfile',help='账号字典')
    parser_exp.add_argument('-passfile',help='密码字典')
    parser_exp.add_argument('-dir',help='目录')
    parser_exp.add_argument('-cmd',help='命令')
    args = parser.parse_args()
    if len(sys.argv) == 2 or sys.argv[2] == '-h' or sys.argv[2] == '--help':
        parser_exp.print_help()
        sys.exit()
    elif sys.argv[2] == '-s' or sys.argv[2] == '--search':
        search_poc(args)
        sys.exit()
    elif sys.argv[2] == '-poc':
        exp_start(args)
elif sys.argv[1] == 'update':
    Reset_poc()
    Initialization_poc()