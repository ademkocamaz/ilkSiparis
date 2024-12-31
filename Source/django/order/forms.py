from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Fieldset, Layout, Row, Submit, Div, Field
from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout
from order._model.order import Order
from order._model.order_line import OrderLine
from order._model.order_state import OrderState
from order._model.order_line_currency import OrderLineCurrency
from extra_views import InlineFormSetFactory


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column("order_current"), Column("date")),
            Row(Column("invoice_number"), Column("shipment_date")),
            Row(Column("number"), Column("order_state")),
            Fieldset(
                "Sipariş Satırları",
                ModalEditFormsetLayout(
                    formset_name="OrderLineInlineFormset",
                ),
            ),
            Div(
                Submit("submit", "Kaydet", css_class="btn btn-lg btn-warning"),
                css_class="d-flex justify-content-center",
            ),
        )

    class Meta:
        model = Order
        fields = [
            field.name
            for field in Order._meta.fields
            if field.name not in ("edited, created, user")
        ]
        widgets = {
            "date": forms.DateTimeInput(
                format=("%Y-%m-%dT%H:%M:%S"), attrs={"type": "datetime-local"}
            ),
            "shipment_date": forms.DateTimeInput(
                format=("%Y-%m-%dT%H:%M:%S"), attrs={"type": "datetime-local"}
            ),
        }


class OrderLineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        field_list = [
            field.name
            for field in OrderLine._meta.fields
            if field.name not in ("id, edited, created, user")
        ]
        self.helper.layout = ModalEditLayout(
            *field_list,
            Field("user"),
        )

    class Meta:
        model = OrderLine
        fields = [
            field.name
            for field in OrderLine._meta.fields
            if field.name not in ("edited, created")
        ]
        widgets = {
            "user": forms.HiddenInput,
        }


class OrderLineInlineFormset(InlineFormSetFactory):
    """def __init__(self, *args, **kwargs):
    super(OrderLineInlineFormset, self).__init__(*args, **kwargs)"""

    model = OrderLine
    form_class = OrderLineForm
    fields = [
        field.name
        for field in OrderLine._meta.fields
        if field.name not in ("id, edited, created")
    ]

    factory_kwargs = {
        "extra": 0,
        "fk_name": "order_line",
    }

    # formset_kwargs = {
    #     "form_kwargs": {
    #         "initial": {

    #         },
    #     }
    # }

    def get_formset_kwargs(self):
        kwargs = super(OrderLineInlineFormset, self).get_formset_kwargs()
        kwargs["form_kwargs"] = {
            "initial": {
                "user": self.request.user,
                # "unit_price": 5.55,
                # "total_price": 6.66,
            }
        }
        # print(kwargs)
        return kwargs


class OrderStateForm(forms.ModelForm):
    class Meta:
        model = OrderState
        fields = [
            field.name
            for field in OrderState._meta.fields
            if field.name not in ("edited, created, user")
        ]

class OrderLineCurrencyForm(forms.ModelForm):
    class Meta:
        model = OrderLineCurrency
        fields = [
            field.name
            for field in OrderLineCurrency._meta.fields
            if field.name not in ("edited, created, user")
        ]
