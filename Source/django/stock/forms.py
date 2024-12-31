from django import forms

from stock._model.stock import Stock
from stock._model.stock_unit import StockUnit
from stock._model.stock_type import StockType
from stock._model.stock_tax_set import StockTaxSet
from stock._model.stock_model import StockModel
from stock._model.stock_color import StockColor
from stock._model.stock_category import StockCategory


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            field.name
            for field in Stock._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockUnitForm(forms.ModelForm):
    class Meta:
        model = StockUnit
        fields = [
            field.name
            for field in StockUnit._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockTypeForm(forms.ModelForm):
    class Meta:
        model = StockType
        fields = [
            field.name
            for field in StockType._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockTaxSetForm(forms.ModelForm):
    class Meta:
        model = StockTaxSet
        fields = [
            field.name
            for field in StockTaxSet._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockModelForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = [
            field.name
            for field in StockModel._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockColorForm(forms.ModelForm):
    class Meta:
        model = StockColor
        fields = [
            field.name
            for field in StockModel._meta.fields
            if field.name not in ("edited, created, user")
        ]


class StockCategoryForm(forms.ModelForm):
    class Meta:
        model = StockCategory
        fields = [
            field.name
            for field in StockCategory._meta.fields
            if field.name not in ("edited, created, user")
        ]
