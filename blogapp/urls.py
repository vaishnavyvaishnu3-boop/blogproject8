from django.urls import path
from .import views


urlpatterns=[
   path('',views.secondpace,name='seconds'),
   path('logins',views.login,name='logged'),
   path('register/',views.registration,name='registered'),
   path('forgot/',views.forgot_password,name='newlypassword'),
   path('profiled/',views.create_profile,name='profile'),
   path('forgotten/',views.create_new_password,name='newerpassword'),
   path('profilelist/',views.profile_shortlist,name='profileslist'),
   path('entireprofile/<int:Profiledata_id>/',views.profile_detaillist,name='fullprofile'),
   path('updated/<int:Profiledata_id>/',views.update_profile,name='updates'),
   path('profils/',views.profile_image,name='picture'),
   path('pics/',views.home_image,name='galleries'),
   path('blog/',views.post_blog,name='createblog'),
   path('see_blog/',views.see_blog,name='see'),
   path('blogupdate/<int:Postitem_id>/',views.update_blog,name='updating'),
   path('blogdelete/<int:Postitem_id>/',views.delete_blog,name='deleted'),
   path('searchblog/',views.search_blog,name='searches'),
   path('searchedblog/',views.search_title,name='searchd'),
   path('commented/',views.createcomment,name='commenting'),
   path('viewcommented/',views.viewcomment,name='commenter'),
   path('eachcomment/<int:Commentdata_id>/',views.view_each_comment,name='eachcomments'),
   path('updatecommented/<int:Commentdata_id>/',views.update_comment,name='updatedcomment'),
   path('deletecommented/<int:Commentdata_id>/',views.delete_comment,name='deletedcomment'),







]