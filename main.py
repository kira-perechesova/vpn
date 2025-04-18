import os
import requests

def enable_vpn(proxy_host="77.43.230.22", proxy_port="7788"):
    os.environ["HTTP_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"
    os.environ["HTTPS_PROXY"] = f"socks5h://{proxy_host}:{proxy_port}"

def disable_vpn():
    os.environ.pop("HTTP_PROXY", None)
    os.environ.pop("HTTPS_PROXY", None)

def send_request():
    response = requests.get("https://httpbin.org/ip", timeout=30)
    print(response.json())

send_request()
enable_vpn()
send_request()
disable_vpn()
send_request()