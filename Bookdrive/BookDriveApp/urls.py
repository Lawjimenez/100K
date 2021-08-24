from django.urls import path
from . import views

urlpatterns = [ 
	path('', views.home, name='home'),
	path('Donor/', views.Donor, name='Donor'),
	path('benif/', views.benif, name='benif'),
	path('Table/', views.List, name='List'),
	path('Grantee/', views.Grantee, name='Grantee'),
	path('update/<str:pk>/', views.update, name='update'),	
	path('updatee/<str:pk>/', views.updatee, name='updatee'),
	path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
	]
