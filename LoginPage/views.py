from django.shortcuts import render, HttpResponse
from LoginPage.models import RegistrationPage
# Create your views here.
def LoginPage(request):

   # return HttpResponse('Here is the login page')
   
   return render(request, 'LoginPage.html')

def registrationPage(request):
   # return HttpResponse('Here is the Registraion page')
   if request.method=="POST":
     
      FirstName = request.POST['FirstName']
      lastName = request.POST['lastName']
      email = request.POST['email']
      password = request.POST['password']
      confirmpassword = request.POST['password']
      birthDate = request.POST['birthDate']
      phoneNumber = request.POST['phoneNumber']
      print(FirstName,lastName,email,password,confirmpassword,birthDate,phoneNumber)
      ins = RegistrationPage(FirstName=FirstName, lastName=lastName, email=email, password=password, confirmpassword=password, birthDate=birthDate,  phoneNumber= phoneNumber)
      ins.save()
      context = {'success': True}
      #RegistrationPage = RegistrationPage(FirstName=FirstName, lastName=lastName, email=email, password=password, confirmpassword=password, birthDate=birthDate,  phoneNumber= phoneNumber)
      #RegistrationPage.save()
      #print("The data has been written to the db")
   return render(request, 'RegistrationPage.html', context)

def SelfTest(request):
   # return HttpResponse('Here is the Registraion page')
      return render(request, 'SelfTest.html')

def Home(request):
   # return HttpResponse('Here is the Home page')
      return render(request, 'Home.html')

def DataAnalysis(request):
   # return HttpResponse('Here is the DataAnalysis page')
      return render(request, 'DataAnalysis.html')

def ContactAs(request):
   # return HttpResponse('Here is the ContactAs page')
      return render(request, 'ContactAs.html')