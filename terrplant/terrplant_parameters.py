# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:50:59 2012

@author: JHarston
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
from django import forms
from django.db import models
from django.utils.safestring import mark_safe

SELECT_INCORPORATION = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))

SELECT_DRIFT = (('0.01','0.01'),('0.05','0.05'),('0','0'))

SELECT_RUN = (('0.01','0.01'),('0.02','0.02'),('0.05','0.05'))

class TerrPlantInp(forms.Form):
    chemical_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),label='Chemical Name',initial='Alachlor')
    pc_code = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), label='PC Code',initial='90501')
    use = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), label='Use',initial='Corn')
    application_method = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), label='Application Method',initial='Ground')
    application_form = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}), label='Application Form',initial='Spray')
    solubility = forms.FloatField(label='Solubility in Water (ppm)',initial=240)
    incorporation = forms.ChoiceField(required=True, choices=SELECT_INCORPORATION, label=mark_safe('Incorporation (If incorporation depth is <u>&lt;</u> 1 in, choose 1. If &gt; 1 in, choose #. If <u>&gt;</u> 6 in, choose 6. For Aerial applications, choose 1.)'))    
    application_rate = forms.FloatField(required=True,label='Application rate (lbs ai/A)',initial=4)    
    drift_fraction = forms.ChoiceField(required=True, choices=SELECT_DRIFT, label=mark_safe('Drift Fraction (Liquid application form by ground: 0.01. Liquid application by aerial, airblast or spray chemigation: 0.05. Granular application form: 0.)'),initial=0.01)
    runoff_fraction = forms.ChoiceField(required=True, choices=SELECT_RUN, label=mark_safe('Runoff Fraction (For solubility &lt; 10 ppm, choose 0.01. For solubility 10-100 &lt; ppm, choose 0.02. For solubility &gt; 100 ppm, choose 0.05)'),initial=0.05)
    EC25_for_nonlisted_seedling_emergence_monocot = forms.FloatField(required=True, label=mark_safe('EC<sub>25</sub> for Non-listed Seedling Emergence Monocot'),initial=0.0067)
    EC25_for_nonlisted_seedling_emergence_dicot = forms.FloatField(required=True, label=mark_safe('EC<sub>25</sub> for Non-listed Seedling Emergence Dicot'),initial=0.034)
    NOAEC_for_listed_seedling_emergence_monocot = forms.FloatField(required=True, label=mark_safe('NOAEC for Non-listed Seedling Emergence Monocot'),initial=0.0023)
    NOAEC_for_listed_seedling_emergence_dicot = forms.FloatField(required=True, label=mark_safe('NOAEC for Non-listed Seedling Emergence Dicot'),initial=0.019)
    EC25_for_nonlisted_vegetative_vigor_monocot = forms.FloatField(label=mark_safe('EC<sub>25</sub> for Non-listed Vegetative Vigor Monocot'),initial=0.068)
    EC25_for_nonlisted_vegetative_vigor_dicot = forms.FloatField(label=mark_safe('EC<sub>25</sub> for Non-listed Vegetative Vigor Dicot'),initial=1.4)
    NOAEC_for_listed_vegetative_vigor_monocot = forms.FloatField(label=mark_safe('NOAEC for Non-listed Vegetative Vigor Monocot'),initial=0.037)
    NOAEC_for_listed_vegetative_vigor_dicot = forms.FloatField(label=mark_safe('NOAEC for Non-listed Vegetative Vigor Dicot'),initial=0.67)