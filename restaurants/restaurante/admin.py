from django.contrib import admin
from .models import Slider
from .models import Post_Detail
from .models import Post_Title
from .models import Product
from .models import About_Page
from .models import Commenter_Name
from .models import Our_Customers
from .models import Send_Message

admin.site.register(Slider)
admin.site.register(Post_Title)
admin.site.register(Post_Detail)
admin.site.register(Product)
admin.site.register(About_Page)
admin.site.register(Commenter_Name)
admin.site.register(Our_Customers)
admin.site.register(Send_Message)