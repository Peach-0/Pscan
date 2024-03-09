import random
from time import sleep
import requests


recursion_urls =[]

def usera(args):
    headers = {}
    if args.useragent != None:
        headers['User-Agent'] = args.useragent
    elif args.useragent == None:
        user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        ]
        # 随机选择一个
        user_agent = random.choice(user_agent_list)
        headers['User-Agent']=user_agent
    if args.cookie != None:
        headers['cookie'] = args.cookie
    return headers

def getcode(url,args):
    try:
        porxy = {}
        if args.porxy != None:
            porxy['http'] = f'socks5://{args.porxy}'
            porxy['https'] = f'socks5://{args.porxy}'
        headers = usera(args)
        response = requests.get(url,headers=headers, timeout=3,proxies=porxy,allow_redirects=False)
        status_code = response.status_code
        if args.code != None:
            if int(args.code) == status_code:
                status_codes(url,status_code,args,response)
        elif args.code == None:
            status_codes(url,status_code,args,response)
        if args.sleep != None:
            sleep(int(args.sleep))
    except:
        pass

def status_codes(url,status_code,args,response):
    if status_code == 200:
        print('\033[0;32m' + '[+]-- ' + str(status_code) + " " + '\033[0;34m' + str(url) + '\033[0m')
        output_url(url, status_code, args)
        if args.recursion == True:
            args.url = url
            recursion(args)
        if args.multilayer != None:
            if int(args.multilayer) > 0:
                args.url = url
                multilayer(args)
    elif status_code == 500:
        print('\033[0;35m' + '[+]-- ' + str(status_code) + " " + '\033[0;34m' + str(url) + '\033[0m')
        output_url(url, status_code, args)
    elif 300 <= status_code < 400:
        try:
            print('\033[0;33m' + '[+]-- ' + str(status_code) + " " + '\033[0;34m' + str(url) + '\033[0m' + "  -->  " + '\033[0;35m' + response.headers['Location'] + '\033[0m')
            output_url(url, status_code, args)
        except:
            print('\033[0;33m' + '[+]-- ' + str(status_code) + " " + '\033[0;34m' + str(url) + '\033[0m')
            output_url(url, status_code, args)
    elif 400 <= status_code < 500:
        print('\033[0;31m' + '[+]-- ' + str(status_code) + " " + '\033[0;34m' + str(url) + '\033[0m')
        output_url(url, status_code, args)
    # else:
    #     print('[+]-- ' + '\033[0;34m' + "服务器错误" + "\t\t" + '\033[0;35m' + str(url) + '\033[0m')
    #     output_url(url, status_code, args)
def output_url(url,status_code,args):
    if args.output != None:
        with open(args.output,'w') as f:
            f.write(url)

def recursion(args):
    from .webdir import webdir_scan
    webdir_scan(args)

def multilayer(args):
    from .subdomain import Subdomain_scan
    Subdomain_scan(args)