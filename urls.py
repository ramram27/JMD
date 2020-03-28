from django.conf.urls import url
from Gateapp import views

urlpatterns = [
       url('view-Person',views.viewPerson),
       url('add',views.add),
       url('New-Person',views.NewPerson),
       url('edit-Person',views.editPerson),
       url('delete-Person',views.deletePerson),
       url('Search-Person',views.SearchPerson),
       url('Search',views.search),
      
       url('edit',views.edit),
       url('login',views.userLogin),
       url('logout',views.userLogout),

]
