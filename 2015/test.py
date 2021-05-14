import json

data = ""
with open('input.txt') as json_f:
  data = json.load(json_f)

# print(data['ips'][1].get('ip', {}).get('ip', ''))


def extract_ip(host: dict, ip_type: str, ip_version: int) -> str:
    def filter_ip_version(x: dict) -> bool:
        return x.get('ip', {}).get('version', None) == ip_version

    def filter_type(x: dict) -> bool:
        return x.get('type', None) == ip_type

    def filter_primary(x: dict) -> bool:
        return x.get('primary', 0) == 1

    filters1 = (filter_ip_version, filter_primary, filter_type)
    filters2 = (filter_ip_version, filter_type)

    arr = []

    # for item in filter(lambda x: all([f(x) for f in filters1]), host.get('ips', [])):
    #     return item.get('ip', {}).get('ip', '').lower()

    for item in filter(lambda x: all([f(x) for f in filters2]), host.get('ips', [])):
        arr.append(item.get('ip', {}).get('ip', '').lower())
    return arr

def extract_ips(host: dict, ip_type: str, ip_version: int) -> list:
    def filter_ip_version(x: dict) -> bool:
        return x.get('ip', {}).get('version', None) == ip_version

    def filter_type(x: dict) -> bool:
        return x.get('type', None) == ip_type

    filters = (filter_ip_version, filter_type)

    ips = []
    for item in filter(lambda x: all([f(x) for f in filters]), host.get('ips', [])):
        ips.append(item.get('ip', {}).get('ip', '').lower())

    return ips if len(ips) > 0 else []


exit = extract_ips(data['containers'][0], 'exit', 4)
print(exit)