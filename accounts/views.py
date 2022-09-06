from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
#accounts App - urls.py에서 설정한 signup을 views.py에서구현
# def signup(request): #회원가입 누르면 GET방식으로 views.py에 들어옴
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST) #form에서 UserCreationForm()을 받아 signup.html로 넘겨줌 회원가입 기입 후 버튼 누르면 POST형식으로 데이터 받아
#         if form.is_valid(): #is_valid 통해 로직 오류 확인 후 없으면 db저장 후 리다이렉트
#             form.save()
#             return redirect('')
#     else:
#         form = UserCreationForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'accounts/signup.html', context)

#회원가입
def signup(request):
    if request.method == 'POST': #값이 넘겨졌을 경우
        if request.POST('password1')==request.POST('password2'): #비번1, 2 입력값이 같다면
            user = User.objects.create_user( #user객체를 새로 생성 (create_user함수 이용 유저 생성)
                username=request.POST('username'), password=request.POST('password1')
            )
            return redirect('/')
    return render(request, 'signup.html') #password1 != 2 인 경우 

def login(request):
    if request.method == 'POST': #login.html에서 넘어온 username과 password를 각 변수에 저장
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #authenticate함수 self, username, password를 인자로 받은 후 정상적 인증된 경우 user객체 하나반환.없으면 None
        #해당 username과 password와 일치하는 user객체를 가짐
        #해당 user객체가 존재한다면 
        if user is not None:
            auth.login(request, user) #세션에 로그인 정보 생성&저장
            return redirect('/')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')