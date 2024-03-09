import re
import threading
import queue
from .webcode import getcode

ok_url_queue = queue.Queue()
def add_protocol_if_needed(url,dicc,args):
    for i in dicc :
        if args.suffix == None:
            ok_url_queue.put(url + i)
        elif args.suffix != None:
            pattern = r'.*' + re.escape(args.suffix) + r'$'
            if args.suffix and re.search(pattern,i):
                ok_url_queue.put(url + i)

def webdir_scan(args):
    with open(args.file, 'r') as file:
        dicc = [line.strip() for line in file]
    u = args.url + '/'
    add_protocol_if_needed(u,dicc,args)
    threads = []
    for _ in range(int(args.theard)):
        thread = threading.Thread(target=process_url, args=(ok_url_queue,args,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def process_url(queue,args):
    while not queue.empty():
        url = queue.get()
        try:
            getcode(url,args)
        except:
            pass
        queue.task_done()