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
      LastName = request.POST['LastName']
      Email = request.POST['Email']
      Password = request.POST['Password']
      ConfirmPasword = request.POST['ConfirmPassword']
      DateOfBirth = request.POST['DateOfBirth']
      PhoneNumber = request.POST['PhoneNumber']
     # print(name, email, phone, desc)
      RegistrationPage = RegistrationPage(FirstName=FirstName, LastName=LastName, Email=Email, Password=Password, ConfirmPasword=ConfirmPasword, DateOfBirth=DateOfBirth,  PhoneNumber= PhoneNumber)
      RegistrationPage.save()
      print("The data has been written to the db")
      return render(request, 'RegistrationPage.html')

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