import json

from conditec.base.controller import BaseController
from demo.models.blog import Blog


class BlogController(BaseController):

    def init(self):
        self.model_class = Blog

    def create(self):
        post_data = json.loads(self.request.body)
        blog = Blog(**post_data)
        blog.save()
        return self.json(200)


