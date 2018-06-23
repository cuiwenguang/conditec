from django.db import models


class ViewArticle(models.Model):
    title = models.CharField(max_length=50)
    contenets = models.TextField(max_length=100)
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'view_article'
        managed = False