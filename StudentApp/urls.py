from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.log_fun,name='log'), #it will dispaly login.html page
    path('logdata',views.logdata_fun), #it will read data and verify as superuser
                                        #and redirect to home.html page
    path('reg',views.reg_fun,name='reg'), #it will redirect to register.html page

    path('regdata',views.regdata_fun), #it will create a superuser account

    path('home',views.home_fun,name='home'), #it will redirect to home.html

    path('add_students',views.addstudent_fun,name='add'), #it will redirect to addstudent.html

    path('readdata',views.readdata_fun), #it will insert record into student table

    path('display',views.display_fun,name='display'), #it will display the student table data in display.html file

    path('update/<int:id>',views.update_fun,name='update'), #it will update the student record

    path('delete/<int:id>',views.delete_fun,name='del'), #it will delete the record from student table

    path('log_out',views.log_out_fun,name='log_out'),

]