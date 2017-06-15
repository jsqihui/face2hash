# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_hash(request):
    data = json.loads(request.body) 
    print data
    return HttpResponse(json.dumps({"message": "data received"}),
                        content_type = "application/json",
                        status = 200)
