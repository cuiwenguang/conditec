from django import forms

from demo.models.article import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=20, min_length=2)

    class Meta:
        model = Category
        fields = ['id', 'name']
