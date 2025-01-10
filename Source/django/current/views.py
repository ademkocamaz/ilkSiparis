from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from current.forms import CurrentForm
from current._model.current import Current


@login_required(login_url="/user/login/")
def current(request):

    if request.method == "POST":
        current_form = CurrentForm(request.POST)
        if current_form.is_valid():
            current_form.instance.user = request.user
            current_form.save()
            messages.add_message(request, messages.INFO, "Cari eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Cari eklenirken hata oluştu."
            )
            for error in list(current_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("current")

    current_form = CurrentForm()
    currents = Current.objects.filter(user=request.user).order_by("created")
    context = {"current_form": current_form, "currents": currents}
    return render(request=request, template_name="current.html", context=context)


@login_required(login_url="user/login/")
def current_detail(request, current_id):
    current = get_object_or_404(Current, pk=current_id)

    if request.method == "POST":
        current_form = CurrentForm(request.POST, instance=current)
        if current_form.is_valid():
            current_form.instance.user = request.user
            current_form.save()
            messages.add_message(request, messages.INFO, "Cari güncellendi.")
        else:
            messages.add_message(
                request, messages.INFO, "Cari güncellenirken bir hata oluştu."
            )
            for error in list(current_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        # return redirect('category_update',category.id)
        return redirect("current")

    current_form = CurrentForm(instance=current)
    context = {
        "current_form": current_form,
    }

    return render(request=request, template_name="current_detail.html", context=context)
