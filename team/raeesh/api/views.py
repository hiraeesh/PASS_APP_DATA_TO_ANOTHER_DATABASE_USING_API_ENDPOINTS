from django.shortcuts import render
from django.http import HttpResponse
from .forms import Stu
import requests
import json


URL= "http://127.0.0.1:8000/api/crud/"

# Create your views here.
def rabiya(request):
    if request.method == 'POST':
        fm=Stu(request.POST)
        if fm.is_valid():
            uid =fm.cleaned_data['id']
            uname =fm.cleaned_data['name']
            uemail =fm.cleaned_data['email']
            upassword =fm.cleaned_data['password']

            
            data={
           'id':uid,
           'name':uname,
           'email':uemail,
           'password':upassword
           
            }
            headers = {'content-Type':'application/json'}
            json_data = json.dumps(data)
            print(json_data)
            r = requests.post(url = URL, headers=headers, data = json_data)
            raeesh= r.json()
            print(raeesh)
            print(data)
            return HttpResponse("<h1>data insert</h1>")

        

    else:
        fm=Stu()
        return render(request,'home.html',{'form':fm})

      

                

      
        # data={
        # 'name':name,
        # 'roll': roll,
        # 'city': city
        # }

    
    

  
      

        



