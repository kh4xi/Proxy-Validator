import json
import requests
from proxy_validate import validate
from utils import report
from utils import color


class UrlParse:
    def __init__(self, page=1, protocols=""):
        self.base_url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page="
        self.page = page  # Default is 1
        self.sort_by = "&sort_by=lastChecked&"
        self.sort_type = "sort_type=desc&protocols="
        self.protocols = protocols
        print("Selected Protocols : ", self.protocols, "\n")

    def get_proxy_list(self):
        # Make Request
        # Store the json
        http_storage = []
        https_storage = []
        socks4_storage = []
        socks5_storage = []
        # Store the json

        for thread in range(1, self.page + 1):
            response = requests.get(
                self.base_url + str(thread) + self.sort_by + self.sort_type + self.protocols)
            formatter = json.loads(response.text)
            data_table = formatter['data']
            # Make Request
            for i in data_table:
                if i['protocols'][0] == 'socks5':
                    socks5_storage.append(i['protocols'][0] + '://' + i['ip'] + ':' + i['port'])
                elif i['protocols'][0] == 'socks4':
                    socks4_storage.append(i['protocols'][0] + '://' + i['ip'] + ':' + i['port'])
                elif i['protocols'][0] == 'http':
                    http_storage.append(i['protocols'][0] + '://' + i['ip'] + ':' + i['port'])
                else:
                    https_storage.append(i['protocols'][0] + '://' + i['ip'] + ':' + i['port'])

        fetched_data = len(http_storage) + len(https_storage) + len(socks4_storage) + len(socks5_storage)
        print(color.colorize_text("Total number of fetched proxy :", color.g_color), fetched_data, "\n")

        return socks5_storage, socks4_storage, http_storage, https_storage

    def print_proxy_list(self):
        socks5_storage, socks4_storage, http_storage, https_storage = self.get_proxy_list()

        all_storage = []
        pynum = 0
        for i in range(len(socks5_storage)):
            pynum = pynum + 1
            print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", socks5_storage[i])
            if (validate.test_protocol5(socks5_storage[i])) == 200:
                print(socks5_storage[i], color.colorize_text(" is valid \n", color.g_color))
                all_storage.append(socks5_storage[i])
            else:
                print(color.colorize_text(" * Connection is not valid \n", color.r_color))

        for i in range(len(socks4_storage)):
            pynum = pynum + 1
            print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", socks4_storage[i])
            if (validate.test_protocol4(socks4_storage[i])) == 200:
                print(socks4_storage[i], color.colorize_text(" is valid \n", color.g_color))
                all_storage.append(socks4_storage[i])
            else:
                print(color.colorize_text(" * Connection is not valid \n", color.r_color))

        for i in range(len(http_storage)):
            pynum = pynum + 1
            print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", http_storage[i])
            if (validate.test_http(http_storage[i])) == 200:
                print(http_storage[i], color.colorize_text(" is valid \n", color.g_color))
                all_storage.append(http_storage[i])
            else:
                print(color.colorize_text(" * Connection is not valid \n", color.r_color))

        for i in range(len(https_storage)):
            pynum = pynum + 1
            print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", https_storage[i])
            if (validate.test_http(https_storage[i])) == 200:
                print(http_storage[i], color.colorize_text(" is valid \n", color.g_color))
                all_storage.append(https_storage[i])
            else:
                print(color.colorize_text(" * Connection is not valid \n", color.r_color))

        print("Summarizing.. All the valid connections :")
        report.value_pars(list(all_storage))
        for i in range(len(all_storage)):
            print(all_storage[i])

        """
          print("Socks5 Proxies:")
           print(socks5_storage)
           print("")

           print("Socks4 Proxies:")
           print(socks4_storage)
           print("")

           print("HTTP Proxies:")
           print(http_storage)
           print("")

           print("HTTPS Proxies:")
           print(https_storage)
"""


"""# Create an instance of UrlParse
url_parse = UrlParse(1, "socks4")

# Call the print_proxy_list method
url_parse.print_proxy_list()
"""
