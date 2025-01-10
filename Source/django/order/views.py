from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order._model.order import Order
from order._model.order_line import OrderLine
from order._model.order_state import OrderState
from order._model.order_line_currency import OrderLineCurrency
from order.forms import (
    OrderForm,
    OrderLineForm,
    OrderLineInlineFormset,
    OrderStateForm,
    OrderLineCurrencyForm,
)
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from datetime import datetime


@login_required(login_url="user/login/")
def order(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.instance.user = request.user
            order_form.save()
            messages.add_message(request, messages.INFO, "Sipariş eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Sipariş eklenirken hata oluştu."
            )
            for error in list(order_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("order")

    order_form = OrderForm()

    orders = Order.objects.filter(user=request.user).order_by("created")
    context = {
        "order_form": order_form,
        "orders": orders,
    }
    return render(request=request, template_name="order.html", context=context)


class OrderCreateView(CreateWithInlinesView):
    template_name = "order_create.html"

    model = Order
    inlines = [
        OrderLineInlineFormset,
    ]
    form_class = OrderForm

    success_url = reverse_lazy("order")

    def forms_valid(self, form, inlines):
        form.instance.user = self.request.user
        response = self.form_valid(form)
        for formset in inlines:
            formset.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = self.get_form()
        return context


class OrderDetailView(UpdateWithInlinesView):
    template_name = "order_detail.html"

    model = Order
    inlines = [
        OrderLineInlineFormset,
    ]
    form_class = OrderForm

    success_url = reverse_lazy("order")


@login_required(login_url="user/login/")
def order_print(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order_lines = OrderLine.objects.filter(order_line=order)
    context = {
        "order": order,
        "order_lines": order_lines,
    }
    return render(request=request, template_name="order_print.html", context=context)


@login_required(login_url="user/login/")
def order_state(request):
    if request.method == "POST":
        order_state_form = OrderStateForm(request.POST)
        if order_state_form.is_valid():
            order_state_form.instance.user = request.user
            order_state_form.save()
            messages.add_message(request, messages.INFO, "Sipariş Durum Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Sipariş Durum Kartı eklenirken hata oluştu."
            )
            for error in list(order_state_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("order_state")

    order_state_form = OrderStateForm()

    order_states = OrderState.objects.filter(user=request.user).order_by("created")
    context = {
        "order_state_form": order_state_form,
        "order_states": order_states,
    }
    return render(request=request, template_name="order_state.html", context=context)


@login_required(login_url="user/login/")
def order_state_detail(request, order_state_id):
    order_state = get_object_or_404(OrderState, pk=order_state_id)

    if request.method == "POST":
        order_state_form = OrderStateForm(request.POST, instance=order_state)
        if order_state_form.is_valid():
            order_state_form.instance.user = request.user
            order_state_form.save()
            messages.add_message(
                request, messages.INFO, "Sipariş Durum Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Sipariş Durum Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(order_state_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("order_state")

    order_state_form = OrderStateForm(instance=order_state)
    context = {
        "order_state_form": order_state_form,
    }

    return render(
        request=request, template_name="order_state_detail.html", context=context
    )


@login_required(login_url="user/login/")
def order_line_currency(request):
    if request.method == "POST":
        order_line_currency_form = OrderLineCurrencyForm(request.POST)
        if order_line_currency_form.is_valid():
            order_line_currency_form.instance.user = request.user
            order_line_currency_form.save()
            messages.add_message(request, messages.INFO, "Para Birimi Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Para Birimi Kartı eklenirken hata oluştu."
            )
            for error in list(order_line_currency_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("order_line_currency")

    order_line_currency_form = OrderLineCurrencyForm()

    order_line_currencies = OrderLineCurrency.objects.filter(
        user=request.user
    ).order_by("created")
    context = {
        "order_line_currency_form": order_line_currency_form,
        "order_line_currencies": order_line_currencies,
    }
    return render(
        request=request, template_name="order_line_currency.html", context=context
    )


@login_required(login_url="user/login/")
def order_line_currency_detail(request, order_line_currency_id):
    order_line_currency = get_object_or_404(
        OrderLineCurrency, pk=order_line_currency_id
    )

    if request.method == "POST":
        order_line_currency_form = OrderLineCurrencyForm(
            request.POST, instance=order_line_currency
        )
        if order_line_currency_form.is_valid():
            order_line_currency_form.instance.user = request.user
            order_line_currency_form.save()
            messages.add_message(
                request, messages.INFO, "Para Birimi Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Para Birimi Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(order_line_currency_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("order_line_currency")

    order_line_currency_form = OrderLineCurrencyForm(instance=order_line_currency)
    context = {
        "order_line_currency_form": order_line_currency_form,
    }

    return render(
        request=request,
        template_name="order_line_currency_detail.html",
        context=context,
    )
