import requests
import threading
import queue
from .webcode import getcode

ok_url_queue = queue.Queue()
def add_protocol_if_needed(url):
    for i in range(1, 65536):
        ok_url_queue.put(url + ':' + str(i))

def webport_scan(args):
    add_protocol_if_needed(args.url)
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
