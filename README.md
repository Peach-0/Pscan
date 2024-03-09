# <span style="color: #03f8f8;">PSCAN-README</span>

<pre style="white-space: pre-wrap;">
<span style="color: #66ff00;">██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗  🌸
██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║  🌸
██████╔╝███████╗██║     ███████║██╔██╗ ██║  🌸
██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║  🌸
██║     ███████║╚██████╗██║  ██║██║ ╚████║  🌸
╚═╝     ╚══════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═══╝</span>  🌸  <span style="color: #3292ce;">peach-scan 1.1.2</span>
<span style="color: #03f8f8;">[-]</span>信息收集模块:
    <span style="color: #0037ff;">[+]</span> webdir     -->  目录扫描
    <span style="color: #0037ff;">[+]</span> webport    -->  旁站扫描
    <span style="color: #0037ff;">[+]</span> subdomain  -->  子域名扫描
    <span style="color: #0037ff;">[+]</span> ipport     -->  端口扫描
    <span style="color: #0037ff;">[+]</span> finger     -->  指纹识别

<span style="color: #03f8f8;">[-]</span> 信息收集模块:
    <span style="color: #0037ff;">[+]</span> exp        -->  poc攻击
</pre>
## <span style="color: #03f8f8;">webdir</span>
<pre style="white-space: pre-wrap;">
web目录扫描
    默认扫描线程10；
    默认目录字典文件在dict/dicc/dicc.txt；
    useragent是随机的几条浏览器useragent，或许可能会导致不能够正常访问。

使用例子：
    基础：
    python pscan.py webdir -u http://ex.com
    全命令：
    python pscan.py webdir -u http://ex.com -t 10 -f dicc.txt -ua "xxx" -c "xxx" -o haha.txt -S 1 -C 200 -r -p 127.0.0.1:7890

指令描述：
usage: peach_scan webdir [-h] [-u URL] [-f FILE] [-t THEARD] [-s SUFFIX] [-ua USERAGENT] [-c COOKIE] [-o OUTPUT] [-S SLEEP] [-C CODE] [-r] [-p PORXY]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标url
  -f FILE, --file FILE  字典文件
  -t THEARD, --theard THEARD
                        指定线程数
  -s SUFFIX, --suffix SUFFIX
                        指定后缀
  -ua USERAGENT, --useragent USERAGENT
                        指定浏览器ua
  -c COOKIE, --cookie COOKIE
                        指定cookie
  -o OUTPUT, --output OUTPUT
                        指定输出到某一文件中
  -S SLEEP, --sleep SLEEP
                        设置延时,延时时间单位为秒,默认一秒
  -C CODE, --code CODE  指定状态码
  -r, --recursion       不进行递归
  -p PORXY, --porxy PORXY
                        设置代理
</pre>
## <span style="color: #03f8f8;">webport</span>
<pre style="white-space: pre-wrap;">
web端口扫描，用于进行旁站扫描
    默认扫描线程20，扫描全端口，不能指定，如果有需要的话，后续版本会进行更新；
    默认延时1s，以防短时间扫描内容过多；

使用例子：
    基础：
    python pscan.py webport -u http://ex.com
    全命令：
    python pscan.py webport -u http://ex.com -t 10 -ua "xxx" -c "xxx" -o haha.txt -S 1 -p 127.0.0.1:7890

指令描述：
usage: peach_scan webport [-h] [-u URL] [-ua USERAGENT] [-c COOKIE] [-o OUTPUT] [-S SLEEP] [-t THEARD] [-p PORXY]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标url
  -ua USERAGENT, --useragent USERAGENT
                        目标url
  -c COOKIE, --cookie COOKIE
                        指定cookie
  -o OUTPUT, --output OUTPUT
                        指定输出到某一文件中
  -S SLEEP, --sleep SLEEP
                        设置延时,延时时间单位为秒,默认一秒
  -t THEARD, --theard THEARD
                        指定线程数
  -p PORXY, --porxy PORXY
                        设置代理
</pre>
## <span style="color: #03f8f8;">subdomain</span>
<pre style="white-space: pre-wrap;">
子域名扫描
    默认子域名文件dict/Subdomain/16w.txt；
    默认线程20；
    默认延时1s；
    可进行多级子域名爆破，用-m可以指定最大的子域名级别；

使用例子：
    基础：
    python pscan.py subdomain -u ex.com
    全命令：
    python pscan.py subdomain -u ex.com -t 10 -f subdomain.txt -o haha.txt -S 1 -m 3 -p 127.0.0.1:7890

指令描述：
usage: peach_scan subdomain [-h] [-u URL] [-f FILE] [-t THEARD] [-o OUTPUT] [-S SLEEP] [-m MULTILAYER] [-p PORXY]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标url
  -f FILE, --file FILE  字典文件
  -t THEARD, --theard THEARD
                        指定线程数
  -o OUTPUT, --output OUTPUT
                        指定输出到某一文件中
  -S SLEEP, --sleep SLEEP
                        设置延时,延时时间单位为秒,默认一秒
  -m MULTILAYER, --multilayer MULTILAYER
                        设置多级子域名爆破
  -p PORXY, --porxy PORXY
                        设置代理

</pre>
## <span style="color: #03f8f8;">ipport</span>
<pre style="white-space: pre-wrap;">
ip端口扫描，没有ip探测，只有端口扫描。
    -ip可以以192.168.1.1或者192.168.1.0/24两种方式指定；
    -port可以以80或80,81,445或300-500等三种方式；

使用例子：
    基础：
    python pscan.py ipport -ip 192.168.1.0/24
    全命令：
    python pscan.py ipport -ip 192.168.1.0/24 -port 300-500 -t 50 -o haha.txt 

指令描述：
usage: peach_scan ipport [-h] [-ip IP] [-port PORT] [-t THEARD] [-o OUTPUT] [-S SLEEP]

options:
  -h, --help            show this help message and exit
  -ip IP                目标ip地址
  -port PORT            指定端口
  -t THEARD, --theard THEARD
                        指定线程数
  -o OUTPUT, --output OUTPUT
                        指定输出到某一文件中
  -S SLEEP, --sleep SLEEP
                        设置延时,延时时间单位为秒,默认一秒
</pre>
## <span style="color: #03f8f8;">finger</span>
<pre style="white-space: pre-wrap;">
指纹识别
    以框架可能存在的文件进行检测识别；

使用例子：
    基础：
    python pscan.py finger -u http://ex.com
    全命令：
    python pscan.py finger -u http://ex.com -f cms_finger.txt -t 50 -ua "xxx" -c "xxx" -p 127.0.0.1:7890

指令描述：
usage: peach_scan finger [-h] [-u URL] [-f FILE] [-t THEARD] [-ua USERAGENT] [-c COOKIE] [-p PORXY]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标ip地址
  -f FILE, --file FILE  对指定文件中的url进行批量指纹识别
  -t THEARD, --theard THEARD
                        指定线程数
  -ua USERAGENT, --useragent USERAGENT
                        指定浏览器ua
  -c COOKIE, --cookie COOKIE
                        指定cookie
  -p PORXY, --porxy PORXY
                        设置代理
</pre>
## <span style="color: #03f8f8;">exp</span>
<pre style="white-space: pre-wrap;">
当前模块未完善，只有一个poc可使用，不建议进行使用。

使用例子：
    基础：
    
    全命令：
    

指令描述：
usage: peach_scan exp [-h] [-poc POC] [-s SEARCH] [-url URL] [-urlfile URLFILE] [-ip IP] [-ipfile IPFILE] [-user USER] [-pwd PWD] [-userfile USERFILE] [-passfile PASSFILE] [-dir DIR] [-cmd CMD]

options:
  -h, --help            show this help message and exit
  -poc POC              指定poc
  -s SEARCH, --search SEARCH
                        搜索poc
  -url URL              目标URL
  -urlfile URLFILE      URL集合文件
  -ip IP                目标IP
  -ipfile IPFILE        IP集合文件
  -user USER            登录账号
  -pwd PWD              登录密码
  -userfile USERFILE    账号字典
  -passfile PASSFILE    密码字典
  -dir DIR              目录
  -cmd CMD              命令
</pre>