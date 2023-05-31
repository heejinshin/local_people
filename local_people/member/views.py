from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.

#회원가입 ; 등록 

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
    

# 로그인 ; LOGIN
def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')  
    
    elif request.method == "POST":
        username = request.POST['username']  #form의 name
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('board:list'))
        
        else:
            return render(request, '/index.html')
        
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")

cur.execute("SELECT * FROM PhoneBook;")
for row in cur:
    print(row)
