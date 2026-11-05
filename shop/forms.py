from django import forms

GENRES = [
    ("fantasy", "Fantasy"),
    ("sci-fi", "Sci-Fi"),
    ("crime", "Kryminał"),
]


class BookForm(forms.Form):
    title = forms.CharField(
        label="Tytuł książki",
        max_length=150,
        min_length=2,
        widget=forms.TextInput(attrs={"class": "wide-input", "placeholder": "Wpisz tytuł..."}),
    )
    price = forms.DecimalField(
        label="Cena (zł)",
        min_value=0.01,
        max_digits=6,
        decimal_places=2,
    )
    discount_price = forms.DecimalField(
        label="Cena promocyjna (zł)",
        min_value=0.01,
        max_digits=6,
        decimal_places=2,
        required=False,
    )
    genre = forms.ChoiceField(
        label="Gatunek",
        choices=GENRES,
    )
    in_stock = forms.BooleanField(
        label="Dostępna w magazynie",
        required=False,
        initial=True,
    )

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if title.lower() in ["test", "brudnopis", "aaa"]:
            raise forms.ValidationError("Wprowadź prawdziwy tytuł, nie testowy.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        discount_price = cleaned_data.get("discount_price")

        if price and discount_price and discount_price >= price:
            self.add_error("discount_price", "Cena promocyjna musi być niższa od regularnej.")

        return cleaned_data


class SearchForm(forms.Form):
    q = forms.CharField(label="Szukaj", required=False, max_length=50)
    in_stock_only = forms.BooleanField(label="Tylko dostępne", required=False)