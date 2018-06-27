from django.http import Http404, HttpResponseForbidden
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """捕获rest framework 错误异常，返回自定义的错误格式"""
    if isinstance(exc, Http404):
        exc = NotFound()
    elif isinstance(exc, HttpResponseForbidden):
        exc = PermissionDenied()
    response = exception_handler(exc=exc, context=context)
    if response and isinstance(response.data, dict):
        detail = response.data.pop('detail', None)
        if detail:
            response.data['error'] = detail
        if hasattr(exc, 'get_codes'):
            response.data['code'] = exc.get_codes()
    return response