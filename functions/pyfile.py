import os
from proxy_validate import validate
from utils import report
from utils import color

allocate_http = []
allocate_https = []
allocate_socks5 = []
allocate_socks4 = []
data = []


class TextFileReader:
    def __init__(self, file_path_to):
        self.file_path = file_path_to

    def read_file(self):
        try:
            if os.path.isfile(self.file_path):
                with open(self.file_path, 'r') as file:
                    content = file.readlines()
                    return content
            else:
                print("File does not exist.")
        except:
            print("Error occurred while reading the file.")


# Example usage

def decide_protocol(content):
    global allocate_http
    global allocate_https
    global allocate_socks5
    global allocate_socks4
    global data
    pynum = 0
    for line in content:
        stripped = line.strip()
        lower_key = stripped.lower()
        predefined = lower_key.split('://')[0]

        if predefined == 'socks5':
            allocate_socks5.append(lower_key)
        elif predefined == 'socks4':
            allocate_socks4.append(lower_key)
        elif predefined == 'http':
            allocate_http.append(lower_key)
        elif predefined == 'https':
            allocate_https.append(lower_key)
        else:
            print("Undefined Value has found", lower_key)

    fetch_total = len(allocate_http) + len(allocate_socks5) + len(allocate_socks4) + len(allocate_https)
    print(color.colorize_text("Number of Proxies are gathered : ", color.g_color), fetch_total, "\n")
    for i in range(len(allocate_http)):
        pynum = pynum + 1
        print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", allocate_http[i])
        if (validate.test_http(allocate_http[i])) == 200:
            print(allocate_http[i], color.colorize_text(" is valid \n", color.g_color))
            data.append(allocate_http[i])
        else:
            print(color.colorize_text(" * Connection is not valid \n", color.r_color))

    for i in range(len(allocate_socks4)):
        pynum = pynum + 1
        print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", allocate_socks4[i])
        if (validate.test_protocol4(allocate_socks4[i])) == 200:
            print(allocate_socks4[i], color.colorize_text(" is valid \n", color.g_color))
            data.append(allocate_socks4[i])
        else:
            print(color.colorize_text(" * Connection is not valid \n", color.r_color))

    for i in range(len(allocate_socks5)):
        pynum = pynum + 1
        print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", allocate_socks5[i])
        if (validate.test_http(allocate_socks5[i])) == 200:
            print(allocate_socks5[i], color.colorize_text(" is valid \n", color.g_color))
            data.append(allocate_socks5[i])
        else:
            print(color.colorize_text(" * Connection is not valid \n", color.r_color))

    for i in range(len(allocate_https)):
        pynum = pynum + 1
        print(color.colorize_text("Testing Connection :", color.y_color), pynum, "  ", allocate_https[i])
        if (validate.test_http(allocate_https[i])) == 200:
            print(allocate_https[i], color.colorize_text(" is valid \n", color.g_color))
            data.append(allocate_https[i])
        else:
            print(color.colorize_text(" * Connection is not valid \n", color.r_color))
    return data


def test_all(path_to_move):
    file_path = path_to_move  # Update with the correct file path
    file_reader = TextFileReader(file_path)
    file_content = file_reader.read_file()
    data_list = decide_protocol(file_content)
    # Access the arrays
    if len(data_list) > 0:
        print("Valid Proxies : ")
        for proxy in data_list:
            print(proxy)
        report.value_pars(data_list)
    else:
        print(color.colorize_text(
            "Please check your proxy list, It couldn't find any valid proxy, also problem may occur because of "
            "response time", color.r_color))
