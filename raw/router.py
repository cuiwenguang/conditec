from raw.api import category

routers = [
    (r'raw/category/', category.CategoryApi),
]