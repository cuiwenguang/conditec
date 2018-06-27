from django.db import models


class Category(models.Model):
    """原料基础信息"""
    name = models.CharField(max_length=50)
    default_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    type = models.CharField(max_length=50, null=True, blank=True)
    state = models.IntegerField(default=1)

    class Meta:
        verbose_name = '品种分类'
        default_permissions = ()
        permissions = (
            ("category_list", "收购|品种管理"),
            ("post_category", "收购|品种编辑"),
            ("delete_category", "收购|删除品种"),
        )
