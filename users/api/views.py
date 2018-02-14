# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User

@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(nickname=username, password=password)
            if user.is_active:
                return Response({
                    'response': 1,
                    'data': {
                        'id': user.pk,
                        'name': user.name,
                        'last_name': user.last_name
                    }
                })
            else:
                return Response({'response': 0, 'errors': 'the user has been deleted'})
        except ObjectDoesNotExist:
            return Response({'response': 0, 'errors': 'Username or password incorrect'})

