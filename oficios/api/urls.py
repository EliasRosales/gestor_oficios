from django.conf.urls import url

from oficios.api.views import get_oficios, get_departamentos, get_remitentes, get_oficios_by_id, \
    get_departamentos_by_id, get_remitentes_by_id, set_oficio, set_departamento, set_remitente, \
    delete_departamento, delete_oficio, delete_remitente, update_departamento, update_oficio, \
    update_remitente, get_estadistics

urlpatterns = [
    url(r'^get_oficios/$', get_oficios),
    url(r'^get_departamentos/$', get_departamentos),
    url(r'^get_remitentes/$', get_remitentes),
    url(r'^get_oficios_by_id/$', get_oficios_by_id),
    url(r'^get_departamentos_by_id/$', get_departamentos_by_id),
    url(r'^get_remitentes_by_id/$', get_remitentes_by_id),
    url(r'^set_departamento/$', set_departamento),
    url(r'^set_oficio/$', set_oficio),
    url(r'^set_remitente/$', set_remitente),
    url(r'^delete_departamento/$', delete_departamento),
    url(r'^delete_oficio/$', delete_oficio),
    url(r'^delete_remitente/$', delete_remitente),
    url(r'^update_departamento/$', update_departamento),
    url(r'^update_oficio/$', update_oficio),
    url(r'^update_remitente/$', update_remitente),
    url(r'^get_estadistics/$', get_estadistics),
]
