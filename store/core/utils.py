import requests

def get_request_ip(request) -> str:
    """Get the IP address of the request"""
    ip = request.session.get('ip', None)
    if not ip:
        x_forward_for= request.META.get('HTTP_X_FORWARDED_FOR', None)
        if x_forward_for:
            ip = x_forward_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', '')
    return ip

def get_ip_info(ip:str)->dict:
    url = f'http://ip-api.ir/info/{ip}'
    response = requests.get(url)
    print('response: ', response.text)
    if not response: 
        return {}
    return response.json()