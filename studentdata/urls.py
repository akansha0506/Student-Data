
from django.contrib import admin
from django.urls import path
from studentdata import view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('registration/',view.registration),

    path('view/',view.view),
    path('viewall/',view.viewall),
    path('viewbybatchtime/',view.viewbybatchtime),
    path('viewbybatchtime1/<str:btime1>',view.viewbybatchtime1),
    path('viewbyregno/',view.viewbyregno),
    path('viewbyregno1/<str:regno>',view.viewbyregno1),
    path('viewbyname/',view.viewbyname),
    path('viewbyname1/<str:fname>',view.viewbyname1),

    path('delete/',view.delete),

    path('update/',view.update),
    path('update1/<str:fupdate>',view.update1),

    path('fees/',view.fees),
    path('submitfee/',view.submitfee),
    path('submitdata/<str:fregno>',view.submitdata),
    path('viewfee/',view.viewfee),
    path('viewfee1/<str:fregno>',view.viewfee1),
    
    path('passout/',view.passout),
]



