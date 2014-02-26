# -*- coding: utf-8 -*-
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.db import models
from tok.models import Dictionary


def root(request):
    ctxt = RequestContext(request, {})
    return render_to_response("index.html", ctxt)


def search(request):
    key = ''
    message = ''
    if "keyword" in request.POST:
        keyword = request.POST["keyword"]

        dst = keyword.replace(u'　', ' ')
        splited = dst.split(' ')

        if len(splited) >= 2:
            key = splited.pop(0)

	    for val in splited:
                dictionary = Dictionary()
		# http://iyukki.blog56.fc2.com/blog-entry-137.html
                dictionary.key = key
                #dictionary.key = unicode(key,'utf-8')
                dictionary.name = val
                #dictionary.name = unicode(val,'utf-8')
                check = Dictionary.objects.extra(
                    where=["key = '" + key + "'", "name = '" + val + "'"]
                )
		if not check: 
                    dictionary.save()
                message += (val.encode('utf-8') + ', ')
        else:
            message = "no key and message"
    else:
        keyword = ""
        message = "input message"
    ctxt = RequestContext(request, {
        "keyword": keyword,
        "key": key, 
        "message": message
    })
    return render_to_response("search.html", ctxt)

from django.http import HttpResponse
from simplejson import dumps
from django.core import serializers

#http://stackoverflow.com/questions/9262278/django-view-returning-json-without-using-template
def get_json(request):
    dictionaries = Dictionary.objects.all()
    to_json = []
    for dictionary in dictionaries:
        dic_dict = {}
        dic_dict['key'] = dictionary.key
        dic_dict['name'] = dictionary.name

        to_json.append(dic_dict)

    # convert the list to JSON
    #response_data = simplejson.dumps(to_json)
    #response_data = dumps(to_json)
    response_data = dumps(to_json,ensure_ascii=False)
    # http://bixly.com/blog/json-jquery-and-django/
    return HttpResponse(response_data, mimetype='application/json')

def get_json2(request):
    foos = Dictionary.objects.all()
    data = serializers.serialize('json', foos)
    return HttpResponse(data, mimetype='application/json')

@csrf_protect
def search_dec(request):
    if "keyword" in request.POST:
        keyword = request.POST["keyword"]
    else:
        keyword = ""
    ctxt = RequestContext(request, {
        "keyword": keyword
    })
    return render_to_response("search.html", ctxt)
