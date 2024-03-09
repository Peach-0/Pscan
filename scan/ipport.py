import socket
import threading
import queue
import ipaddress


def scan(ips,q):
    for i in range(len(ips)):
        while not q.empty():
            x = q.get()
            try:
                s = socket.socket()
                s.connect((str(ips[i]), int(x)))
                print(f"{ips[i]}:{x}\topen")
            except socket.error as e:
                # error_str = str(e)
                # print(f"{ips[i]}:{x}\terror: {error_str}")
                pass
            except Exception as e:
                # error_str = str(e)
                # print(f"{ips[i]}:{x}\terror: {error_str}")
                pass
            finally:
                s.close()
                q.task_done()


def ipport_scan(args):
    ips = []
    ports = []
    ip = args.ip
    port = args.port
    theard = args.theard
    try:
        if ip.find('/') >= 1:
            net = ipaddress.ip_network((str(ip)))
            for x in net.hosts():
                ips.append(x)
        elif ip.find('/') < 1:
            ips.append(ip)
    except ValueError:
        pass

    try:
        if port== 'all' or port == 'ALL':
            for i in range(1,65536):
                ports.append(i)
        elif port.find(',') >= 1:
            port = port.split(',')
            for i in range(len(port)):
                ports.append(port[i])
        elif port.find('-') > 0:
            port = port.split('-')
            for i in range(int(port[0]), int(port[1]) + 1):
                ports.append(i)
        elif port.find(',') < 1 and port.find('-') < 1:
            ports.append(port)
    except:
        pass
    q = queue.Queue()
    for p in ports:
        q.put(p)

    threads_list = []
    for _ in range(theard):
        t = threading.Thread(target=scan, args=(ips, q))
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()
    q.join()