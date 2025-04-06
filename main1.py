import requests
import requests
from requests.exceptions import RequestException

def create_vpn_session(proxy_host="107.152.98.5", proxy_port="4145"):
    session = requests.Session()
    proxies = {
        'http': f'socks5://{proxy_host}:{proxy_port}',
        'https': f'socks5://{proxy_host}:{proxy_port}'
    }
    session.proxies.update(proxies)
    return session

def send_request(session=None):
    try:
        if session:
            response = session.get("https://httpbin.org/ip", timeout=10)
        else:
            response = requests.get("https://httpbin.org/ip", timeout=10)
        print(response.json())
    except RequestException as e:
        print(f"Request failed: {e}")

# Test without VPN
print("Without VPN:")
send_request()

# Test with VPN
print("\nWith VPN:")
vpn_session = create_vpn_session()
send_request(vpn_session)

# Test after VPN
print("\nAfter VPN (new session):")
send_request()