# -*- coding:utf-8 -*-
#FileName:forms.py

from django import forms

class Replay(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(required = False)
	message = forms.CharField(widget = forms.Textarea)
