from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
