from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from member.models import User

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

def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'users/register.html')

    elif request.method == "POST":
        username = request.POST.get['username',None]   #딕셔너리형태
        password = request.POST.get['password',None]
        re_password = request.POST.get['re_password',None]
        res_data = {} 
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password= make_password(password))
            user.save()
        return render(request, 'users/register.html', res_data) #register를 요청받으면 register.html 로 응답.