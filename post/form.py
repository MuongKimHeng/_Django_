from django import forms

class PostForm(forms.Form):

    title = forms.CharField(
        label="Title",
        max_length=100,
        required=True
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea,
        required=True
    )