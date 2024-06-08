from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,
                             widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']

    #def __init__(self, *args, **kwargs):
        #super(CommentForm, self).__init__(*args, **kwargs)
        
        # Make first name, last name, and email fields read-only
        #self.fields['name'].widget.attrs['readonly'] = True
        #self.fields['last_name'].widget.attrs['readonly'] = True
        #self.fields['email'].widget.attrs['readonly'] = True

class SearchForm(forms.Form):
    query = forms.CharField()
    