from rest_framework import serializers, viewsets
from raw.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'default_price', 'type',)



class CategoryApi(viewsets.ModelViewSet):
    """
    收购品种接口
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


