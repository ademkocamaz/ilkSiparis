from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stock.forms import (
    StockForm,
    StockUnitForm,
    StockTypeForm,
    StockTaxSetForm,
    StockModelForm,
    StockColorForm,
    StockCategoryForm,
)
from stock._model.stock import Stock
from stock._model.stock_unit import StockUnit
from stock._model.stock_type import StockType
from stock._model.stock_tax_set import StockTaxSet
from stock._model.stock_model import StockModel
from stock._model.stock_color import StockColor
from stock._model.stock_category import StockCategory


@login_required(login_url="/user/login/")
def stock(request):

    if request.method == "POST":
        stock_form = StockForm(request.POST)
        if stock_form.is_valid():
            stock_form.instance.user = request.user
            stock_form.save()
            messages.add_message(request, messages.INFO, "Stok Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Kartı eklenirken hata oluştu."
            )
            for error in list(stock_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock")

    stock_form = StockForm()
    stocks = Stock.objects.order_by("created")
    context = {
        "stock_form": stock_form,
        "stocks": stocks,
    }
    return render(request=request, template_name="stock.html", context=context)


@login_required(login_url="/user/login/")
def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)

    if request.method == "POST":
        stock_form = StockForm(request.POST, instance=stock)
        if stock_form.is_valid():
            stock_form.instance.user = request.user
            stock_form.save()
            messages.add_message(request, messages.INFO, "Stok Kartı güncellendi.")
        else:
            messages.add_message(
                request, messages.INFO, "Stok Kartı güncellenirken bir hata oluştu."
            )
            for error in list(stock_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock")

    stock_form = StockForm(instance=stock)
    context = {
        "stock_form": stock_form,
    }

    return render(request=request, template_name="stock_detail.html", context=context)


@login_required(login_url="/user/login/")
def stock_unit(request):
    if request.method == "POST":
        stock_unit_form = StockUnitForm(request.POST)
        if stock_unit_form.is_valid():
            stock_unit_form.instance.user = request.user
            stock_unit_form.save()
            messages.add_message(request, messages.INFO, "Stok Birim Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Birim Kartı eklenirken hata oluştu."
            )
            for error in list(stock_unit_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_unit")

    stock_unit_form = StockUnitForm()
    stock_units = StockUnit.objects.order_by("created")
    context = {
        "stock_unit_form": stock_unit_form,
        "stock_units": stock_units,
    }
    return render(request=request, template_name="stock_unit.html", context=context)


@login_required(login_url="/user/login/")
def stock_unit_detail(request, stock_unit_id):
    stock_unit = get_object_or_404(StockUnit, pk=stock_unit_id)

    if request.method == "POST":
        stock_unit_form = StockUnitForm(request.POST, instance=stock_unit)
        if stock_unit_form.is_valid():
            stock_unit_form.instance.user = request.user
            stock_unit_form.save()
            messages.add_message(
                request, messages.INFO, "Stok Birim Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Birim Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_unit_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_unit")

    stock_unit_form = StockUnitForm(instance=stock_unit)
    context = {
        "stock_unit_form": stock_unit_form,
    }

    return render(
        request=request, template_name="stock_unit_detail.html", context=context
    )


@login_required(login_url="/user/login/")
def stock_type(request):
    if request.method == "POST":
        stock_type_form = StockTypeForm(request.POST)
        if stock_type_form.is_valid():
            stock_type_form.instance.user = request.user
            stock_type_form.save()
            messages.add_message(request, messages.INFO, "Stok Tipi Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Tipi Kartı eklenirken hata oluştu."
            )
            for error in list(stock_type_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_type")

    stock_type_form = StockTypeForm()
    stock_types = StockType.objects.order_by("created")
    context = {
        "stock_type_form": stock_type_form,
        "stock_types": stock_types,
    }
    return render(request=request, template_name="stock_type.html", context=context)


@login_required(login_url="/user/login/")
def stock_type_detail(request, stock_type_id):
    stock_type = get_object_or_404(StockType, pk=stock_type_id)

    if request.method == "POST":
        stock_type_form = StockTypeForm(request.POST, instance=stock_type)
        if stock_type_form.is_valid():
            stock_type_form.instance.user = request.user
            stock_type_form.save()
            messages.add_message(request, messages.INFO, "Stok Tipi Kartı güncellendi.")
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Tipi Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_type_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_type")

    stock_type_form = StockTypeForm(instance=stock_type)
    context = {
        "stock_type_form": stock_type_form,
    }

    return render(
        request=request, template_name="stock_type_detail.html", context=context
    )


@login_required(login_url="/user/login/")
def stock_tax_set(request):
    if request.method == "POST":
        stock_tax_set_form = StockTaxSetForm(request.POST)
        if stock_tax_set_form.is_valid():
            stock_tax_set_form.instance.user = request.user
            stock_tax_set_form.save()
            messages.add_message(
                request, messages.INFO, "Stok Vergi Oranı Kartı eklendi."
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Stok Vergi Oranı Kartı eklenirken hata oluştu.",
            )
            for error in list(stock_tax_set_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_tax_set")

    stock_tax_set_form = StockTaxSetForm()
    stock_tax_sets = StockTaxSet.objects.order_by("created")
    context = {
        "stock_tax_set_form": stock_tax_set_form,
        "stock_tax_sets": stock_tax_sets,
    }
    return render(request=request, template_name="stock_tax_set.html", context=context)


@login_required(login_url="/user/login/")
def stock_tax_set_detail(request, stock_tax_set_id):
    stock_tax_set = get_object_or_404(StockTaxSet, pk=stock_tax_set_id)

    if request.method == "POST":
        stock_tax_set_form = StockTaxSetForm(request.POST, instance=stock_tax_set)
        if stock_tax_set_form.is_valid():
            stock_tax_set_form.instance.user = request.user
            stock_tax_set_form.save()
            messages.add_message(
                request, messages.INFO, "Stok Vergi Oranı Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Vergi Oranı Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_tax_set_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_tax_set")

    stock_tax_set_form = StockTaxSetForm(instance=stock_tax_set)
    context = {
        "stock_tax_set_form": stock_tax_set_form,
    }

    return render(
        request=request, template_name="stock_tax_set_detail.html", context=context
    )


@login_required(login_url="/user/login/")
def stock_model(request):
    if request.method == "POST":
        stock_model_form = StockModelForm(request.POST)
        if stock_model_form.is_valid():
            stock_model_form.instance.user = request.user
            stock_model_form.save()
            messages.add_message(request, messages.INFO, "Stok Model Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Model Kartı eklenirken hata oluştu."
            )
            for error in list(stock_model_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_model")

    stock_model_form = StockModelForm()
    stock_models = StockModel.objects.order_by("created")
    context = {
        "stock_model_form": stock_model_form,
        "stock_models": stock_models,
    }
    return render(request=request, template_name="stock_model.html", context=context)


@login_required(login_url="/user/login/")
def stock_model_detail(request, stock_model_id):
    stock_model = get_object_or_404(StockModel, pk=stock_model_id)

    if request.method == "POST":
        stock_model_form = StockModelForm(request.POST, instance=stock_model)
        if stock_model_form.is_valid():
            stock_model_form.instance.user = request.user
            stock_model_form.save()
            messages.add_message(
                request, messages.INFO, "Stok Model Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Model Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_model_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_model")

    stock_model_form = StockModelForm(instance=stock_model)
    context = {
        "stock_model_form": stock_model_form,
    }

    return render(
        request=request, template_name="stock_model_detail.html", context=context
    )


@login_required(login_url="/user/login/")
def stock_color(request):
    if request.method == "POST":
        stock_color_form = StockColorForm(request.POST)
        if stock_color_form.is_valid():
            stock_color_form.instance.user = request.user
            stock_color_form.save()
            messages.add_message(request, messages.INFO, "Stok Renk Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Renk Kartı eklenirken hata oluştu."
            )
            for error in list(stock_color_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_color")

    stock_color_form = StockColorForm()
    stock_colors = StockColor.objects.order_by("created")
    context = {
        "stock_color_form": stock_color_form,
        "stock_colors": stock_colors,
    }
    return render(request=request, template_name="stock_color.html", context=context)


@login_required(login_url="/user/login/")
def stock_color_detail(request, stock_color_id):
    stock_color = get_object_or_404(StockColor, pk=stock_color_id)

    if request.method == "POST":
        stock_color_form = StockColorForm(request.POST, instance=stock_color)
        if stock_color_form.is_valid():
            stock_color_form.instance.user = request.user
            stock_color_form.save()
            messages.add_message(request, messages.INFO, "Stok Renk Kartı güncellendi.")
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Renk Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_color_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_color")

    stock_color_form = StockColorForm(instance=stock_color)
    context = {
        "stock_color_form": stock_color_form,
    }

    return render(
        request=request, template_name="stock_color_detail.html", context=context
    )


@login_required(login_url="/user/login/")
def stock_category(request):
    if request.method == "POST":
        stock_category_form = StockCategoryForm(request.POST)
        if stock_category_form.is_valid():
            stock_category_form.instance.user = request.user
            stock_category_form.save()
            messages.add_message(request, messages.INFO, "Stok Kategori Kartı eklendi.")
        else:
            messages.add_message(
                request, messages.ERROR, "Stok Kategori Kartı eklenirken hata oluştu."
            )
            for error in list(stock_category_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)
        return redirect("stock_category")

    stock_category_form = StockCategoryForm()
    stock_categories = StockCategory.objects.order_by("created")
    context = {
        "stock_category_form": stock_category_form,
        "stock_categories": stock_categories,
    }
    return render(request=request, template_name="stock_category.html", context=context)


@login_required(login_url="/user/login/")
def stock_category_detail(request, stock_category_id):
    stock_category = get_object_or_404(StockCategory, pk=stock_category_id)

    if request.method == "POST":
        stock_category_form = StockCategoryForm(request.POST, instance=stock_category)
        if stock_category_form.is_valid():
            stock_category_form.instance.user = request.user
            stock_category_form.save()
            messages.add_message(
                request, messages.INFO, "Stok Kategori Kartı güncellendi."
            )
        else:
            messages.add_message(
                request,
                messages.INFO,
                "Stok Kategori Kartı güncellenirken bir hata oluştu.",
            )
            for error in list(stock_category_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect("stock_category")

    stock_category_form = StockCategoryForm(instance=stock_category)
    context = {
        "stock_category_form": stock_category_form,
    }

    return render(
        request=request, template_name="stock_category_detail.html", context=context
    )
