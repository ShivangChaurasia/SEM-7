from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    teacher_name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    feedback = forms.CharField(widget=forms.Textarea)
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
