from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
    
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        
        # Make first name, last name, and email fields read-only
        self.fields['first_name'].widget.attrs['readonly'] = True
        #self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True