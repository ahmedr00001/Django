from django.contrib import admin
from .models import Product , Test

#register your model here


admin.site.register(Product)
admin.site.register(Test)

admin.site.site_header = '  حمدي عمك '