from .forms import FormSingUp, FormSingIn
from django.conf import settings

def get_FormSingUp(request):
    formSingUp = FormSingUp()
    return{
        'formSingUp': formSingUp
    }

def get_FormSingIn(request):
    formSingIn = FormSingIn()
    return{
        'formSingIn': formSingIn
    }

def get_TinyMCE(request):
    tiny_mce = settings.TINYMCE_API
    return{
        'tiny_mce' : tiny_mce
    }

def public_Key(request):
    recaptcha = settings.RECAPTCHA_SITE_KEY
    return{
        'site_key': recaptcha
    }