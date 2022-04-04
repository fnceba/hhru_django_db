from django import forms


class ReadFromCSVForm(forms.Form):
    start_index = forms.IntegerField(label="Start index")
    end_index = forms.IntegerField(label="End index")
    csv_file = forms.FileField()
