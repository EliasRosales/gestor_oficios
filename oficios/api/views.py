# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

import oficios
from oficios.models import Trades, Departments, Sender


@api_view(['GET'])
def get_oficios(request):
    oficios = Trades.objects.filter(is_active=True).order_by('-date_trades')
    response = []
    for oficio in oficios:
        response.append({
            'fecha_oficio': oficio.date_trades,
            'descripcion': oficio.description,
            'folio': oficio.folio,
            'observaciones': oficio.observations,
            'departamentos': oficio.departament.name,
            'remitente': oficio.sender.department,
            'fecha_registro': oficio.register_date,
            'id': oficio.pk
        })
    return Response({'oficios': response})


@api_view(['GET'])
def get_departamentos(request):
    departamentos = Departments.objects.filter(is_active=True)
    response = []
    for departamento in departamentos:
        response.append({
            'nombre': departamento.name,
            'responsable': departamento.responsible,
            'id': departamento.pk
        })
    return Response({'departamentos': response})


@api_view((['GET']))
def get_remitentes(request):
    remitentes = Sender.objects.filter(is_active=True)
    response = []
    for remitente in remitentes:
        response.append({
            'nombre': remitente.department,
            'responsable': remitente.responsible,
            'id': remitente.pk
        })
    return Response({'remitentes': response})


@api_view(['GET'])
def get_oficios_by_id(request, oficio_id):
    try:
        oficio = Trades.objects.get(pk=oficio_id)
        response = {
            'fecha_oficio': oficio.date_trades,
            'descripcion': oficio.description,
            'folio': oficio.folio,
            'observaciones': oficio.observations,
            'departamentos': oficio.departament.pk,
            'remitente': oficio.sender.pk,
            'fecha_registro': oficio.register_date,
            'id': oficio.pk
        }
        return Response({'response': 1, 'oficio': response})
    except Trades.DoesNotExist:
        return Response({'response': 0})


@api_view(['GET'])
def get_departamentos_by_id(request, departamento_id):
    try:
        departamento = Departments.objects.get(pk=departamento_id)
        response = {
            'nombre': departamento.name,
            'responsable': departamento.responsible,
        }
        return Response({'response': 1, 'departamento': response})
    except Departments.DoesNotExist:
        return Response({'response': 0})


@api_view((['GET']))
def get_remitentes_by_id(request, remitente_id):
    try:
        remitente = Sender.objects.get(pk=remitente_id)
        response = {
            'nombre': remitente.department,
            'responsable': remitente.responsible,
        }
        return Response({'response': 1, 'remitente': response})
    except Departments.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
def set_oficio(request):
    date_trades = request.data['fecha_oficio']
    description = request.data['descripcion']
    folio = request.data['folio']
    observations = request.data['observaciones']
    departament_id = request.data['departamento_id']
    sender_id = request.data['remitente_id']
    try:
        departament = Departments.objects.get(pk=departament_id)
        sender = Sender.objects.get(pk=sender_id)
        Trades.objects.create(date_trades=date_trades, description=description, folio=folio, observations=observations,
                              departament=departament, sender=sender)
        return Response({'response': 1})
    except Departments.DoesNotExist or Sender.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
def set_departamento(request):
    name = request.data['nombre']
    responsible = request.data['responsable']
    Departments.objects.create(name=name, responsible=responsible)
    return Response({'response': 1})


@api_view((['POST']))
def set_remitente(request):
    if request.method == 'POST':
        name = request.data['nombre']
        responsible = request.data['responsable']
        Sender.objects.create(department=name, responsible=responsible)
        return Response({'response': 1})


@api_view(['POST'])
def delete_oficio(request):
    try:
        oficio = Trades.objects.get(pk=request.data['oficio_id'])
        oficio.delete_date = datetime.today()
        oficio.is_active = False
        oficio.save()
        return Response({'response': 1})
    except Trades.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
def delete_departamento(request):
    try:
        departamento = Departments.objects.get(pk=request.data['departamento_id'])
        departamento.delete_date = datetime.today()
        departamento.is_active = False
        departamento.save()
        return Response({'response': 1})
    except Departments.DoesNotExist:
        return Response({'response': 0})


@api_view((['POST']))
def delete_remitente(request):
    try:
        remitente = Sender.objects.get(pk=request.data['remitente_id'])
        remitente.delete_date = datetime.today()
        remitente.is_active = False
        remitente.save()
        return Response({'response': 1})
    except Trades.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
def update_oficio(request):
    oficio_id = request.data['oficio_id']
    date_trades = request.data['fecha_oficio']
    description = request.data['descripcion']
    folio = request.data['folio']
    observations = request.data['observaciones']
    departament_id = request.data['departamento_id']
    sender_id = request.data['remitente_id']
    try:
        departament = Departments.objects.get(pk=departament_id)
        sender = Sender.objects.get(pk=sender_id)
        oficio = Trades.objects.get(pk=oficio_id)
        oficio.date_trades = date_trades
        oficio.description = description
        oficio.folio = folio
        oficio.observations = observations
        oficio.departament = departament
        oficio.sender = sender
        oficio.save()
        return Response({'response': 1})
    except Departments.DoesNotExist or Sender.DoesNotExist or Trades.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
def update_departamento(request):
    try:
        departamento = Departments.objects.get(pk=request.data['departamento_id'])
        name = request.data['nombre']
        responsible = request.data['responsable']
        departamento.name = name
        departamento.responsible = responsible
        departamento.save()
        return Response({'response': 1})
    except Departments.DoesNotExist:
        return Response({'response': 0})


@api_view((['POST']))
def update_remitente(request):
    try:
        remitente = Sender.objects.get(pk=request.data['remitente_id'])
        name = request.data['nombre']
        responsible = request.data['responsable']
        remitente.name = name
        remitente.responsible = responsible
        remitente.save()
        return Response({'response': 1})
    except Sender.DoesNotExist:
        return Response({'response': 0})


@api_view(['GET'])
def get_estadistics(request):
    oficios_activos = Trades.objects.filter(is_active=True)
    total_oficios = len(oficios_activos)
    deps = Departments.objects.filter(is_active=True)
    rems = Sender.objects.filter(is_active=True)
    departamentos_estadisticas = []
    remitentes_estadisticas = []
    for d in deps:
        departamentos_estadisticas.append({
            'departamento': d.name,
            'numero_oficios': 0
        })
    for r in rems:
        remitentes_estadisticas.append({
            'remitente': r.department,
            'numero_oficios': 0
        })
    for o in oficios_activos:
        for d in departamentos_estadisticas:
            if o.departament.name == d['departamento']:
                d['numero_oficios'] = d['numero_oficios'] + 1
        for r in remitentes_estadisticas:
            if o.sender.department == r['remitente']:
                r['numero_oficios'] = r['numero_oficios'] + 1
    return Response({'oficios_total': total_oficios, 'departamentos_total': departamentos_estadisticas,
                     'remitentes_total': remitentes_estadisticas})


@api_view(['POST'])
def get_estadistics_filtro(request):
    fecha_inicio = request.data['fecha_inicio']
    fecha_fin = request.data['fecha_fin']
    oficios_activos = Trades.objects.filter(is_active=True, date_trades__range=(fecha_inicio, fecha_fin))
    total_oficios = len(oficios_activos)
    deps = Departments.objects.filter(is_active=True)
    rems = Sender.objects.filter(is_active=True)
    departamentos_estadisticas = []
    remitentes_estadisticas = []
    for d in deps:
        departamentos_estadisticas.append({
            'departamento': d.name,
            'numero_oficios': 0
        })
    for r in rems:
        remitentes_estadisticas.append({
            'remitente': r.department,
            'numero_oficios': 0
        })
    for o in oficios_activos:
        for d in departamentos_estadisticas:
            if o.departament.name == d['departamento']:
                d['numero_oficios'] = d['numero_oficios'] + 1
        for r in remitentes_estadisticas:
            if o.sender.department == r['remitente']:
                r['numero_oficios'] = r['numero_oficios'] + 1
    return Response({'oficios_total': total_oficios, 'departamentos_total': departamentos_estadisticas,
                     'remitentes_total': remitentes_estadisticas})


@api_view(['POST'])
def get_oficios_filtro(request):
    fecha_inicio = request.data['fecha_inicio']
    fecha_fin = request.data['fecha_fin']
    departament_id = request.data['departamento_id']
    sender_id = request.data['remitente_id']
    response = []

    if fecha_inicio != "" and fecha_fin != "" and departament_id != "" and sender_id != "":
        oficios = Trades.objects.filter(is_active=True, date_trades__range=(fecha_inicio, fecha_fin), departament__exact=departament_id, sender__exact= sender_id)
        for oficio in oficios:
            response.append({
                'fecha_oficio': oficio.date_trades,
                'descripcion': oficio.description,
                'folio': oficio.folio,
                'observaciones': oficio.observations,
                'departamentos': oficio.departament.name,
                'remitente': oficio.sender.department,
                'fecha_registro': oficio.register_date,
                'id': oficio.pk
            })
    else:
        if fecha_inicio != "" and fecha_fin != "":
            oficios = Trades.objects.filter(is_active=True, date_trades__range=(fecha_inicio, fecha_fin))
            for oficio in oficios:
                response.append({
                    'fecha_oficio': oficio.date_trades,
                    'descripcion': oficio.description,
                    'folio': oficio.folio,
                    'observaciones': oficio.observations,
                    'departamentos': oficio.departament.name,
                    'remitente': oficio.sender.department,
                    'fecha_registro': oficio.register_date,
                    'id': oficio.pk
                })
        else:
            if departament_id != "":
                dep = Trades.objects.filter(is_active=True, departament__exact=departament_id)
                for oficio in dep:
                    response.append({
                        'fecha_oficio': oficio.date_trades,
                        'descripcion': oficio.description,
                        'folio': oficio.folio,
                        'observaciones': oficio.observations,
                        'departamentos': oficio.departament.name,
                        'remitente': oficio.sender.department,
                        'fecha_registro': oficio.register_date,
                        'id': oficio.pk
                    })
            else:
                if sender_id != "":
                    rem = Trades.objects.filter(is_active=True, sender__exact=sender_id)
                    for oficio in rem:
                        response.append({
                            'fecha_oficio': oficio.date_trades,
                            'descripcion': oficio.description,
                            'folio': oficio.folio,
                            'observaciones': oficio.observations,
                            'departamentos': oficio.departament.name,
                            'remitente': oficio.sender.department,
                            'fecha_registro': oficio.register_date,
                            'id': oficio.pk
                        })
                else:
                    if fecha_inicio != "" and fecha_fin != "" and departament_id != "" and sender_id == "":
                        oficios = Trades.objects.filter(is_active=True, date_trades__range=(fecha_inicio, fecha_fin),
                                                        departament__exact=departament_id)
                        for oficio in oficios:
                            response.append({
                                'fecha_oficio': oficio.date_trades,
                                'descripcion': oficio.description,
                                'folio': oficio.folio,
                                'observaciones': oficio.observations,
                                'departamentos': oficio.departament.name,
                                'remitente': oficio.sender.department,
                                'fecha_registro': oficio.register_date,
                                'id': oficio.pk
                            })
                    else:
                        if fecha_inicio != "" and fecha_fin != "" and departament_id == "" and sender_id != "":
                            oficios = Trades.objects.filter(is_active=True,
                                                            date_trades__range=(fecha_inicio, fecha_fin),
                                                            sender__exact=sender_id)
                            for oficio in oficios:
                                response.append({
                                    'fecha_oficio': oficio.date_trades,
                                    'descripcion': oficio.description,
                                    'folio': oficio.folio,
                                    'observaciones': oficio.observations,
                                    'departamentos': oficio.departament.name,
                                    'remitente': oficio.sender.department,
                                    'fecha_registro': oficio.register_date,
                                    'id': oficio.pk
                                })
                        else:
                            if fecha_inicio == "" and fecha_fin == "" and departament_id != "" and sender_id != "":
                                oficios = Trades.objects.filter(is_active=True,
                                                                departament__exact=departament_id,
                                                                sender__exact=sender_id)
                                for oficio in oficios:
                                    response.append({
                                        'fecha_oficio': oficio.date_trades,
                                        'descripcion': oficio.description,
                                        'folio': oficio.folio,
                                        'observaciones': oficio.observations,
                                        'departamentos': oficio.departament.name,
                                        'remitente': oficio.sender.department,
                                        'fecha_registro': oficio.register_date,
                                        'id': oficio.pk
                                    })


    return Response({'oficios': response})
