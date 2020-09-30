from django.utils.deprecation import MiddlewareMixin

FORBIDDEN_URLS = ['admin', 'redoc']


class IPForbiddenMiddleWare(MiddlewareMixin):
    """
    限制只有内网才可以访问django admin 后台 和 api文档
    """
    @staticmethod
    def process_request(request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if request.path.split('/')[1] in FORBIDDEN_URLS and ip.startswith('192.'):
            raise PermissionError
