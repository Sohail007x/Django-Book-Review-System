from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        # Adding widgets for all fields to make the form compact, user-friendly, and styled with Bootstrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description', 'rows': 3}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN (13 digits)', 'maxlength': 13}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'average_rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the average rating (0-5)', 'min': 0, 'max': 5}),
        }

    # Custom clean method if necessary, e.g., if you want to enforce certain constraints
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN should be exactly 13 digits.")
        return isbn

    def clean_average_rating(self):
        rating = self.cleaned_data.get('average_rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating must be between 0 and 5.")
        return rating
