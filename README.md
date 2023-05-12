# Proxy-Validator
Automatic Proxy validation tool. You can choose to use --auto function to
get the list of the proxies by itself or you can use the --validate function
to test your proxy list integrity.
note that currently not supports user:pass login

supported protocols's are HTTP, HTTPS, SOCKS5, SOCKS4

#### MIT License 
### Installing dependencies

`pip install -r requirements.txt`


### Show Help
`python proxy-valid.py --help`

## Automatically Fetch Data and validate
`python proxy-valid.py --auto all`

or you can specify protocols like

`python proxy-valid.py --auto https,socks5`

you can increase the number of proxies with level command

`python proxy-valid.py --auto all --level 2`

each level is 500 proxy so 2 will be 1000 in total

## Validate your proxy list
`python proxy-valid.py --validate /User/Desktop/example.txt or exanple.txt`

### Check for updates
`python proxy-valid.py --update check`

### Example Proxy List
`http://ip:port`
`https://ip:port`
`socks5://ip:port`
`socks4://ip:port`


