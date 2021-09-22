from django import forms

from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """ Форма для отзывов """
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')

