import re,threading,queue
from .webcode import getcode
# 初始化线程安全的队列
ok_url_queue = queue.Queue()

# 获取子域名列表
def add_protocol_if_needed(url,subdomain_1):
    for i in subdomain_1:
        if re.search(r'^(http://|https://)', url):
            url = url.replace('http://','').replace('https://', '')
        ok_url_queue.put('http://' + i + '.' +url)
        ok_url_queue.put('https://' + i + '.' + url)

# 开始扫描
def Subdomain_scan(args):
    with open(args.file, 'r') as file:
        subdomain_1 = [line.strip() for line in file]  # 读取文件并创建URL列表
    add_protocol_if_needed(args.url,subdomain_1)

    threads = []
    for _ in range(args.theard):
        thread = threading.Thread(target=process_url, args=(ok_url_queue,args,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if args.multilayer != None:
        if int(args.multilayer) > 0:
            args.multilayer = str(int(args.multilayer) - 1)

def process_url(queue,args):
    while not queue.empty():
        url = queue.get()
        try:
            getcode(url,args)
        except:
            pass
        queue.task_done()