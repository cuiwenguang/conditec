from conditec.base.controller import BaseController
from demo.models.article import Category
from demo.forms.category import CategoryForm


class CategoryController(BaseController):
    queryset = Category.objects.all()
    model_form = CategoryForm
