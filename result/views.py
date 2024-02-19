from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        rollnumber = request.POST['Rollnumber']
        name = request.POST['Name']

        try:
            user = User.objects.get(Rollnumber=rollnumber, Name=name)
            # User authentication successful, redirect to success page
            return redirect('success', rollnumber=rollnumber)
        except User.DoesNotExist:
            messages.error(request, 'Invalid Name or Rollnumber!')

    return render(request, 'login.html')

def success(request, rollnumber):
    try:
        user = User.objects.get(Rollnumber=rollnumber)
        return render(request, 'success.html', {'user': user})
    except User.DoesNotExist:
        error_message = 'User not found.'
        return render(request, 'login.html', {'error_message': error_message})
