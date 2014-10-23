from django.conf.urls import *
from django.contrib import admin
import AuShadha.settings

from dynamic_aushadha_models.views import *
from dynamic_aushadha_models.dijit_widgets.pane import render_dynamic_aushadha_models_pane
from dynamic_aushadha_models.dijit_widgets.tree import render_dynamic_aushadha_models_tree

admin.autodiscover()

urlpatterns = patterns('',

################################ CRUD ##################################
                       url(r'dynamic_aushadha_models/list/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.dynamic_aushadha_models_detail_list',
                           name='dynamic_aushadha_models_detail_list'
                           ),

                       url(r'dynamic_aushadha_models/add/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.dynamic_aushadha_models_detail_add',
                           name='dynamic_aushadha_models_detail_add'
                           ),

                       url(r'dynamic_aushadha_models/edit/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.dynamic_aushadha_models_detail_edit',
                           name='dynamic_aushadha_models_detail_edit'
                           ),

                       url(r'dynamic_aushadha_models/del/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.dynamic_aushadha_models_detail_del',
                           name='dynamic_aushadha_models_detail_del'
                           ),

################################ JSON, UI-PANE & TREE #########################

                      url(r'dynamic_aushadha_models/pane/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.dijit_widgets.pane.render_dynamic_aushadha_models_pane',
                           name='render_dynamic_aushadha_models_pane_with_id'
                           ),

                      url(r'dynamic_aushadha_models/pane/$',
                           'dynamic_aushadha_models.dijit_widgets.pane.render_dynamic_aushadha_models_pane',
                           name='render_dynamic_aushadha_models_pane_without_id'
                           ),

                       url(r'dynamic_aushadha_models/tree/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_tree',
                           name='render_dynamic_aushadha_models_tree_with_id'
                           ),

                       url(r'dynamic_aushadha_models/tree/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_tree',
                           name='render_dynamic_aushadha_models_tree_without_id'
                           ),

                       url(r'dynamic_aushadha_models/json/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_json',
                           name='render_dynamic_aushadha_models_json_without_id'
                           ),

                       url(r'dynamic_aushadha_models/json/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_json',
                           name='render_dynamic_aushadha_models_json_with_id'
                           ),

################################ SUMMARY ###############################

                       url(r'dynamic_aushadha_models/summary/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_summary',
                           name='render_dynamic_aushadha_models_summary_without_id'
                           ),

                       url(r'dynamic_aushadha_models/summary/(?P<id>\d+)/$',
                           'dynamic_aushadha_models.views.render_dynamic_aushadha_models_summary',
                           name='render_dynamic_aushadha_models_summary_with_id'
                           ),

)
