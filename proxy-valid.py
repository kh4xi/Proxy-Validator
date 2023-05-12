import argparse
import auto_list
import datetime
import pyfile
import utils.report
from utils import report

print('''
             
  ____                         __     __    _ _     _       _             
 |  _ \ _ __ _____  ___   _    \ \   / __ _| (_) __| | __ _| |_ ___  _ __ 
 | |_) | '__/ _ \ \/ | | | |____\ \ / / _` | | |/ _` |/ _` | __/ _ \| '__|
 |  __/| | | (_) >  <| |_| |_____\ V | (_| | | | (_| | (_| | || (_) | |   
 |_|   |_|  \___/_/\_\\__, |      \_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|   
                      |___/                                                                                                                                  
github.com/kh4xi  
        
Usage : proxy-valid.py --help 
        proxy-valid.py --auto all or --auto https,socks5...  
        proxy-valid.py --auto all --level 2 (Default is 1 / 1 means 500 max)    
        proxy-valid.py --validate User/Desktop/proxy.txt      
        Supported Methods (Socks5, Socks4, Http, Https)    
        
        __version__ = '1.0'                                          
''')


current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Create the argument parser object
parser = argparse.ArgumentParser(description='Automatic Proxy Validation and Collector')

# Options
parser.add_argument('-a', '--auto', type=str,
                    help='proxy-valid.py --auto all or --auto https,http / Automatically gather '
                         'proxies from online source and validate them ')
parser.add_argument('-v', '--validate', type=str, help='proxy-valid.py --validate proxylist.txt / Validating of their '
                                                       'responses ')
parser.add_argument('-l', '--level', type=int,
                    help='proxy-valid.py --auto all --level 1 / Level 1 is 500 Proxy from List, '
                         'Each Level increases the number, It should Max 10')

# Parse the command-line arguments
args = parser.parse_args()
level = int(args.level) if args.level else 1

if args.validate:
    pyfile.test_all(args.validate)

if args.auto:
    protocols = args.auto.split(',')
    if protocols == ["all"]:
        protocols = "socks5,socks4,http,https"
    else:
        protocols = ",".join(protocols)
    print(formatted_time, "\n")
    url_parse = auto_list.UrlParse(level, protocols)
    url_parse.print_proxy_list()



