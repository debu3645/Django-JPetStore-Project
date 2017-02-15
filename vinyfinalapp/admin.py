from django.contrib import admin
from .models import vinyusers , vinyproducts , vinyitems, vinyaddcart
# Register your models here.

admin.site.register(vinyusers)
admin.site.register(vinyproducts)
admin.site.register(vinyitems)
admin.site.register(vinyaddcart)