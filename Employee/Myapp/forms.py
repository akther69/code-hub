from django import forms

class WorkForm(forms.Form) :
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    description=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    start_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control mb-2","type":"date"}))
    end_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control mb-2","type":"date"}))
    status_options=(
        ("created","created"),
        ("wip","wip"),
        ("completed","completed"),
        ("due","due")
    )
    status=forms.ChoiceField(choices=status_options,widget=forms.Select(attrs={"class":"form-control mb-2 form-select"}))