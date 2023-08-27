from .utils import *
from django.http import HttpResponse
from config import settings

class RestrictCountryIpMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        ip = get_request_ip(request)
        if self._check_restriction(ip,request):
            return HttpResponse('You are not allowed to access this site', status=403)
        request.session['ip'] = ip
        response = self.get_response(request)
        return response

    def _check_restriction(self, ip, request) -> bool:
        code = request.session.get('countryCode', None)
        if not code: 
            ip_info = get_ip_info(ip)
            code = ip_info.get('countryCode', None)
        request.session['countryCode'] = code
        if code and code in self._get_restricted_countries():
            return True
        return False

    def _get_restricted_countries(self) ->list:
        return settings.RESTRICTED_COUNTRY_CODES or []