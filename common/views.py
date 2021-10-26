from django.contrib.auth import authenticate, login    # authenticate : 사용자명과 비밀번호 정확한지 검증하는 함수 (사용자 인증)
# django.contrib.auth 모듈의 authenticate : 사용자 인증 / login : 로그인 담당
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":       # POST 요청이면 화면에서 입력한 데이터로 사용자 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # form.cleaned_data.get : 입력값을 개별적으로 얻고 싶은 경우 사용(사용자명, 비밀번호)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인   # 신규 사용자를 생성한 후 자동 로그인 (authenticate, login 함수 사용)
            return redirect('index')
    else:     # GET 요청이면 계정생성 화면을 리턴
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
