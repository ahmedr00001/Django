from django.shortcuts import render
from .models import Login
from .form import LoginForm ,LoginForm3  #to access form


# Create your views here.


##first way
def forms (request) :
    #request get all info from form so
    x = request.POST.get('username')
    # print (x) #to make sure
    y = request.POST.get('password')

    #to store in database first import model
    data = Login(username = x , password = y)
    # data.save()

    users = Login.objects.all()
    users_num = Login.objects.all().count()

    return render(request ,'forms/forms.html' , {'users' :users , 'users_num' : users_num})

####################################
##second way using LoginForm in form.py
def forms2 (request) :
    #request get all info from form so
    x = request.POST.get('username')
    # print (x) #to make sure
    y = request.POST.get('password')

    #to store in database first import model
    data = Login(username = x , password = y)
    data.save()

    users = Login.objects.all()
    users_num = Login.objects.all().count()

    return render(request ,'forms/forms2.html' , {'my_form' : LoginForm,'users' :users , 'users_num' : users_num})

 
#third way using Login in form.py
def forms3 (request) :

    if request.method == 'POST':  #for security and to save issue of  page
        dataform =LoginForm3(request.POST)  #just this line to save to database
        if dataform.is_valid():    #security of database
            dataform.save()


    users = Login.objects.all()
    users_num = Login.objects.all().count()

    return render(request ,'forms/forms3.html' , {'my_form' : LoginForm3,'users' :users , 'users_num' : users_num})
