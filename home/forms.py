from django import forms

class FormContacto(forms.Form):
    name = forms.CharField(label = "Name", widget=forms.TextInput(attrs={'placeholder': 'Eleanor Shellstrop'}))
    email = forms.EmailField(label = "Work Email", widget=forms.TextInput(attrs={'placeholder': 'eleanor@goodplace.com'}))
    message = forms.CharField(label = "Message", widget=forms.Textarea(attrs={'placeholder': 'How can we help you?'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class FormSingUp(forms.Form):
    name_up = forms.CharField(label = "Name", widget=forms.TextInput(attrs={'placeholder': 'Eleanor Shellstrop'}))
    email_up = forms.EmailField(label = "Email", widget=forms.TextInput(attrs={'placeholder': 'eleanor@goodplace.com'}))
    password_up = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs={'placeholder': '..............', 'class': 'placeholder-centered'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class FormSingIn(forms.Form):
    email_in = forms.CharField(label = "Username", widget=forms.TextInput(attrs={'placeholder': 'eleanor27'}))
    password_in = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs={'placeholder': '..............', 'class': 'placeholder-centered'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

