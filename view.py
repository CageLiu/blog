# -*- coding:utf-8 -*-
#FileName:view.py

import datetime
from md5 import md5
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db.models import Q
from blog.category.models import *
from blog.forms import *

def index(request,name="",title="",template_name="index.html"):
	category = Type.objects.all().order_by('id')
	category_list = [item.name for item in category]
	if not name or name == "index":
		article = Article.objects.all().order_by('-date')
	elif name not in category_list:
		template_name = '404.html'
	else:
		try:
			article = Article.objects.filter(article_type = name).order_by('-date')
		except Article.DoesNotExist:
			article = ''
	if title:
		try:
			details = Article.objects.filter(article_type = name).get(title = title)
		except Article.DoesNotExist:
			details = ''
		try:
			replay = Replays.objects.filter(article_id = details.id).order_by('-time')
		except Replays.DoesNotExist:
			replay = ''
		if request.method == "POST":
			form = Replay(request.POST)
			if form.is_valid():
				cont = form.cleaned_data
				cont['parent_id'] = 0
				cont['article_id'] = details.id
				Replays(name=cont['name'],message=cont['message'],parent_id=cont['parent_id'],article_id=cont['article_id'],email=cont['email']).save()
				return HttpResponseRedirect("/" + name +"/" + title + "/")
			if form['name'].errors:
				form.errors['name'] = '姓名不能为空!'
			if form['email'].errors:
				form.errors['email'] = '请输入正确的邮箱地址!'
			if form['message'].errors:
				form.errors['message'] = '回复内容不能为空!'
		else:
			form = Replay()
	if name == 'about':
		template_name = 'about.html'
	if name == 'contact':
		template_name = 'contact.html'
	if 'search' in request.GET:
		search = request.GET['search']
		article = Article.objects.filter(Q(title__icontains = search)|Q(author__icontains = search)|Q(article_type__icontains = search)|Q(cont__icontains = search))
		template_name = 'index.html'
	return render_to_response(template_name,locals())


def admin(request):
	if 'username' in request.POST and 'password' in request.POST:
		usm = request.POST['username']
		pwd = request.POST['password']
		if len(usm) == 0:
			utips = '用户名不能为空!'
		elif len(pwd) == 0:
			ptips = '密码不能为空!'
		else:
			try:
				rightpwd = User.objects.get(username = usm).password
			except User.DoesNotExist:
				utips = '用户名不存在!'
			else:
				if rightpwd == md5(pwd).hexdigest():
					return HttpResponseRedirect('/manager/')
				else:
					ptips = '密码错误!'
	return render_to_response('login.html',locals())

def manager(request):
	return render_to_response('index.html',locals())
