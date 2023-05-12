import socks
import requests
import socket


class Socks4Validate:
    def __init__(self, proxy_ip, proxy_port):
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port

    def make_request(self, url):
        try:
            socks.set_default_proxy(socks.SOCKS4, self.proxy_ip, self.proxy_port)
            socket.socket = socks.socksocket

            response = requests.get(url)
            return response
        except:
            pass
        return None

    def request_with_proxy(self, url):
        response = self.make_request(url)
        if response:
            return response.status_code
        else:
            return None

