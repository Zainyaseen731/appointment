from django.contrib import admin
from .models import Post
from .models1 import Appointment,AppointmentTimeSlot
#admin.site.register(Post)
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields=[
        'title',
        'user_name',
        'slug',
        'email',
        'phone',
        'publish', 
        'publish_date',
        'updated','timestemp','age'
        
    ]
    readonly_fields=['updated','timestemp','age']

    def age(self,obj,*args,**kwargs):
        return str(obj.age())

    class Meta:
        model=Post


class AppointmentTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('appointment_day','appointment_time')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','note','date','time','status')




#class AppointmenttAdmin(admin.ModelAdmin):
 #   fields = [
  #      'first_name',
   #     'last_name',
    #    'email',
     #   'note',
      #  'date',
       # 'time',
    #]

    #class Meta:
     #   model = Appointment


admin.site.register(Post,PostAdmin)
admin.site.register(Appointment,AppointmentAdmin)
#admin.site.register(AppointmenttAdmin)
admin.site.register(AppointmentTimeSlot,AppointmentTimeSlotAdmin)