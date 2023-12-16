from django.contrib import admin
from tabledata.models import tabledata
from tabledata.models import passoutdata
from tabledata.models import feedata
from tabledata.models import feetable

class tabledataAdmin(admin.ModelAdmin):
    list_display=('reg','name','fathername','mothername','phoneno','address','city','gender',
                   'course','btime','photo','fee','refee')

admin.site.register(tabledata,tabledataAdmin)

class passoutdataAdmin(admin.ModelAdmin):
    list_display=('reg','name','fathername','mothername','phoneno','address','city','gender',
                   'course','btime','photo','fee','refee')

admin.site.register(passoutdata,passoutdataAdmin)


class feedataAdmin(admin.ModelAdmin):
    list_display=('regno','fee','date')

admin.site.register(feedata,feedataAdmin)


class feetableAdmin(admin.ModelAdmin):
    list_display=('regno','rem','totalfee','fee','date')

admin.site.register(feetable,feetableAdmin)
