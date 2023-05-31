from django.shortcuts import render,redirect
from models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # 사용자가 입력한 PW와 실제 PW의 비교 
        if request.POST['password1'] == request.POST["password2"]:
            user = User.objects.create_user(
                  username = request.POST['username'],
                password = request.POST['password1'],
                email = request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')