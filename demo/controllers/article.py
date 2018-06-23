from django.core import serializers
from conditec.base.controller import BaseController


class ArticleController(BaseController):
    def index(self):
        return self.render(self.request, 'index.html', {"title": "xx"})

    def add(self):
        return self.json(200, {"title": "xxxx"}, "ok")

    def get_all(self):
        from demo.models import ViewArticle
        result = ViewArticle.objects.all().values()
        return self.json(200, result)

