# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from oficios.models import Trades, Departments, Sender


@api_view(['GET'])
def get_oficios(request):
    oficios = Trades.objects.filter(is_active=True)
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
        })
    return Response({'departamentos': response})


@api_view((['GET']))
def get_remitentes(request):
    remitentes = Sender.objects.filter(is_active=True)
    response = []
    for remitente in remitentes:
        response.append({
            'nombre': remitente.name,
            'responsable': remitente.responsible,
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
            'departamentos': oficio.departament.name,
            'remitente': oficio.sender.department,
            'fecha_registro': oficio.register_date,
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
            'nombre': remitente.name,
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
    name = request.data['nombre']
    responsible = request.data['responsable']
    Sender.objects.create(name=name, responsible=responsible)
    return Response({'response': 1})


@api_view(['POST'])
def delete_oficio(request):
    try:
        oficio = Trades.objects.get(request.data['oficio_id'])
        oficio.delete_date = datetime.today()
        oficio.is_active = False
        oficio.save()
        return Response({'response': 1})
    except Trades.DoesNotExist:
        return Response({'return': 0})


@api_view(['POST'])
def delete_departamento(request):
    try:
        departamento = Departments.objects.get(request.data['departamento_id'])
        departamento.delete_date = datetime.today()
        departamento.is_active = False
        departamento.save()
        return Response({'response': 1})
    except Trades.DoesNotExist:
        return Response({'return': 0})


@api_view((['POST']))
def delete_remitente(request):
    try:
        remitente = Trades.objects.get(request.data['remitente_id'])
        remitente.delete_date = datetime.today()
        remitente.is_active = False
        remitente.save()
        return Response({'response': 1})
    except Trades.DoesNotExist:
        return Response({'return': 0})


@api_view(['POST'])
def update_oficio(request):
    return Response()


@api_view(['POST'])
def update_departamento(request):
    return Response()


@api_view((['POST']))
def update_remitente(request):
    return Response()


@api_view(['GET'])
def get_estadistics(request):
    return Response()
