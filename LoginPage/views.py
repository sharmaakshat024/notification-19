from django.shortcuts import render, HttpResponse

# Create your views here.
def LoginPage(request):
   # return HttpResponse('Here is the login page')
   context = {'name': 'Aksh', 'course': 'Django'}
   return render(request, 'LoginPage.html', context)

def RegistrationPage(request):
   # return HttpResponse('Here is the Registraion page')
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