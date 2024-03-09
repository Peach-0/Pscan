def thelp_run():
    print('''信息收集
    目录扫描:webdir_scan
        python pscan.py -tool webdir -url http://127.0.0.1/<br>
    
    子域名扫描:subomain_scan
        python pscan.py -tool subdomain -url qq.com

    
    端口扫描:port_scan
        python pscan.py -tool ipport -ip 127.0.0.1/24 -port all
        -ip:
            -ip 192.168.1.0/24;-ip 192.168.1.1
        -port:
            -port all;-port ALL;-port 400-500;-port 445;-port 335,445
    
    有无cdn
    
    web端口扫描:webport_scan
        python pscan.py -tool
    
    旁站
    
    js扫描
        python pscan.py -tool
    
    蜜罐识别
        python pscan.py -tool''')
