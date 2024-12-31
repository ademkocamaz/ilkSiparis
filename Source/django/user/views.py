from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import ProfileForm, ResetPasswordForm


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Oturum açıldı.")
            messages.add_message(request, messages.INFO, username + " Hoşgeldiniz.")
            return redirect("index")
        else:
            messages.add_message(
                request, messages.ERROR, "Kullanıcı adı veya Parola yanlış"
            )

    return render(request, "login.html")

@login_required(login_url="/user/login/")
def logout(request):
    if request.method == "POST":
        username = request.user.username
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturumunuz kapatıldı.")
    return redirect("index")


@login_required(login_url="/user/login/")
def profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request, messages.INFO, "Kullanıcı bilgileri güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Kullanıcı bilgileri güncellenirken bir hata oluştu.",
            )

    profile_form = ProfileForm(instance=request.user)
    context = {
        "profile_form": profile_form,
    }
    return render(request, "profile.html", context)


@login_required(login_url="/user/login/")
def reset_password(request):
    if request.method == "POST":
        reset_password_form = ResetPasswordForm(request.user, request.POST)
        if reset_password_form.is_valid():
            reset_password_form.save()
            messages.add_message(
                request, messages.INFO, "Şifreniz başarıyla değiştirildi."
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Şifreniz değiştirilirken hata oluştu."
            )
            for error in list(reset_password_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
    reset_password_form = ResetPasswordForm(request.user)
    context = {"reset_password_form": reset_password_form}
    return render(request, "reset_password.html", context)
