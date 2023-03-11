from django.contrib import admin

# Register your models here.

class SensorAdmin(admin.ModelAdmin):
    list_display = ['category_name','sensor_type', 'sensor_symbol', 'sensor_price']

class InductiveAdmin(admin.ModelAdmin):
    list_display = ['category','type','name','url','url_img','price','stock','manufacturer',
                    'flush','spec','housing','connection','size','material','IP','output_structure',
                    'voltage','output_type','adjust','distance','indicator','temperature']



from .models import Sensors, Inductive
admin.site.register(Sensors, SensorAdmin)
admin.site.register(Inductive, InductiveAdmin)
