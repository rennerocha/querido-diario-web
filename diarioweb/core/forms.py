import datetime
from django import forms


TERRITORIES = [
    ("", ">>> TODAS <<<"),
    ("5002704", "Campo Grande - MS"),
    ("4205407", "Florianópolis - SC"),
    ("5208707", "Goiânia - GO"),
    ("2408102", "Natal - RN"),
    ("1721000", "Palmas - TO"),
    ("3304557", "Rio de Janeiro - RJ"),
    ("2927408", "Salvador - BA"),
]


class SearchForm(forms.Form):
    territory_id = forms.ChoiceField(label="Cidade", choices=TERRITORIES, initial="", required=False)
    since = forms.DateField(label="Data Inicial", required=True)
    until = forms.DateField(label="Data Final", required=False, initial=datetime.date.today())
    keywords = forms.CharField(label="Palavras Chave", required=False)
