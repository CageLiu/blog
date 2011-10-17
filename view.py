# -*- coding:utf-8 -*-
#FileName:view.py

import datetime
from md5 import md5
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db.models import Q
from blog.category.models import *
from blog.forms import *

def index(request,name="",arid="",template_name="index.html"):
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
	if arid:
		try:
			arid = int(arid)
			try:
				details = Article.objects.filter(article_type = name).get(id = arid)
				title = details.title
				try:
					replay = Replays.objects.filter(article_id = details.id).order_by('-time')
				except Replays.DoesNotExist:
					replay = ''
			except Article.DoesNotExist:
				details = ''
		except ValueError:
			pass
		if request.method == "POST":
			form = Replay(request.POST)
			if form.is_valid():
				cont = form.cleaned_data
				cont['article_id'] = details.id
				Replays(name=cont['name'],message=cont['message'],article_id=cont['article_id'],email=cont['email']).save()
				return HttpResponseRedirect("/blog/" + name +"/" + str(arid) + "/")
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
		article = Article.objects.filter(Q(title__icontains = search)|Q(author__icontains = search)|Q(article_type__icontains = search)|Q(cont__icontains = search)).order_by('-date')
		template_name = 'index.html'
	return render_to_response(template_name,locals())


def admin(request):
	if request.session.get('username'):
		return HttpResponseRedirect('/blog/manager/')
	else:
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
						request.session['username'] = usm
						request.session.set_expiry(0)
						return HttpResponseRedirect('/blog/manager/')
					else:
						ptips = '密码错误!'
	return render_to_response('login.html',locals())

def manager(request,operation='',template_name="admin.html"):
	if request.session.get('username'):
		if operation:
			template_name = operation+".html"
			if operation == 'add_user':
				if request.method == "POST":
					add_user_form = Add_user(request.POST)
					if add_user_form.is_valid():
						newuser = add_user_form.cleaned_data
						User(username = newuser['usm'],password = md5(newuser['confirm_pwd']).hexdigest()).save()
						return HttpResponseRedirect('/blog/manager/')
				else:
					add_user_form = Add_user()
			if operation == 'add_article':
				if 'aid' in request.GET:
					try:
						aid = int(request.GET['aid'])
					except ValueError:
						pass
					article = Article.objects.get(id = aid)
					add_article_form = Add_article(initial={'title':article.title,'author':article.author,'cont':article.cont,'article_type':article.article_type})
					if request.method == "POST":
						add_article_form = Add_article(request.POST)
						if add_article_form.is_valid():
							newarticle = add_article_form.cleaned_data
							Article.objects.filter(id = aid).update(title=newarticle['title'],author=newarticle['author'],cont=newarticle['cont'],article_type=newarticle['article_type'])
							return HttpResponseRedirect('/blog/manager/')
				elif request.method == "POST":
					add_article_form = Add_article(request.POST)
					if add_article_form.is_valid():
						newarticle = add_article_form.cleaned_data
						Article(title=newarticle['title'],author=newarticle['author'],cont=newarticle['cont'],article_type=newarticle['article_type']).save()
						return HttpResponseRedirect('/blog/manager/')
				else:
					add_article_form = Add_article()
		else:
			user = User.objects.all().order_by('username')
			article = Article.objects.all().order_by('-date')
			if 'aid' in request.GET:
				try:
					aid = int(request.GET['aid'])
				except ValueError:
					pass
				Article.objects.get(id = aid).delete()
				Replays.objects.filter(article_id = aid).delete()
				return HttpResponseRedirect('/blog/manager/')
	else:
		return HttpResponseRedirect('/blog/onlyme/')
	return render_to_response(template_name,locals())
