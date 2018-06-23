import json
from django.http import Http404
from django.views.generic.base import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q


class BaseController(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.http_method_names = ['get', 'post', 'put', 'delete']
        self.render = render
        queryset = None
        model_form = None

    def dispatch(self, request, *args, **kwargs):
        try:
            action = kwargs["action"]
        except:
            action = None
        if action is None:
            method = request.method.lower()
            if method not in self.http_method_names:
                raise Exception("不支持的请求方式")
            handler = getattr(self, method)
        else:
            try:
                handler = getattr(self, action)
            except NotImplemented:
                return Http404("没有实现")
        return handler()

    def json(self, code, data={}, message=None):
        return JsonResponse({
            "code": code,
            "data": data,
            "message": message
        })

    def get(self):
        if self.queryset is None:
            raise Exception("没有指定model")
        pk = self.kwargs["id"]
        if pk is None:
            query_params = Q()
            for k, v in self.request.GET.items():
                q = {}
                q[k] = v
                query_params.add(Q(**q), Q.AND)
            items = self.queryset.filter(query_params).values()
            data = [d for d in items]
        else:
            data = self.queryset.filter(id=pk).values()[0]
        return self.json(200, data)

    def post(self):
        json_data = json.loads(self.request.body)
        form = self.model_form(json_data)
        if form.is_valid():
            instance = form.save(commit=False)
            if self.kwargs["id"] is not None:
                instance.id = self.kwargs["id"]
            instance.save()
            return self.json(200, message='success')
        else:
            return self.json(401, message=form.errors.as_json())

    def delete(self):
        pk = self.kwargs['id']
        self.queryset.get(id=pk).delete()
        return self.json(200, message='success')

