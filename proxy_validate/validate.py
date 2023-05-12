from . import socks5_method
from . import socks4_method
from . import http_method


def unpack_url(url):
    # Remove the protocol part (e.g., "socks5://")
    url_without_protocol = url.split("://")[1]

    # Split the remaining URL at the colon (":") to get the IP and port
    ip, port = url_without_protocol.split(":")
    port = int(port)  # Convert port to integer
    return ip, port


def test_protocol5(url):
    ip, port = unpack_url(url)
    socks5_validator = socks5_method.Socks5Validate(ip, port)
    response_code = socks5_validator.request_with_proxy("https://dns.google/")
    return response_code


def test_protocol4(url):
    ip, port = unpack_url(url)
    socks4_validator = socks4_method.Socks4Validate(ip, port)
    response_code = socks4_validator.request_with_proxy("https://dns.google/")
    return response_code


def test_http(url):
    ip, port = unpack_url(url)
    http_validator = http_method.HttpValidate(ip, port)
    response_code = http_validator.request_with_proxy("https://dns.google/")
    return response_code


"""print("this is validate file")
if test_protocol5("socks5://ip:port") == 200:
    print("SOCKS5 proxy is working")
else:
    print("SOCKS5 proxy is not working")
"""
