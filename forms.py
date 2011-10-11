# -*- coding:utf-8 -*-
#FileName:forms.py

from django import forms

class Replay(forms.Form):
	name = forms.CharField(widget = forms.TextInput(attrs={'class':'txt name'}))
	email = forms.EmailField(required = False,widget = forms.TextInput(attrs={'class':'txt email'}))
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'message'}))

class Add_user(forms.Form):
	usm = forms.CharField()
	pwd = forms.CharField(widget = forms.PasswordInput)
	confirm_pwd = forms.CharField(widget = forms.PasswordInput)

class Add_article(forms.Form):
	title = forms.CharField()
	author = forms.CharField()
	cont = forms.CharField(widget = forms.Textarea)
	article_type = forms.CharField()
