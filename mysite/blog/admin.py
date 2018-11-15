from django.contrib import admin
from  .models import bloginfo
from  .models import product
from .models import card

admin.site.register(bloginfo)
admin.site.register(product)
admin.site.register(card)