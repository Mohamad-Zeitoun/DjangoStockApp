from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'



class StockForm(forms.Form):
    ticker_symbol = forms.CharField(label="Ticker Symbol", max_length=50)
    
    fromDate = forms.DateField(

        input_formats=["%Y-%m-%d"],
        widget=DateInput

    )

    toDate = forms.DateField(

        input_formats=["%Y-%m-%d"],
        widget=DateInput

    )
    





