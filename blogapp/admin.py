from django.contrib import admin
from .models import register,logindata,resetpassword,profiledata,correctpassword,profilepicture,postitem,commentdata

admin.site.register(register)
admin.site.register(logindata)
admin.site.register(resetpassword)
admin.site.register(profiledata)
admin.site.register(correctpassword)
admin.site.register(profilepicture)
admin.site.register(postitem)
admin.site.register(commentdata)


