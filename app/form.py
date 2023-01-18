# from django.contrib.sites.shortcuts import get_current_site
# from django.core.exceptions import ValidationError
# from django.core.mail import send_mail
# from django.forms import *
# from django import forms
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from root.settings import EMAIL_HOST_USER


# class ForgotPasswordForm(forms.Form):
#     email = forms.EmailField()
#
#     def send_email(self):
#         subect = 'xabarni titlesi'
#         message = 'message ham keldi'
#         from_email = EMAIL_HOST_USER
#         recipient_list = ['asilbek1721@gmail.com']
#         result = send_mail(subect, message, from_email, recipient_list)
#         print(result)
