# -*- coding: utf-8 -*-

import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import numpy
import cgi
import cgitb
cgitb.enable()
import unittest
from StringIO import StringIO
import cStringIO
import logging 
import csv
from trex2 import trex2_tables
from trex2 import trex2_model

chem_name = []
use = []
formu_name = []
a_i = []
Application_type = []
p_i = []
den = []
m_s_r_p = []
r_s = []
b_w = []
h_l = []
n_a = []
crop_use = []
rate_out = []
day_out = []
ld50_bird = []
lc50_bird = []
NOAEC_bird = []
NOAEL_bird = []
aw_bird_sm = []
aw_bird_md = []
aw_bird_lg = []
Species_of_the_tested_bird = []
tw_bird = []
x = []
ld50_mamm = []
lc50_mamm = []
NOAEC_mamm = []
NOAEL_mamm = []
aw_mamm_sm = []
aw_mamm_md = []
aw_mamm_lg = []
tw_mamm = []

######Pre-defined outputs########

sa_bird_1_s_out=[]
sa_bird_2_s_out=[]
sc_bird_s_out=[]
sa_mamm_1_s_out=[]
sa_mamm_2_s_out=[]
sc_mamm_s_out=[]
sa_bird_1_m_out=[]
sa_bird_2_m_out=[]
sc_bird_m_out=[]
sa_mamm_1_m_out=[]
sa_mamm_2_m_out=[]
sc_mamm_m_out=[]
sa_bird_1_l_out=[]
sa_bird_2_l_out=[]
sc_bird_l_out=[]
sa_mamm_1_l_out=[]
sa_mamm_2_l_out=[]
sc_mamm_l_out=[]


#Table 6.1
EEC_diet_SG_RBG_out=[]
EEC_diet_TG_RBG_out=[]
EEC_diet_BP_RBG_out=[]
EEC_diet_FR_RBG_out=[]
EEC_diet_AR_RBG_out=[]

EEC_diet_SG_RBL_out=[]
EEC_diet_TG_RBL_out=[]
EEC_diet_BP_RBL_out=[]
EEC_diet_FR_RBL_out=[]
EEC_diet_AR_RBL_out=[]

EEC_diet_SG_BG_out=[]
EEC_diet_TG_BG_out=[]
EEC_diet_BP_BG_out=[]
EEC_diet_FR_BG_out=[]
EEC_diet_AR_BG_out=[]

EEC_diet_SG_BL_out=[]
EEC_diet_TG_BL_out=[]
EEC_diet_BP_BL_out=[]
EEC_diet_FR_BL_out=[]
EEC_diet_AR_BL_out=[]

#Table 7
EEC_dose_bird_SG_RBG_sm_out=[]
EEC_dose_bird_SG_RBG_md_out=[]
EEC_dose_bird_SG_RBG_lg_out=[]
EEC_dose_bird_TG_RBG_sm_out=[]
EEC_dose_bird_TG_RBG_md_out=[]
EEC_dose_bird_TG_RBG_lg_out=[]
EEC_dose_bird_BP_RBG_sm_out=[]
EEC_dose_bird_BP_RBG_md_out=[]
EEC_dose_bird_BP_RBG_lg_out=[]
EEC_dose_bird_FP_RBG_sm_out=[]
EEC_dose_bird_FP_RBG_md_out=[]
EEC_dose_bird_FP_RBG_lg_out=[]
EEC_dose_bird_AR_RBG_sm_out=[]
EEC_dose_bird_AR_RBG_md_out=[]
EEC_dose_bird_AR_RBG_lg_out=[]
EEC_dose_bird_SE_RBG_sm_out=[]
EEC_dose_bird_SE_RBG_md_out=[]
EEC_dose_bird_SE_RBG_lg_out=[]

EEC_dose_bird_SG_RBL_sm_out=[]
EEC_dose_bird_SG_RBL_md_out=[]
EEC_dose_bird_SG_RBL_lg_out=[]
EEC_dose_bird_TG_RBL_sm_out=[]
EEC_dose_bird_TG_RBL_md_out=[]
EEC_dose_bird_TG_RBL_lg_out=[]
EEC_dose_bird_BP_RBL_sm_out=[]
EEC_dose_bird_BP_RBL_md_out=[]
EEC_dose_bird_BP_RBL_lg_out=[]
EEC_dose_bird_FP_RBL_sm_out=[]
EEC_dose_bird_FP_RBL_md_out=[]
EEC_dose_bird_FP_RBL_lg_out=[]
EEC_dose_bird_AR_RBL_sm_out=[]
EEC_dose_bird_AR_RBL_md_out=[]
EEC_dose_bird_AR_RBL_lg_out=[]
EEC_dose_bird_SE_RBL_sm_out=[]
EEC_dose_bird_SE_RBL_md_out=[]
EEC_dose_bird_SE_RBL_lg_out=[]

EEC_dose_bird_SG_BG_sm_out=[]
EEC_dose_bird_SG_BG_md_out=[]
EEC_dose_bird_SG_BG_lg_out=[]
EEC_dose_bird_TG_BG_sm_out=[]
EEC_dose_bird_TG_BG_md_out=[]
EEC_dose_bird_TG_BG_lg_out=[]
EEC_dose_bird_BP_BG_sm_out=[]
EEC_dose_bird_BP_BG_md_out=[]
EEC_dose_bird_BP_BG_lg_out=[]
EEC_dose_bird_FP_BG_sm_out=[]
EEC_dose_bird_FP_BG_md_out=[]
EEC_dose_bird_FP_BG_lg_out=[]
EEC_dose_bird_AR_BG_sm_out=[]
EEC_dose_bird_AR_BG_md_out=[]
EEC_dose_bird_AR_BG_lg_out=[]
EEC_dose_bird_SE_BG_sm_out=[]
EEC_dose_bird_SE_BG_md_out=[]
EEC_dose_bird_SE_BG_lg_out=[]

EEC_dose_bird_SG_BL_sm_out=[]
EEC_dose_bird_SG_BL_md_out=[]
EEC_dose_bird_SG_BL_lg_out=[]
EEC_dose_bird_TG_BL_sm_out=[]
EEC_dose_bird_TG_BL_md_out=[]
EEC_dose_bird_TG_BL_lg_out=[]
EEC_dose_bird_BP_BL_sm_out=[]
EEC_dose_bird_BP_BL_md_out=[]
EEC_dose_bird_BP_BL_lg_out=[]
EEC_dose_bird_FP_BL_sm_out=[]
EEC_dose_bird_FP_BL_md_out=[]
EEC_dose_bird_FP_BL_lg_out=[]
EEC_dose_bird_AR_BL_sm_out=[]
EEC_dose_bird_AR_BL_md_out=[]
EEC_dose_bird_AR_BL_lg_out=[]
EEC_dose_bird_SE_BL_sm_out=[]
EEC_dose_bird_SE_BL_md_out=[]
EEC_dose_bird_SE_BL_lg_out=[]

#Table8
ARQ_diet_bird_SG_A_RBG_out=[]
ARQ_diet_bird_SG_C_RBG_out=[]
ARQ_diet_bird_TG_A_RBG_out=[]
ARQ_diet_bird_TG_C_RBG_out=[]
ARQ_diet_bird_BP_A_RBG_out=[]
ARQ_diet_bird_BP_C_RBG_out=[]
ARQ_diet_bird_FP_A_RBG_out=[]
ARQ_diet_bird_FP_C_RBG_out=[]
ARQ_diet_bird_AR_A_RBG_out=[]
ARQ_diet_bird_AR_C_RBG_out=[]

ARQ_diet_bird_SG_A_RBL_out=[]
ARQ_diet_bird_SG_C_RBL_out=[]
ARQ_diet_bird_TG_A_RBL_out=[]
ARQ_diet_bird_TG_C_RBL_out=[]
ARQ_diet_bird_BP_A_RBL_out=[]
ARQ_diet_bird_BP_C_RBL_out=[]
ARQ_diet_bird_FP_A_RBL_out=[]
ARQ_diet_bird_FP_C_RBL_out=[]
ARQ_diet_bird_AR_A_RBL_out=[]
ARQ_diet_bird_AR_C_RBL_out=[]

ARQ_diet_bird_SG_A_BG_out=[]
ARQ_diet_bird_SG_C_BG_out=[]
ARQ_diet_bird_TG_A_BG_out=[]
ARQ_diet_bird_TG_C_BG_out=[]
ARQ_diet_bird_BP_A_BG_out=[]
ARQ_diet_bird_BP_C_BG_out=[]
ARQ_diet_bird_FP_A_BG_out=[]
ARQ_diet_bird_FP_C_BG_out=[]
ARQ_diet_bird_AR_A_BG_out=[]
ARQ_diet_bird_AR_C_BG_out=[]

ARQ_diet_bird_SG_A_BL_out=[]
ARQ_diet_bird_SG_C_BL_out=[]
ARQ_diet_bird_TG_A_BL_out=[]
ARQ_diet_bird_TG_C_BL_out=[]
ARQ_diet_bird_BP_A_BL_out=[]
ARQ_diet_bird_BP_C_BL_out=[]
ARQ_diet_bird_FP_A_BL_out=[]
ARQ_diet_bird_FP_C_BL_out=[]
ARQ_diet_bird_AR_A_BL_out=[]
ARQ_diet_bird_AR_C_BL_out=[]

#Table9
EEC_dose_mamm_SG_sm_RBG_out=[]
EEC_dose_mamm_SG_md_RBG_out=[]
EEC_dose_mamm_SG_lg_RBG_out=[]
EEC_dose_mamm_TG_sm_RBG_out=[]
EEC_dose_mamm_TG_md_RBG_out=[]
EEC_dose_mamm_TG_lg_RBG_out=[]
EEC_dose_mamm_BP_sm_RBG_out=[]
EEC_dose_mamm_BP_md_RBG_out=[]
EEC_dose_mamm_BP_lg_RBG_out=[]
EEC_dose_mamm_FP_sm_RBG_out=[]
EEC_dose_mamm_FP_md_RBG_out=[]
EEC_dose_mamm_FP_lg_RBG_out=[]
EEC_dose_mamm_AR_sm_RBG_out=[]
EEC_dose_mamm_AR_md_RBG_out=[]
EEC_dose_mamm_AR_lg_RBG_out=[]
EEC_dose_mamm_SE_sm_RBG_out=[]
EEC_dose_mamm_SE_md_RBG_out=[]
EEC_dose_mamm_SE_lg_RBG_out=[]

EEC_dose_mamm_SG_sm_RBL_out=[]
EEC_dose_mamm_SG_md_RBL_out=[]
EEC_dose_mamm_SG_lg_RBL_out=[]
EEC_dose_mamm_TG_sm_RBL_out=[]
EEC_dose_mamm_TG_md_RBL_out=[]
EEC_dose_mamm_TG_lg_RBL_out=[]
EEC_dose_mamm_BP_sm_RBL_out=[]
EEC_dose_mamm_BP_md_RBL_out=[]
EEC_dose_mamm_BP_lg_RBL_out=[]
EEC_dose_mamm_FP_sm_RBL_out=[]
EEC_dose_mamm_FP_md_RBL_out=[]
EEC_dose_mamm_FP_lg_RBL_out=[]
EEC_dose_mamm_AR_sm_RBL_out=[]
EEC_dose_mamm_AR_md_RBL_out=[]
EEC_dose_mamm_AR_lg_RBL_out=[]
EEC_dose_mamm_SE_sm_RBL_out=[]
EEC_dose_mamm_SE_md_RBL_out=[]
EEC_dose_mamm_SE_lg_RBL_out=[]

EEC_dose_mamm_SG_sm_BG_out=[]
EEC_dose_mamm_SG_md_BG_out=[]
EEC_dose_mamm_SG_lg_BG_out=[]
EEC_dose_mamm_TG_sm_BG_out=[]
EEC_dose_mamm_TG_md_BG_out=[]
EEC_dose_mamm_TG_lg_BG_out=[]
EEC_dose_mamm_BP_sm_BG_out=[]
EEC_dose_mamm_BP_md_BG_out=[]
EEC_dose_mamm_BP_lg_BG_out=[]
EEC_dose_mamm_FP_sm_BG_out=[]
EEC_dose_mamm_FP_md_BG_out=[]
EEC_dose_mamm_FP_lg_BG_out=[]
EEC_dose_mamm_AR_sm_BG_out=[]
EEC_dose_mamm_AR_md_BG_out=[]
EEC_dose_mamm_AR_lg_BG_out=[]
EEC_dose_mamm_SE_sm_BG_out=[]
EEC_dose_mamm_SE_md_BG_out=[]
EEC_dose_mamm_SE_lg_BG_out=[]

EEC_dose_mamm_SG_sm_BL_out=[]
EEC_dose_mamm_SG_md_BL_out=[]
EEC_dose_mamm_SG_lg_BL_out=[]
EEC_dose_mamm_TG_sm_BL_out=[]
EEC_dose_mamm_TG_md_BL_out=[]
EEC_dose_mamm_TG_lg_BL_out=[]
EEC_dose_mamm_BP_sm_BL_out=[]
EEC_dose_mamm_BP_md_BL_out=[]
EEC_dose_mamm_BP_lg_BL_out=[]
EEC_dose_mamm_FP_sm_BL_out=[]
EEC_dose_mamm_FP_md_BL_out=[]
EEC_dose_mamm_FP_lg_BL_out=[]
EEC_dose_mamm_AR_sm_BL_out=[]
EEC_dose_mamm_AR_md_BL_out=[]
EEC_dose_mamm_AR_lg_BL_out=[]
EEC_dose_mamm_SE_sm_BL_out=[]
EEC_dose_mamm_SE_md_BL_out=[]
EEC_dose_mamm_SE_lg_BL_out=[]

#Table 10
ARQ_dose_mamm_SG_sm_RBG_out=[]
CRQ_dose_mamm_SG_sm_RBG_out=[]
ARQ_dose_mamm_SG_md_RBG_out=[]
CRQ_dose_mamm_SG_md_RBG_out=[]
ARQ_dose_mamm_SG_lg_RBG_out=[]
CRQ_dose_mamm_SG_lg_RBG_out=[]
ARQ_dose_mamm_TG_sm_RBG_out=[]
CRQ_dose_mamm_TG_sm_RBG_out=[]
ARQ_dose_mamm_TG_md_RBG_out=[]
CRQ_dose_mamm_TG_md_RBG_out=[]
ARQ_dose_mamm_TG_lg_RBG_out=[]
CRQ_dose_mamm_TG_lg_RBG_out=[]
ARQ_dose_mamm_BP_sm_RBG_out=[]
CRQ_dose_mamm_BP_sm_RBG_out=[]
ARQ_dose_mamm_BP_md_RBG_out=[]
CRQ_dose_mamm_BP_md_RBG_out=[]
ARQ_dose_mamm_BP_lg_RBG_out=[]
CRQ_dose_mamm_BP_lg_RBG_out=[]
ARQ_dose_mamm_FP_sm_RBG_out=[]
CRQ_dose_mamm_FP_sm_RBG_out=[]
ARQ_dose_mamm_FP_md_RBG_out=[]
CRQ_dose_mamm_FP_md_RBG_out=[]
ARQ_dose_mamm_FP_lg_RBG_out=[]
CRQ_dose_mamm_FP_lg_RBG_out=[]
ARQ_dose_mamm_AR_sm_RBG_out=[]
CRQ_dose_mamm_AR_sm_RBG_out=[]
ARQ_dose_mamm_AR_md_RBG_out=[]
CRQ_dose_mamm_AR_md_RBG_out=[]
ARQ_dose_mamm_AR_lg_RBG_out=[]
CRQ_dose_mamm_AR_lg_RBG_out=[]
ARQ_dose_mamm_SE_sm_RBG_out=[]
CRQ_dose_mamm_SE_sm_RBG_out=[]
ARQ_dose_mamm_SE_md_RBG_out=[]
CRQ_dose_mamm_SE_md_RBG_out=[]
ARQ_dose_mamm_SE_lg_RBG_out=[]
CRQ_dose_mamm_SE_lg_RBG_out=[]

ARQ_dose_mamm_SG_sm_RBL_out=[]
CRQ_dose_mamm_SG_sm_RBL_out=[]
ARQ_dose_mamm_SG_md_RBL_out=[]
CRQ_dose_mamm_SG_md_RBL_out=[]
ARQ_dose_mamm_SG_lg_RBL_out=[]
CRQ_dose_mamm_SG_lg_RBL_out=[]
ARQ_dose_mamm_TG_sm_RBL_out=[]
CRQ_dose_mamm_TG_sm_RBL_out=[]
ARQ_dose_mamm_TG_md_RBL_out=[]
CRQ_dose_mamm_TG_md_RBL_out=[]
ARQ_dose_mamm_TG_lg_RBL_out=[]
CRQ_dose_mamm_TG_lg_RBL_out=[]
ARQ_dose_mamm_BP_sm_RBL_out=[]
CRQ_dose_mamm_BP_sm_RBL_out=[]
ARQ_dose_mamm_BP_md_RBL_out=[]
CRQ_dose_mamm_BP_md_RBL_out=[]
ARQ_dose_mamm_BP_lg_RBL_out=[]
CRQ_dose_mamm_BP_lg_RBL_out=[]
ARQ_dose_mamm_FP_sm_RBL_out=[]
CRQ_dose_mamm_FP_sm_RBL_out=[]
ARQ_dose_mamm_FP_md_RBL_out=[]
CRQ_dose_mamm_FP_md_RBL_out=[]
ARQ_dose_mamm_FP_lg_RBL_out=[]
CRQ_dose_mamm_FP_lg_RBL_out=[]
ARQ_dose_mamm_AR_sm_RBL_out=[]
CRQ_dose_mamm_AR_sm_RBL_out=[]
ARQ_dose_mamm_AR_md_RBL_out=[]
CRQ_dose_mamm_AR_md_RBL_out=[]
ARQ_dose_mamm_AR_lg_RBL_out=[]
CRQ_dose_mamm_AR_lg_RBL_out=[]
ARQ_dose_mamm_SE_sm_RBL_out=[]
CRQ_dose_mamm_SE_sm_RBL_out=[]
ARQ_dose_mamm_SE_md_RBL_out=[]
CRQ_dose_mamm_SE_md_RBL_out=[]
ARQ_dose_mamm_SE_lg_RBL_out=[]
CRQ_dose_mamm_SE_lg_RBL_out=[]

ARQ_dose_mamm_SG_sm_BG_out=[]
CRQ_dose_mamm_SG_sm_BG_out=[]
ARQ_dose_mamm_SG_md_BG_out=[]
CRQ_dose_mamm_SG_md_BG_out=[]
ARQ_dose_mamm_SG_lg_BG_out=[]
CRQ_dose_mamm_SG_lg_BG_out=[]
ARQ_dose_mamm_TG_sm_BG_out=[]
CRQ_dose_mamm_TG_sm_BG_out=[]
ARQ_dose_mamm_TG_md_BG_out=[]
CRQ_dose_mamm_TG_md_BG_out=[]
ARQ_dose_mamm_TG_lg_BG_out=[]
CRQ_dose_mamm_TG_lg_BG_out=[]
ARQ_dose_mamm_BP_sm_BG_out=[]
CRQ_dose_mamm_BP_sm_BG_out=[]
ARQ_dose_mamm_BP_md_BG_out=[]
CRQ_dose_mamm_BP_md_BG_out=[]
ARQ_dose_mamm_BP_lg_BG_out=[]
CRQ_dose_mamm_BP_lg_BG_out=[]
ARQ_dose_mamm_FP_sm_BG_out=[]
CRQ_dose_mamm_FP_sm_BG_out=[]
ARQ_dose_mamm_FP_md_BG_out=[]
CRQ_dose_mamm_FP_md_BG_out=[]
ARQ_dose_mamm_FP_lg_BG_out=[]
CRQ_dose_mamm_FP_lg_BG_out=[]
ARQ_dose_mamm_AR_sm_BG_out=[]
CRQ_dose_mamm_AR_sm_BG_out=[]
ARQ_dose_mamm_AR_md_BG_out=[]
CRQ_dose_mamm_AR_md_BG_out=[]
ARQ_dose_mamm_AR_lg_BG_out=[]
CRQ_dose_mamm_AR_lg_BG_out=[]
ARQ_dose_mamm_SE_sm_BG_out=[]
CRQ_dose_mamm_SE_sm_BG_out=[]
ARQ_dose_mamm_SE_md_BG_out=[]
CRQ_dose_mamm_SE_md_BG_out=[]
ARQ_dose_mamm_SE_lg_BG_out=[]
CRQ_dose_mamm_SE_lg_BG_out=[]

ARQ_dose_mamm_SG_sm_BL_out=[]
CRQ_dose_mamm_SG_sm_BL_out=[]
ARQ_dose_mamm_SG_md_BL_out=[]
CRQ_dose_mamm_SG_md_BL_out=[]
ARQ_dose_mamm_SG_lg_BL_out=[]
CRQ_dose_mamm_SG_lg_BL_out=[]
ARQ_dose_mamm_TG_sm_BL_out=[]
CRQ_dose_mamm_TG_sm_BL_out=[]
ARQ_dose_mamm_TG_md_BL_out=[]
CRQ_dose_mamm_TG_md_BL_out=[]
ARQ_dose_mamm_TG_lg_BL_out=[]
CRQ_dose_mamm_TG_lg_BL_out=[]
ARQ_dose_mamm_BP_sm_BL_out=[]
CRQ_dose_mamm_BP_sm_BL_out=[]
ARQ_dose_mamm_BP_md_BL_out=[]
CRQ_dose_mamm_BP_md_BL_out=[]
ARQ_dose_mamm_BP_lg_BL_out=[]
CRQ_dose_mamm_BP_lg_BL_out=[]
ARQ_dose_mamm_FP_sm_BL_out=[]
CRQ_dose_mamm_FP_sm_BL_out=[]
ARQ_dose_mamm_FP_md_BL_out=[]
CRQ_dose_mamm_FP_md_BL_out=[]
ARQ_dose_mamm_FP_lg_BL_out=[]
CRQ_dose_mamm_FP_lg_BL_out=[]
ARQ_dose_mamm_AR_sm_BL_out=[]
CRQ_dose_mamm_AR_sm_BL_out=[]
ARQ_dose_mamm_AR_md_BL_out=[]
CRQ_dose_mamm_AR_md_BL_out=[]
ARQ_dose_mamm_AR_lg_BL_out=[]
CRQ_dose_mamm_AR_lg_BL_out=[]
ARQ_dose_mamm_SE_sm_BL_out=[]
CRQ_dose_mamm_SE_sm_BL_out=[]
ARQ_dose_mamm_SE_md_BL_out=[]
CRQ_dose_mamm_SE_md_BL_out=[]
ARQ_dose_mamm_SE_lg_BL_out=[]
CRQ_dose_mamm_SE_lg_BL_out=[]

#Table 11
ARQ_diet_mamm_SG_RBG_out=[]
CRQ_diet_mamm_SG_RBG_out=[]
ARQ_diet_mamm_TG_RBG_out=[]
CRQ_diet_mamm_TG_RBG_out=[]
ARQ_diet_mamm_BP_RBG_out=[]
CRQ_diet_mamm_BP_RBG_out=[]
ARQ_diet_mamm_FP_RBG_out=[]
CRQ_diet_mamm_FP_RBG_out=[]
ARQ_diet_mamm_AR_RBG_out=[]
CRQ_diet_mamm_AR_RBG_out=[]

ARQ_diet_mamm_SG_RBL_out=[]
CRQ_diet_mamm_SG_RBL_out=[]
ARQ_diet_mamm_TG_RBL_out=[]
CRQ_diet_mamm_TG_RBL_out=[]
ARQ_diet_mamm_BP_RBL_out=[]
CRQ_diet_mamm_BP_RBL_out=[]
ARQ_diet_mamm_FP_RBL_out=[]
CRQ_diet_mamm_FP_RBL_out=[]
ARQ_diet_mamm_AR_RBL_out=[]
CRQ_diet_mamm_AR_RBL_out=[]

ARQ_diet_mamm_SG_BG_out=[]
CRQ_diet_mamm_SG_BG_out=[]
ARQ_diet_mamm_TG_BG_out=[]
CRQ_diet_mamm_TG_BG_out=[]
ARQ_diet_mamm_BP_BG_out=[]
CRQ_diet_mamm_BP_BG_out=[]
ARQ_diet_mamm_FP_BG_out=[]
CRQ_diet_mamm_FP_BG_out=[]
ARQ_diet_mamm_AR_BG_out=[]
CRQ_diet_mamm_AR_BG_out=[]

ARQ_diet_mamm_SG_BL_out=[]
CRQ_diet_mamm_SG_BL_out=[]
ARQ_diet_mamm_TG_BL_out=[]
CRQ_diet_mamm_TG_BL_out=[]
ARQ_diet_mamm_BP_BL_out=[]
CRQ_diet_mamm_BP_BL_out=[]
ARQ_diet_mamm_FP_BL_out=[]
CRQ_diet_mamm_FP_BL_out=[]
ARQ_diet_mamm_AR_BL_out=[]
CRQ_diet_mamm_AR_BL_out=[]

#Table 12
LD50_rg_bird_sm_out=[]
LD50_rg_mamm_sm_out=[]
LD50_rg_bird_md_out=[]
LD50_rg_mamm_md_out=[]
LD50_rg_bird_lg_out=[]
LD50_rg_mamm_lg_out=[]

#Table 13
LD50_rl_bird_sm_out=[]
LD50_rl_mamm_sm_out=[]
LD50_rl_bird_md_out=[]
LD50_rl_mamm_md_out=[]
LD50_rl_bird_lg_out=[]
LD50_rl_mamm_lg_out=[]

#Table 14
LD50_bg_bird_sm_out=[]
LD50_bg_mamm_sm_out=[]
LD50_bg_bird_md_out=[]
LD50_bg_mamm_md_out=[]
LD50_bg_bird_lg_out=[]
LD50_bg_mamm_lg_out=[]

#Table 15
LD50_bl_bird_sm_out=[]
LD50_bl_mamm_sm_out=[]
LD50_bl_bird_md_out=[]
LD50_bl_mamm_md_out=[]
LD50_bl_bird_lg_out=[]
LD50_bl_mamm_lg_out=[]

def html_table(row_inp,iter):
###Inputs###########
    chem_name_temp = str(row_inp[0])
    chem_name.append(chem_name_temp)
    use_temp = str(row_inp[1])
    use.append(use_temp)
    formu_name_temp = str(row_inp[2])
    formu_name.append(formu_name_temp)
    a_i_temp = float(row_inp[3])/100
    a_i.append(a_i_temp)
    Application_type_temp = str(row_inp[4])
    Application_type.append(Application_type_temp)
    p_i_temp = float(row_inp[5])/100
    p_i.append(p_i_temp)
    den_temp = float(row_inp[6])
    den.append(den_temp)
    m_s_r_p_temp = float(row_inp[7])
    m_s_r_p.append(m_s_r_p_temp)
    r_s_temp = float(row_inp[8])
    r_s.append(r_s_temp)
    b_w_temp = float(row_inp[9])
    b_w.append(b_w_temp)
    h_l_temp = float(row_inp[10])
    h_l.append(h_l_temp)
    crop_use_temp = str(row_inp[12])
    crop_use.append(crop_use_temp)
    n_a_temp = float(row_inp[11])
    n_a.append(n_a_temp)
    rate_out_temp = row_inp[13]
    rate_out_temp=rate_out_temp.split(',')
    rate_out_temp=[float(i) for i in rate_out_temp]
    rate_out.append(rate_out_temp)
    day_out_temp = str(row_inp[14])
    day_out_temp=day_out_temp.split(',')
    day_out_temp=[float(i) for i in day_out_temp]
    day_out.append(day_out_temp)
    ld50_bird_temp = float(row_inp[15])
    ld50_bird.append(ld50_bird_temp)
    lc50_bird_temp = float(row_inp[16])
    lc50_bird.append(lc50_bird_temp)
    NOAEC_bird_temp = float(row_inp[17])
    NOAEC_bird.append(NOAEC_bird_temp)
    NOAEL_bird_temp = float(row_inp[18])
    NOAEL_bird.append(NOAEL_bird_temp)
    aw_bird_sm_temp = float(row_inp[19])
    aw_bird_sm.append(aw_bird_sm_temp)
    aw_bird_md_temp = float(row_inp[20])
    aw_bird_md.append(aw_bird_md_temp)
    aw_bird_lg_temp = float(row_inp[21])
    aw_bird_lg.append(aw_bird_lg_temp)
    Species_of_the_tested_bird_temp = str(row_inp[22])
    Species_of_the_tested_bird.append(Species_of_the_tested_bird_temp)
    tw_bird_temp = float(row_inp[23])
    tw_bird.append(tw_bird_temp)
    x_temp = float(row_inp[24])
    x.append(x_temp)
    ld50_mamm_temp = float(row_inp[25])
    ld50_mamm.append(ld50_mamm_temp)
    lc50_mamm_temp = float(row_inp[26])
    lc50_mamm.append(lc50_mamm_temp)
    NOAEC_mamm_temp = float(row_inp[27])
    NOAEC_mamm.append(NOAEC_mamm_temp)
    NOAEL_mamm_temp = float(row_inp[28])
    NOAEL_mamm.append(NOAEL_mamm_temp)
    aw_mamm_sm_temp = float(row_inp[29])
    aw_mamm_sm.append(aw_mamm_sm_temp)
    aw_mamm_md_temp = float(row_inp[30])
    aw_mamm_md.append(aw_mamm_md_temp)
    aw_mamm_lg_temp = float(row_inp[31])
    aw_mamm_lg.append(aw_mamm_lg_temp)
    tw_mamm_temp = float(row_inp[32])
    tw_mamm.append(tw_mamm_temp)

    if Application_type_temp == 'Seed Treatment':
        a_r_p_temp = rate_out_temp[0]
    else:
        a_r_p_temp = 0

    Input_header="""<table border="1">
                        <tr><H3>Batch Calculation of Iteration %s</H3></tr><br>
                    </table>"""%(iter)

    trex2_obj_temp = trex2_model.trex2(chem_name_temp, use_temp, formu_name_temp, a_i_temp, Application_type_temp, r_s_temp, b_w_temp, a_r_p_temp, p_i_temp, den_temp, h_l_temp, n_a_temp, rate_out_temp, day_out_temp,
                    ld50_bird_temp, lc50_bird_temp, NOAEC_bird_temp, NOAEL_bird_temp, aw_bird_sm_temp, aw_bird_md_temp, aw_bird_lg_temp, Species_of_the_tested_bird_temp, 
                    tw_bird_temp, x_temp, ld50_mamm_temp, lc50_mamm_temp, NOAEC_mamm_temp, NOAEL_mamm_temp, aw_mamm_sm_temp, aw_mamm_md_temp, aw_mamm_lg_temp, tw_mamm_temp,
                    m_s_r_p_temp)

    table_all_out = trex2_tables.table_all(trex2_obj_temp)
    
    html_table_temp = Input_header + table_all_out[0]


    if Application_type_temp == 'Seed Treatment':
        sa_bird_1_s_temp=table_all_out[1]['sa_bird_1_s']
        sa_bird_1_s_out.append(sa_bird_1_s_temp)
        sa_bird_2_s_temp=table_all_out[1]['sa_bird_2_s']
        sa_bird_2_s_out.append(sa_bird_2_s_temp)
        sc_bird_s_temp=table_all_out[1]['sc_bird_s']
        sc_bird_s_out.append(sc_bird_s_temp)
        sa_mamm_1_s_temp=table_all_out[1]['sa_mamm_1_s']
        sa_mamm_1_s_out.append(sa_mamm_1_s_temp)
        sa_mamm_2_s_temp=table_all_out[1]['sa_mamm_2_s']
        sa_mamm_2_s_out.append(sa_mamm_2_s_temp)
        sc_mamm_s_temp=table_all_out[1]['sc_mamm_s']
        sc_mamm_s_out.append(sc_mamm_s_temp)
        sa_bird_1_m_temp=table_all_out[1]['sa_bird_1_m']
        sa_bird_1_m_out.append(sa_bird_1_m_temp)
        sa_bird_2_m_temp=table_all_out[1]['sa_bird_2_m']
        sa_bird_2_m_out.append(sa_bird_2_m_temp)
        sc_bird_m_temp=table_all_out[1]['sc_bird_m']
        sc_bird_m_out.append(sc_bird_m_temp)
        sa_mamm_1_m_temp=table_all_out[1]['sa_mamm_1_m']
        sa_mamm_1_m_out.append(sa_mamm_1_m_temp)
        sa_mamm_2_m_temp=table_all_out[1]['sa_mamm_2_m']
        sa_mamm_2_m_out.append(sa_mamm_2_m_temp)
        sc_mamm_m_temp=table_all_out[1]['sc_mamm_m']
        sc_mamm_m_out.append(sc_mamm_m_temp)
        sa_bird_1_l_temp=table_all_out[1]['sa_bird_1_l']
        sa_bird_1_l_out.append(sa_bird_1_l_temp)
        sa_bird_2_l_temp=table_all_out[1]['sa_bird_2_l']
        sa_bird_2_l_out.append(sa_bird_2_l_temp)
        sc_bird_l_temp=table_all_out[1]['sc_bird_l']
        sc_bird_l_out.append(sc_bird_l_temp)
        sa_mamm_1_l_temp=table_all_out[1]['sa_mamm_1_l']
        sa_mamm_1_l_out.append(sa_mamm_1_l_temp)
        sa_mamm_2_l_temp=table_all_out[1]['sa_mamm_2_l']
        sa_mamm_2_l_out.append(sa_mamm_2_l_temp)
        sc_mamm_l_temp=table_all_out[1]['sc_mamm_l']
        sc_mamm_l_out.append(sc_mamm_l_temp)


    if Application_type_temp == 'Row/Band/In-furrow-Granular':
        LD50_rg_bird_sm_temp=table_all_out[7]['LD50_rg_bird_sm']
        LD50_rg_bird_sm_out.append(LD50_rg_bird_sm_temp)
        LD50_rg_mamm_sm_temp=table_all_out[7]['LD50_rg_mamm_sm']
        LD50_rg_mamm_sm_out.append(LD50_rg_mamm_sm_temp)
        LD50_rg_bird_md_temp=table_all_out[7]['LD50_rg_bird_md']
        LD50_rg_bird_md_out.append(LD50_rg_bird_md_temp)
        LD50_rg_mamm_md_temp=table_all_out[7]['LD50_rg_mamm_md']
        LD50_rg_mamm_md_out.append(LD50_rg_mamm_md_temp)
        LD50_rg_bird_lg_temp=table_all_out[7]['LD50_rg_bird_lg']
        LD50_rg_bird_lg_out.append(LD50_rg_bird_lg_temp)
        LD50_rg_mamm_lg_temp=table_all_out[7]['LD50_rg_mamm_lg']
        LD50_rg_mamm_lg_out.append(LD50_rg_mamm_lg_temp)

####Table 6##
        EEC_diet_SG_RBG_temp=table_all_out[1]['EEC_diet_SG']
        EEC_diet_SG_RBG_out.append(EEC_diet_SG_RBG_temp)
        EEC_diet_TG_RBG_temp=table_all_out[1]['EEC_diet_TG']
        EEC_diet_TG_RBG_out.append(EEC_diet_TG_RBG_temp)
        EEC_diet_BP_RBG_temp=table_all_out[1]['EEC_diet_BP']
        EEC_diet_BP_RBG_out.append(EEC_diet_BP_RBG_temp)
        EEC_diet_FR_RBG_temp=table_all_out[1]['EEC_diet_FR']
        EEC_diet_FR_RBG_out.append(EEC_diet_FR_RBG_temp)
        EEC_diet_AR_RBG_temp=table_all_out[1]['EEC_diet_AR']
        EEC_diet_AR_RBG_out.append(EEC_diet_AR_RBG_temp)

####Table 7##
        EEC_dose_bird_SG_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_SG_sm']
        EEC_dose_bird_SG_RBG_sm_out.append(EEC_dose_bird_SG_RBG_sm_temp)
        EEC_dose_bird_SG_RBG_md_temp=table_all_out[2]['EEC_dose_bird_SG_md']
        EEC_dose_bird_SG_RBG_md_out.append(EEC_dose_bird_SG_RBG_md_temp)
        EEC_dose_bird_SG_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_SG_lg']
        EEC_dose_bird_SG_RBG_lg_out.append(EEC_dose_bird_SG_RBG_lg_temp)
        EEC_dose_bird_TG_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_TG_sm']
        EEC_dose_bird_TG_RBG_sm_out.append(EEC_dose_bird_TG_RBG_sm_temp)
        EEC_dose_bird_TG_RBG_md_temp=table_all_out[2]['EEC_dose_bird_TG_md']
        EEC_dose_bird_TG_RBG_md_out.append(EEC_dose_bird_TG_RBG_md_temp)
        EEC_dose_bird_TG_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_TG_lg']
        EEC_dose_bird_TG_RBG_lg_out.append(EEC_dose_bird_TG_RBG_lg_temp)
        EEC_dose_bird_BP_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_BP_sm']
        EEC_dose_bird_BP_RBG_sm_out.append(EEC_dose_bird_BP_RBG_sm_temp)
        EEC_dose_bird_BP_RBG_md_temp=table_all_out[2]['EEC_dose_bird_BP_md']
        EEC_dose_bird_BP_RBG_md_out.append(EEC_dose_bird_BP_RBG_md_temp)
        EEC_dose_bird_BP_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_BP_lg']
        EEC_dose_bird_BP_RBG_lg_out.append(EEC_dose_bird_BP_RBG_lg_temp)
        EEC_dose_bird_FP_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_FP_sm']
        EEC_dose_bird_FP_RBG_sm_out.append(EEC_dose_bird_FP_RBG_sm_temp)
        EEC_dose_bird_FP_RBG_md_temp=table_all_out[2]['EEC_dose_bird_FP_md']
        EEC_dose_bird_FP_RBG_md_out.append(EEC_dose_bird_FP_RBG_md_temp)
        EEC_dose_bird_FP_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_FP_lg']
        EEC_dose_bird_FP_RBG_lg_out.append(EEC_dose_bird_FP_RBG_lg_temp)
        EEC_dose_bird_AR_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_AR_sm']
        EEC_dose_bird_AR_RBG_sm_out.append(EEC_dose_bird_AR_RBG_sm_temp)
        EEC_dose_bird_AR_RBG_md_temp=table_all_out[2]['EEC_dose_bird_AR_md']
        EEC_dose_bird_AR_RBG_md_out.append(EEC_dose_bird_AR_RBG_md_temp)
        EEC_dose_bird_AR_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_AR_lg']
        EEC_dose_bird_AR_RBG_lg_out.append(EEC_dose_bird_AR_RBG_lg_temp)
        EEC_dose_bird_SE_RBG_sm_temp=table_all_out[2]['EEC_dose_bird_SE_sm']
        EEC_dose_bird_SE_RBG_sm_out.append(EEC_dose_bird_SE_RBG_sm_temp)
        EEC_dose_bird_SE_RBG_md_temp=table_all_out[2]['EEC_dose_bird_SE_md']
        EEC_dose_bird_SE_RBG_md_out.append(EEC_dose_bird_SE_RBG_md_temp)
        EEC_dose_bird_SE_RBG_lg_temp=table_all_out[2]['EEC_dose_bird_SE_lg']
        EEC_dose_bird_SE_RBG_lg_out.append(EEC_dose_bird_SE_RBG_lg_temp)

###Table 8#######
        ARQ_diet_bird_SG_A_RBG_temp=table_all_out[3]['ARQ_diet_bird_SG_A']
        ARQ_diet_bird_SG_A_RBG_out.append(ARQ_diet_bird_SG_A_RBG_temp)
        ARQ_diet_bird_SG_C_RBG_temp=table_all_out[3]['ARQ_diet_bird_SG_C']
        ARQ_diet_bird_SG_C_RBG_out.append(ARQ_diet_bird_SG_C_RBG_temp)
        ARQ_diet_bird_TG_A_RBG_temp=table_all_out[3]['ARQ_diet_bird_TG_A']
        ARQ_diet_bird_TG_A_RBG_out.append(ARQ_diet_bird_TG_A_RBG_temp)
        ARQ_diet_bird_TG_C_RBG_temp=table_all_out[3]['ARQ_diet_bird_TG_C']
        ARQ_diet_bird_TG_C_RBG_out.append(ARQ_diet_bird_TG_C_RBG_temp)
        ARQ_diet_bird_BP_A_RBG_temp=table_all_out[3]['ARQ_diet_bird_BP_A']
        ARQ_diet_bird_BP_A_RBG_out.append(ARQ_diet_bird_BP_A_RBG_temp)
        ARQ_diet_bird_BP_C_RBG_temp=table_all_out[3]['ARQ_diet_bird_BP_C']
        ARQ_diet_bird_BP_C_RBG_out.append(ARQ_diet_bird_BP_C_RBG_temp)
        ARQ_diet_bird_FP_A_RBG_temp=table_all_out[3]['ARQ_diet_bird_FP_A']
        ARQ_diet_bird_FP_A_RBG_out.append(ARQ_diet_bird_FP_A_RBG_temp)
        ARQ_diet_bird_FP_C_RBG_temp=table_all_out[3]['ARQ_diet_bird_FP_C']
        ARQ_diet_bird_FP_C_RBG_out.append(ARQ_diet_bird_FP_C_RBG_temp)
        ARQ_diet_bird_AR_A_RBG_temp=table_all_out[3]['ARQ_diet_bird_AR_A']
        ARQ_diet_bird_AR_A_RBG_out.append(ARQ_diet_bird_AR_A_RBG_temp)
        ARQ_diet_bird_AR_C_RBG_temp=table_all_out[3]['ARQ_diet_bird_AR_C']
        ARQ_diet_bird_AR_C_RBG_out.append(ARQ_diet_bird_AR_C_RBG_temp)

###Table 9#######
        EEC_dose_mamm_SG_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_SG_sm']
        EEC_dose_mamm_SG_sm_RBG_out.append(EEC_dose_mamm_SG_sm_RBG_temp)
        EEC_dose_mamm_SG_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_SG_md']
        EEC_dose_mamm_SG_md_RBG_out.append(EEC_dose_mamm_SG_md_RBG_temp)
        EEC_dose_mamm_SG_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_SG_lg']
        EEC_dose_mamm_SG_lg_RBG_out.append(EEC_dose_mamm_SG_lg_RBG_temp)
        EEC_dose_mamm_TG_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_TG_sm']
        EEC_dose_mamm_TG_sm_RBG_out.append(EEC_dose_mamm_TG_sm_RBG_temp)
        EEC_dose_mamm_TG_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_TG_md']
        EEC_dose_mamm_TG_md_RBG_out.append(EEC_dose_mamm_TG_md_RBG_temp)
        EEC_dose_mamm_TG_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_TG_lg']
        EEC_dose_mamm_TG_lg_RBG_out.append(EEC_dose_mamm_TG_lg_RBG_temp)
        EEC_dose_mamm_BP_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_BP_sm']
        EEC_dose_mamm_BP_sm_RBG_out.append(EEC_dose_mamm_BP_sm_RBG_temp)
        EEC_dose_mamm_BP_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_BP_md']
        EEC_dose_mamm_BP_md_RBG_out.append(EEC_dose_mamm_BP_md_RBG_temp)
        EEC_dose_mamm_BP_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_BP_lg']
        EEC_dose_mamm_BP_lg_RBG_out.append(EEC_dose_mamm_BP_lg_RBG_temp)
        EEC_dose_mamm_FP_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_FP_sm']
        EEC_dose_mamm_FP_sm_RBG_out.append(EEC_dose_mamm_FP_sm_RBG_temp)
        EEC_dose_mamm_FP_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_FP_md']
        EEC_dose_mamm_FP_md_RBG_out.append(EEC_dose_mamm_FP_md_RBG_temp)
        EEC_dose_mamm_FP_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_FP_lg']
        EEC_dose_mamm_FP_lg_RBG_out.append(EEC_dose_mamm_FP_lg_RBG_temp)
        EEC_dose_mamm_AR_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_AR_sm']
        EEC_dose_mamm_AR_sm_RBG_out.append(EEC_dose_mamm_AR_sm_RBG_temp)
        EEC_dose_mamm_AR_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_AR_md']
        EEC_dose_mamm_AR_md_RBG_out.append(EEC_dose_mamm_AR_md_RBG_temp)
        EEC_dose_mamm_AR_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_AR_lg']
        EEC_dose_mamm_AR_lg_RBG_out.append(EEC_dose_mamm_AR_lg_RBG_temp)
        EEC_dose_mamm_SE_sm_RBG_temp=table_all_out[4]['EEC_dose_mamm_SE_sm']
        EEC_dose_mamm_SE_sm_RBG_out.append(EEC_dose_mamm_SE_sm_RBG_temp)
        EEC_dose_mamm_SE_md_RBG_temp=table_all_out[4]['EEC_dose_mamm_SE_md']
        EEC_dose_mamm_SE_md_RBG_out.append(EEC_dose_mamm_SE_md_RBG_temp)
        EEC_dose_mamm_SE_lg_RBG_temp=table_all_out[4]['EEC_dose_mamm_SE_lg']
        EEC_dose_mamm_SE_lg_RBG_out.append(EEC_dose_mamm_SE_lg_RBG_temp)

###Table 10#######
        ARQ_dose_mamm_SG_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SG_sm']
        ARQ_dose_mamm_SG_sm_RBG_out.append(ARQ_dose_mamm_SG_sm_RBG_temp)
        CRQ_dose_mamm_SG_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SG_sm']
        CRQ_dose_mamm_SG_sm_RBG_out.append(CRQ_dose_mamm_SG_sm_RBG_temp)
        ARQ_dose_mamm_SG_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SG_md']
        ARQ_dose_mamm_SG_md_RBG_out.append(ARQ_dose_mamm_SG_md_RBG_temp)
        CRQ_dose_mamm_SG_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SG_md']
        CRQ_dose_mamm_SG_md_RBG_out.append(CRQ_dose_mamm_SG_md_RBG_temp)
        ARQ_dose_mamm_SG_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SG_lg']
        ARQ_dose_mamm_SG_lg_RBG_out.append(ARQ_dose_mamm_SG_lg_RBG_temp)
        CRQ_dose_mamm_SG_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SG_lg']
        CRQ_dose_mamm_SG_lg_RBG_out.append(CRQ_dose_mamm_SG_lg_RBG_temp)
        ARQ_dose_mamm_TG_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_TG_sm']
        ARQ_dose_mamm_TG_sm_RBG_out.append(ARQ_dose_mamm_TG_sm_RBG_temp)
        CRQ_dose_mamm_TG_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_TG_sm']
        CRQ_dose_mamm_TG_sm_RBG_out.append(CRQ_dose_mamm_TG_sm_RBG_temp)
        ARQ_dose_mamm_TG_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_TG_md']
        ARQ_dose_mamm_TG_md_RBG_out.append(ARQ_dose_mamm_TG_md_RBG_temp)
        CRQ_dose_mamm_TG_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_TG_md']
        CRQ_dose_mamm_TG_md_RBG_out.append(CRQ_dose_mamm_TG_md_RBG_temp)
        ARQ_dose_mamm_TG_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_TG_lg']
        ARQ_dose_mamm_TG_lg_RBG_out.append(ARQ_dose_mamm_TG_lg_RBG_temp)
        CRQ_dose_mamm_TG_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_TG_lg']
        CRQ_dose_mamm_TG_lg_RBG_out.append(CRQ_dose_mamm_TG_lg_RBG_temp)
        ARQ_dose_mamm_BP_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_BP_sm']
        ARQ_dose_mamm_BP_sm_RBG_out.append(ARQ_dose_mamm_BP_sm_RBG_temp)
        CRQ_dose_mamm_BP_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_BP_sm']
        CRQ_dose_mamm_BP_sm_RBG_out.append(CRQ_dose_mamm_BP_sm_RBG_temp)
        ARQ_dose_mamm_BP_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_BP_md']
        ARQ_dose_mamm_BP_md_RBG_out.append(ARQ_dose_mamm_BP_md_RBG_temp)
        CRQ_dose_mamm_BP_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_BP_md']
        CRQ_dose_mamm_BP_md_RBG_out.append(CRQ_dose_mamm_BP_md_RBG_temp)
        ARQ_dose_mamm_BP_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_BP_lg']
        ARQ_dose_mamm_BP_lg_RBG_out.append(ARQ_dose_mamm_BP_lg_RBG_temp)
        CRQ_dose_mamm_BP_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_BP_lg']
        CRQ_dose_mamm_BP_lg_RBG_out.append(CRQ_dose_mamm_BP_lg_RBG_temp)
        ARQ_dose_mamm_FP_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_FP_sm']
        ARQ_dose_mamm_FP_sm_RBG_out.append(ARQ_dose_mamm_FP_sm_RBG_temp)
        CRQ_dose_mamm_FP_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_FP_sm']
        CRQ_dose_mamm_FP_sm_RBG_out.append(CRQ_dose_mamm_FP_sm_RBG_temp)
        ARQ_dose_mamm_FP_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_FP_md']
        ARQ_dose_mamm_FP_md_RBG_out.append(ARQ_dose_mamm_FP_md_RBG_temp)
        CRQ_dose_mamm_FP_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_FP_md']
        CRQ_dose_mamm_FP_md_RBG_out.append(CRQ_dose_mamm_FP_md_RBG_temp)
        ARQ_dose_mamm_FP_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_FP_lg']
        ARQ_dose_mamm_FP_lg_RBG_out.append(ARQ_dose_mamm_FP_lg_RBG_temp)
        CRQ_dose_mamm_FP_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_FP_lg']
        CRQ_dose_mamm_FP_lg_RBG_out.append(CRQ_dose_mamm_FP_lg_RBG_temp)
        ARQ_dose_mamm_AR_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_AR_sm']
        ARQ_dose_mamm_AR_sm_RBG_out.append(ARQ_dose_mamm_AR_sm_RBG_temp)
        CRQ_dose_mamm_AR_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_AR_sm']
        CRQ_dose_mamm_AR_sm_RBG_out.append(CRQ_dose_mamm_AR_sm_RBG_temp)
        ARQ_dose_mamm_AR_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_AR_md']
        ARQ_dose_mamm_AR_md_RBG_out.append(ARQ_dose_mamm_AR_md_RBG_temp)
        CRQ_dose_mamm_AR_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_AR_md']
        CRQ_dose_mamm_AR_md_RBG_out.append(CRQ_dose_mamm_AR_md_RBG_temp)
        ARQ_dose_mamm_AR_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_AR_lg']
        ARQ_dose_mamm_AR_lg_RBG_out.append(ARQ_dose_mamm_AR_lg_RBG_temp)
        CRQ_dose_mamm_AR_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_AR_lg']
        CRQ_dose_mamm_AR_lg_RBG_out.append(CRQ_dose_mamm_AR_lg_RBG_temp)
        ARQ_dose_mamm_SE_sm_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SE_sm']
        ARQ_dose_mamm_SE_sm_RBG_out.append(ARQ_dose_mamm_SE_sm_RBG_temp)
        CRQ_dose_mamm_SE_sm_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SE_sm']
        CRQ_dose_mamm_SE_sm_RBG_out.append(CRQ_dose_mamm_SE_sm_RBG_temp)
        ARQ_dose_mamm_SE_md_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SE_md']
        ARQ_dose_mamm_SE_md_RBG_out.append(ARQ_dose_mamm_SE_md_RBG_temp)
        CRQ_dose_mamm_SE_md_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SE_md']
        CRQ_dose_mamm_SE_md_RBG_out.append(CRQ_dose_mamm_SE_md_RBG_temp)
        ARQ_dose_mamm_SE_lg_RBG_temp=table_all_out[5]['ARQ_dose_mamm_SE_lg']
        ARQ_dose_mamm_SE_lg_RBG_out.append(ARQ_dose_mamm_SE_lg_RBG_temp)
        CRQ_dose_mamm_SE_lg_RBG_temp=table_all_out[5]['CRQ_dose_mamm_SE_lg']
        CRQ_dose_mamm_SE_lg_RBG_out.append(CRQ_dose_mamm_SE_lg_RBG_temp)

###Table 11#######
        ARQ_diet_mamm_SG_RBG_temp=table_all_out[6]['ARQ_diet_mamm_SG']
        ARQ_diet_mamm_SG_RBG_out.append(ARQ_diet_mamm_SG_RBG_temp)
        CRQ_diet_mamm_SG_RBG_temp=table_all_out[6]['CRQ_diet_mamm_SG']
        CRQ_diet_mamm_SG_RBG_out.append(CRQ_diet_mamm_SG_RBG_temp)
        ARQ_diet_mamm_TG_RBG_temp=table_all_out[6]['ARQ_diet_mamm_TG']
        ARQ_diet_mamm_TG_RBG_out.append(ARQ_diet_mamm_TG_RBG_temp)
        CRQ_diet_mamm_TG_RBG_temp=table_all_out[6]['CRQ_diet_mamm_TG']
        CRQ_diet_mamm_TG_RBG_out.append(CRQ_diet_mamm_TG_RBG_temp)
        ARQ_diet_mamm_BP_RBG_temp=table_all_out[6]['ARQ_diet_mamm_BP']
        ARQ_diet_mamm_BP_RBG_out.append(ARQ_diet_mamm_BP_RBG_temp)
        CRQ_diet_mamm_BP_RBG_temp=table_all_out[6]['CRQ_diet_mamm_BP']
        CRQ_diet_mamm_BP_RBG_out.append(CRQ_diet_mamm_BP_RBG_temp)
        ARQ_diet_mamm_FP_RBG_temp=table_all_out[6]['ARQ_diet_mamm_FP']
        ARQ_diet_mamm_FP_RBG_out.append(ARQ_diet_mamm_FP_RBG_temp)
        CRQ_diet_mamm_FP_RBG_temp=table_all_out[6]['CRQ_diet_mamm_FP']
        CRQ_diet_mamm_FP_RBG_out.append(CRQ_diet_mamm_FP_RBG_temp)
        ARQ_diet_mamm_AR_RBG_temp=table_all_out[6]['ARQ_diet_mamm_AR']
        ARQ_diet_mamm_AR_RBG_out.append(ARQ_diet_mamm_AR_RBG_temp)
        CRQ_diet_mamm_AR_RBG_temp=table_all_out[6]['CRQ_diet_mamm_AR']
        CRQ_diet_mamm_AR_RBG_out.append(CRQ_diet_mamm_AR_RBG_temp)

    if Application_type_temp == 'Row/Band/In-furrow-Liquid':
        LD50_rl_bird_sm_temp=table_all_out[7]['LD50_rl_bird_sm']
        LD50_rl_bird_sm_out.append(LD50_rl_bird_sm_temp)
        LD50_rl_mamm_sm_temp=table_all_out[7]['LD50_rl_mamm_sm']
        LD50_rl_mamm_sm_out.append(LD50_rl_mamm_sm_temp)
        LD50_rl_bird_md_temp=table_all_out[7]['LD50_rl_bird_md']
        LD50_rl_bird_md_out.append(LD50_rl_bird_md_temp)
        LD50_rl_mamm_md_temp=table_all_out[7]['LD50_rl_mamm_md']
        LD50_rl_mamm_md_out.append(LD50_rl_mamm_md_temp)
        LD50_rl_bird_lg_temp=table_all_out[7]['LD50_rl_bird_lg']
        LD50_rl_bird_lg_out.append(LD50_rl_bird_lg_temp)
        LD50_rl_mamm_lg_temp=table_all_out[7]['LD50_rl_mamm_lg']
        LD50_rl_mamm_lg_out.append(LD50_rl_mamm_lg_temp)

####Table 6##
        EEC_diet_SG_RBL_temp=table_all_out[1]['EEC_diet_SG']
        EEC_diet_SG_RBL_out.append(EEC_diet_SG_RBL_temp)
        EEC_diet_TG_RBL_temp=table_all_out[1]['EEC_diet_TG']
        EEC_diet_TG_RBL_out.append(EEC_diet_TG_RBL_temp)
        EEC_diet_BP_RBL_temp=table_all_out[1]['EEC_diet_BP']
        EEC_diet_BP_RBL_out.append(EEC_diet_BP_RBL_temp)
        EEC_diet_FR_RBL_temp=table_all_out[1]['EEC_diet_FR']
        EEC_diet_FR_RBL_out.append(EEC_diet_FR_RBL_temp)
        EEC_diet_AR_RBL_temp=table_all_out[1]['EEC_diet_AR']
        EEC_diet_AR_RBL_out.append(EEC_diet_AR_RBL_temp)

####Table 7##
        EEC_dose_bird_SG_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_SG_sm']
        EEC_dose_bird_SG_RBL_sm_out.append(EEC_dose_bird_SG_RBL_sm_temp)
        EEC_dose_bird_SG_RBL_md_temp=table_all_out[2]['EEC_dose_bird_SG_md']
        EEC_dose_bird_SG_RBL_md_out.append(EEC_dose_bird_SG_RBL_md_temp)
        EEC_dose_bird_SG_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_SG_lg']
        EEC_dose_bird_SG_RBL_lg_out.append(EEC_dose_bird_SG_RBL_lg_temp)
        EEC_dose_bird_TG_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_TG_sm']
        EEC_dose_bird_TG_RBL_sm_out.append(EEC_dose_bird_TG_RBL_sm_temp)
        EEC_dose_bird_TG_RBL_md_temp=table_all_out[2]['EEC_dose_bird_TG_md']
        EEC_dose_bird_TG_RBL_md_out.append(EEC_dose_bird_TG_RBL_md_temp)
        EEC_dose_bird_TG_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_TG_lg']
        EEC_dose_bird_TG_RBL_lg_out.append(EEC_dose_bird_TG_RBL_lg_temp)
        EEC_dose_bird_BP_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_BP_sm']
        EEC_dose_bird_BP_RBL_sm_out.append(EEC_dose_bird_BP_RBL_sm_temp)
        EEC_dose_bird_BP_RBL_md_temp=table_all_out[2]['EEC_dose_bird_BP_md']
        EEC_dose_bird_BP_RBL_md_out.append(EEC_dose_bird_BP_RBL_md_temp)
        EEC_dose_bird_BP_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_BP_lg']
        EEC_dose_bird_BP_RBL_lg_out.append(EEC_dose_bird_BP_RBL_lg_temp)
        EEC_dose_bird_FP_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_FP_sm']
        EEC_dose_bird_FP_RBL_sm_out.append(EEC_dose_bird_FP_RBL_sm_temp)
        EEC_dose_bird_FP_RBL_md_temp=table_all_out[2]['EEC_dose_bird_FP_md']
        EEC_dose_bird_FP_RBL_md_out.append(EEC_dose_bird_FP_RBL_md_temp)
        EEC_dose_bird_FP_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_FP_lg']
        EEC_dose_bird_FP_RBL_lg_out.append(EEC_dose_bird_FP_RBL_lg_temp)
        EEC_dose_bird_AR_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_AR_sm']
        EEC_dose_bird_AR_RBL_sm_out.append(EEC_dose_bird_AR_RBL_sm_temp)
        EEC_dose_bird_AR_RBL_md_temp=table_all_out[2]['EEC_dose_bird_AR_md']
        EEC_dose_bird_AR_RBL_md_out.append(EEC_dose_bird_AR_RBL_md_temp)
        EEC_dose_bird_AR_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_AR_lg']
        EEC_dose_bird_AR_RBL_lg_out.append(EEC_dose_bird_AR_RBL_lg_temp)
        EEC_dose_bird_SE_RBL_sm_temp=table_all_out[2]['EEC_dose_bird_SE_sm']
        EEC_dose_bird_SE_RBL_sm_out.append(EEC_dose_bird_SE_RBL_sm_temp)
        EEC_dose_bird_SE_RBL_md_temp=table_all_out[2]['EEC_dose_bird_SE_md']
        EEC_dose_bird_SE_RBL_md_out.append(EEC_dose_bird_SE_RBL_md_temp)
        EEC_dose_bird_SE_RBL_lg_temp=table_all_out[2]['EEC_dose_bird_SE_lg']
        EEC_dose_bird_SE_RBL_lg_out.append(EEC_dose_bird_SE_RBL_lg_temp)

###Table 8#######
        ARQ_diet_bird_SG_A_RBL_temp=table_all_out[3]['ARQ_diet_bird_SG_A']
        ARQ_diet_bird_SG_A_RBL_out.append(ARQ_diet_bird_SG_A_RBL_temp)
        ARQ_diet_bird_SG_C_RBL_temp=table_all_out[3]['ARQ_diet_bird_SG_C']
        ARQ_diet_bird_SG_C_RBL_out.append(ARQ_diet_bird_SG_C_RBL_temp)
        ARQ_diet_bird_TG_A_RBL_temp=table_all_out[3]['ARQ_diet_bird_TG_A']
        ARQ_diet_bird_TG_A_RBL_out.append(ARQ_diet_bird_TG_A_RBL_temp)
        ARQ_diet_bird_TG_C_RBL_temp=table_all_out[3]['ARQ_diet_bird_TG_C']
        ARQ_diet_bird_TG_C_RBL_out.append(ARQ_diet_bird_TG_C_RBL_temp)
        ARQ_diet_bird_BP_A_RBL_temp=table_all_out[3]['ARQ_diet_bird_BP_A']
        ARQ_diet_bird_BP_A_RBL_out.append(ARQ_diet_bird_BP_A_RBL_temp)
        ARQ_diet_bird_BP_C_RBL_temp=table_all_out[3]['ARQ_diet_bird_BP_C']
        ARQ_diet_bird_BP_C_RBL_out.append(ARQ_diet_bird_BP_C_RBL_temp)
        ARQ_diet_bird_FP_A_RBL_temp=table_all_out[3]['ARQ_diet_bird_FP_A']
        ARQ_diet_bird_FP_A_RBL_out.append(ARQ_diet_bird_FP_A_RBL_temp)
        ARQ_diet_bird_FP_C_RBL_temp=table_all_out[3]['ARQ_diet_bird_FP_C']
        ARQ_diet_bird_FP_C_RBL_out.append(ARQ_diet_bird_FP_C_RBL_temp)
        ARQ_diet_bird_AR_A_RBL_temp=table_all_out[3]['ARQ_diet_bird_AR_A']
        ARQ_diet_bird_AR_A_RBL_out.append(ARQ_diet_bird_AR_A_RBL_temp)
        ARQ_diet_bird_AR_C_RBL_temp=table_all_out[3]['ARQ_diet_bird_AR_C']
        ARQ_diet_bird_AR_C_RBL_out.append(ARQ_diet_bird_AR_C_RBL_temp)

###Table 9#######
        EEC_dose_mamm_SG_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_SG_sm']
        EEC_dose_mamm_SG_sm_RBL_out.append(EEC_dose_mamm_SG_sm_RBL_temp)
        EEC_dose_mamm_SG_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_SG_md']
        EEC_dose_mamm_SG_md_RBL_out.append(EEC_dose_mamm_SG_md_RBL_temp)
        EEC_dose_mamm_SG_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_SG_lg']
        EEC_dose_mamm_SG_lg_RBL_out.append(EEC_dose_mamm_SG_lg_RBL_temp)
        EEC_dose_mamm_TG_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_TG_sm']
        EEC_dose_mamm_TG_sm_RBL_out.append(EEC_dose_mamm_TG_sm_RBL_temp)
        EEC_dose_mamm_TG_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_TG_md']
        EEC_dose_mamm_TG_md_RBL_out.append(EEC_dose_mamm_TG_md_RBL_temp)
        EEC_dose_mamm_TG_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_TG_lg']
        EEC_dose_mamm_TG_lg_RBL_out.append(EEC_dose_mamm_TG_lg_RBL_temp)
        EEC_dose_mamm_BP_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_BP_sm']
        EEC_dose_mamm_BP_sm_RBL_out.append(EEC_dose_mamm_BP_sm_RBL_temp)
        EEC_dose_mamm_BP_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_BP_md']
        EEC_dose_mamm_BP_md_RBL_out.append(EEC_dose_mamm_BP_md_RBL_temp)
        EEC_dose_mamm_BP_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_BP_lg']
        EEC_dose_mamm_BP_lg_RBL_out.append(EEC_dose_mamm_BP_lg_RBL_temp)
        EEC_dose_mamm_FP_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_FP_sm']
        EEC_dose_mamm_FP_sm_RBL_out.append(EEC_dose_mamm_FP_sm_RBL_temp)
        EEC_dose_mamm_FP_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_FP_md']
        EEC_dose_mamm_FP_md_RBL_out.append(EEC_dose_mamm_FP_md_RBL_temp)
        EEC_dose_mamm_FP_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_FP_lg']
        EEC_dose_mamm_FP_lg_RBL_out.append(EEC_dose_mamm_FP_lg_RBL_temp)
        EEC_dose_mamm_AR_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_AR_sm']
        EEC_dose_mamm_AR_sm_RBL_out.append(EEC_dose_mamm_AR_sm_RBL_temp)
        EEC_dose_mamm_AR_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_AR_md']
        EEC_dose_mamm_AR_md_RBL_out.append(EEC_dose_mamm_AR_md_RBL_temp)
        EEC_dose_mamm_AR_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_AR_lg']
        EEC_dose_mamm_AR_lg_RBL_out.append(EEC_dose_mamm_AR_lg_RBL_temp)
        EEC_dose_mamm_SE_sm_RBL_temp=table_all_out[4]['EEC_dose_mamm_SE_sm']
        EEC_dose_mamm_SE_sm_RBL_out.append(EEC_dose_mamm_SE_sm_RBL_temp)
        EEC_dose_mamm_SE_md_RBL_temp=table_all_out[4]['EEC_dose_mamm_SE_md']
        EEC_dose_mamm_SE_md_RBL_out.append(EEC_dose_mamm_SE_md_RBL_temp)
        EEC_dose_mamm_SE_lg_RBL_temp=table_all_out[4]['EEC_dose_mamm_SE_lg']
        EEC_dose_mamm_SE_lg_RBL_out.append(EEC_dose_mamm_SE_lg_RBL_temp)

###Table 10#######
        ARQ_dose_mamm_SG_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SG_sm']
        ARQ_dose_mamm_SG_sm_RBL_out.append(ARQ_dose_mamm_SG_sm_RBL_temp)
        CRQ_dose_mamm_SG_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SG_sm']
        CRQ_dose_mamm_SG_sm_RBL_out.append(CRQ_dose_mamm_SG_sm_RBL_temp)
        ARQ_dose_mamm_SG_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SG_md']
        ARQ_dose_mamm_SG_md_RBL_out.append(ARQ_dose_mamm_SG_md_RBL_temp)
        CRQ_dose_mamm_SG_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SG_md']
        CRQ_dose_mamm_SG_md_RBL_out.append(CRQ_dose_mamm_SG_md_RBL_temp)
        ARQ_dose_mamm_SG_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SG_lg']
        ARQ_dose_mamm_SG_lg_RBL_out.append(ARQ_dose_mamm_SG_lg_RBL_temp)
        CRQ_dose_mamm_SG_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SG_lg']
        CRQ_dose_mamm_SG_lg_RBL_out.append(CRQ_dose_mamm_SG_lg_RBL_temp)
        ARQ_dose_mamm_TG_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_TG_sm']
        ARQ_dose_mamm_TG_sm_RBL_out.append(ARQ_dose_mamm_TG_sm_RBL_temp)
        CRQ_dose_mamm_TG_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_TG_sm']
        CRQ_dose_mamm_TG_sm_RBL_out.append(CRQ_dose_mamm_TG_sm_RBL_temp)
        ARQ_dose_mamm_TG_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_TG_md']
        ARQ_dose_mamm_TG_md_RBL_out.append(ARQ_dose_mamm_TG_md_RBL_temp)
        CRQ_dose_mamm_TG_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_TG_md']
        CRQ_dose_mamm_TG_md_RBL_out.append(CRQ_dose_mamm_TG_md_RBL_temp)
        ARQ_dose_mamm_TG_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_TG_lg']
        ARQ_dose_mamm_TG_lg_RBL_out.append(ARQ_dose_mamm_TG_lg_RBL_temp)
        CRQ_dose_mamm_TG_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_TG_lg']
        CRQ_dose_mamm_TG_lg_RBL_out.append(CRQ_dose_mamm_TG_lg_RBL_temp)
        ARQ_dose_mamm_BP_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_BP_sm']
        ARQ_dose_mamm_BP_sm_RBL_out.append(ARQ_dose_mamm_BP_sm_RBL_temp)
        CRQ_dose_mamm_BP_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_BP_sm']
        CRQ_dose_mamm_BP_sm_RBL_out.append(CRQ_dose_mamm_BP_sm_RBL_temp)
        ARQ_dose_mamm_BP_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_BP_md']
        ARQ_dose_mamm_BP_md_RBL_out.append(ARQ_dose_mamm_BP_md_RBL_temp)
        CRQ_dose_mamm_BP_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_BP_md']
        CRQ_dose_mamm_BP_md_RBL_out.append(CRQ_dose_mamm_BP_md_RBL_temp)
        ARQ_dose_mamm_BP_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_BP_lg']
        ARQ_dose_mamm_BP_lg_RBL_out.append(ARQ_dose_mamm_BP_lg_RBL_temp)
        CRQ_dose_mamm_BP_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_BP_lg']
        CRQ_dose_mamm_BP_lg_RBL_out.append(CRQ_dose_mamm_BP_lg_RBL_temp)
        ARQ_dose_mamm_FP_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_FP_sm']
        ARQ_dose_mamm_FP_sm_RBL_out.append(ARQ_dose_mamm_FP_sm_RBL_temp)
        CRQ_dose_mamm_FP_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_FP_sm']
        CRQ_dose_mamm_FP_sm_RBL_out.append(CRQ_dose_mamm_FP_sm_RBL_temp)
        ARQ_dose_mamm_FP_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_FP_md']
        ARQ_dose_mamm_FP_md_RBL_out.append(ARQ_dose_mamm_FP_md_RBL_temp)
        CRQ_dose_mamm_FP_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_FP_md']
        CRQ_dose_mamm_FP_md_RBL_out.append(CRQ_dose_mamm_FP_md_RBL_temp)
        ARQ_dose_mamm_FP_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_FP_lg']
        ARQ_dose_mamm_FP_lg_RBL_out.append(ARQ_dose_mamm_FP_lg_RBL_temp)
        CRQ_dose_mamm_FP_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_FP_lg']
        CRQ_dose_mamm_FP_lg_RBL_out.append(CRQ_dose_mamm_FP_lg_RBL_temp)
        ARQ_dose_mamm_AR_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_AR_sm']
        ARQ_dose_mamm_AR_sm_RBL_out.append(ARQ_dose_mamm_AR_sm_RBL_temp)
        CRQ_dose_mamm_AR_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_AR_sm']
        CRQ_dose_mamm_AR_sm_RBL_out.append(CRQ_dose_mamm_AR_sm_RBL_temp)
        ARQ_dose_mamm_AR_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_AR_md']
        ARQ_dose_mamm_AR_md_RBL_out.append(ARQ_dose_mamm_AR_md_RBL_temp)
        CRQ_dose_mamm_AR_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_AR_md']
        CRQ_dose_mamm_AR_md_RBL_out.append(CRQ_dose_mamm_AR_md_RBL_temp)
        ARQ_dose_mamm_AR_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_AR_lg']
        ARQ_dose_mamm_AR_lg_RBL_out.append(ARQ_dose_mamm_AR_lg_RBL_temp)
        CRQ_dose_mamm_AR_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_AR_lg']
        CRQ_dose_mamm_AR_lg_RBL_out.append(CRQ_dose_mamm_AR_lg_RBL_temp)
        ARQ_dose_mamm_SE_sm_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SE_sm']
        ARQ_dose_mamm_SE_sm_RBL_out.append(ARQ_dose_mamm_SE_sm_RBL_temp)
        CRQ_dose_mamm_SE_sm_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SE_sm']
        CRQ_dose_mamm_SE_sm_RBL_out.append(CRQ_dose_mamm_SE_sm_RBL_temp)
        ARQ_dose_mamm_SE_md_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SE_md']
        ARQ_dose_mamm_SE_md_RBL_out.append(ARQ_dose_mamm_SE_md_RBL_temp)
        CRQ_dose_mamm_SE_md_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SE_md']
        CRQ_dose_mamm_SE_md_RBL_out.append(CRQ_dose_mamm_SE_md_RBL_temp)
        ARQ_dose_mamm_SE_lg_RBL_temp=table_all_out[5]['ARQ_dose_mamm_SE_lg']
        ARQ_dose_mamm_SE_lg_RBL_out.append(ARQ_dose_mamm_SE_lg_RBL_temp)
        CRQ_dose_mamm_SE_lg_RBL_temp=table_all_out[5]['CRQ_dose_mamm_SE_lg']
        CRQ_dose_mamm_SE_lg_RBL_out.append(CRQ_dose_mamm_SE_lg_RBL_temp)

###Table 11#######
        ARQ_diet_mamm_SG_RBL_temp=table_all_out[6]['ARQ_diet_mamm_SG']
        ARQ_diet_mamm_SG_RBL_out.append(ARQ_diet_mamm_SG_RBL_temp)
        CRQ_diet_mamm_SG_RBL_temp=table_all_out[6]['CRQ_diet_mamm_SG']
        CRQ_diet_mamm_SG_RBL_out.append(CRQ_diet_mamm_SG_RBL_temp)
        ARQ_diet_mamm_TG_RBL_temp=table_all_out[6]['ARQ_diet_mamm_TG']
        ARQ_diet_mamm_TG_RBL_out.append(ARQ_diet_mamm_TG_RBL_temp)
        CRQ_diet_mamm_TG_RBL_temp=table_all_out[6]['CRQ_diet_mamm_TG']
        CRQ_diet_mamm_TG_RBL_out.append(CRQ_diet_mamm_TG_RBL_temp)
        ARQ_diet_mamm_BP_RBL_temp=table_all_out[6]['ARQ_diet_mamm_BP']
        ARQ_diet_mamm_BP_RBL_out.append(ARQ_diet_mamm_BP_RBL_temp)
        CRQ_diet_mamm_BP_RBL_temp=table_all_out[6]['CRQ_diet_mamm_BP']
        CRQ_diet_mamm_BP_RBL_out.append(CRQ_diet_mamm_BP_RBL_temp)
        ARQ_diet_mamm_FP_RBL_temp=table_all_out[6]['ARQ_diet_mamm_FP']
        ARQ_diet_mamm_FP_RBL_out.append(ARQ_diet_mamm_FP_RBL_temp)
        CRQ_diet_mamm_FP_RBL_temp=table_all_out[6]['CRQ_diet_mamm_FP']
        CRQ_diet_mamm_FP_RBL_out.append(CRQ_diet_mamm_FP_RBL_temp)
        ARQ_diet_mamm_AR_RBL_temp=table_all_out[6]['ARQ_diet_mamm_AR']
        ARQ_diet_mamm_AR_RBL_out.append(ARQ_diet_mamm_AR_RBL_temp)
        CRQ_diet_mamm_AR_RBL_temp=table_all_out[6]['CRQ_diet_mamm_AR']
        CRQ_diet_mamm_AR_RBL_out.append(CRQ_diet_mamm_AR_RBL_temp)

    if Application_type_temp == 'Broadcast-Granular':
        LD50_bg_bird_sm_temp=table_all_out[7]['LD50_bg_bird_sm']
        LD50_bg_bird_sm_out.append(LD50_bg_bird_sm_temp)
        LD50_bg_mamm_sm_temp=table_all_out[7]['LD50_bg_mamm_sm']
        LD50_bg_mamm_sm_out.append(LD50_bg_mamm_sm_temp)
        LD50_bg_bird_md_temp=table_all_out[7]['LD50_bg_bird_md']
        LD50_bg_bird_md_out.append(LD50_bg_bird_md_temp)
        LD50_bg_mamm_md_temp=table_all_out[7]['LD50_bg_mamm_md']
        LD50_bg_mamm_md_out.append(LD50_bg_mamm_md_temp)
        LD50_bg_bird_lg_temp=table_all_out[7]['LD50_bg_bird_lg']
        LD50_bg_bird_lg_out.append(LD50_bg_bird_lg_temp)
        LD50_bg_mamm_lg_temp=table_all_out[7]['LD50_bg_mamm_lg']
        LD50_bg_mamm_lg_out.append(LD50_bg_mamm_lg_temp)

####Table 6##
        EEC_diet_SG_BG_temp=table_all_out[1]['EEC_diet_SG']
        EEC_diet_SG_BG_out.append(EEC_diet_SG_BG_temp)
        EEC_diet_TG_BG_temp=table_all_out[1]['EEC_diet_TG']
        EEC_diet_TG_BG_out.append(EEC_diet_TG_BG_temp)
        EEC_diet_BP_BG_temp=table_all_out[1]['EEC_diet_BP']
        EEC_diet_BP_BG_out.append(EEC_diet_BP_BG_temp)
        EEC_diet_FR_BG_temp=table_all_out[1]['EEC_diet_FR']
        EEC_diet_FR_BG_out.append(EEC_diet_FR_BG_temp)
        EEC_diet_AR_BG_temp=table_all_out[1]['EEC_diet_AR']
        EEC_diet_AR_BG_out.append(EEC_diet_AR_BG_temp)

####Table 7##
        EEC_dose_bird_SG_BG_sm_temp=table_all_out[2]['EEC_dose_bird_SG_sm']
        EEC_dose_bird_SG_BG_sm_out.append(EEC_dose_bird_SG_BG_sm_temp)
        EEC_dose_bird_SG_BG_md_temp=table_all_out[2]['EEC_dose_bird_SG_md']
        EEC_dose_bird_SG_BG_md_out.append(EEC_dose_bird_SG_BG_md_temp)
        EEC_dose_bird_SG_BG_lg_temp=table_all_out[2]['EEC_dose_bird_SG_lg']
        EEC_dose_bird_SG_BG_lg_out.append(EEC_dose_bird_SG_BG_lg_temp)
        EEC_dose_bird_TG_BG_sm_temp=table_all_out[2]['EEC_dose_bird_TG_sm']
        EEC_dose_bird_TG_BG_sm_out.append(EEC_dose_bird_TG_BG_sm_temp)
        EEC_dose_bird_TG_BG_md_temp=table_all_out[2]['EEC_dose_bird_TG_md']
        EEC_dose_bird_TG_BG_md_out.append(EEC_dose_bird_TG_BG_md_temp)
        EEC_dose_bird_TG_BG_lg_temp=table_all_out[2]['EEC_dose_bird_TG_lg']
        EEC_dose_bird_TG_BG_lg_out.append(EEC_dose_bird_TG_BG_lg_temp)
        EEC_dose_bird_BP_BG_sm_temp=table_all_out[2]['EEC_dose_bird_BP_sm']
        EEC_dose_bird_BP_BG_sm_out.append(EEC_dose_bird_BP_BG_sm_temp)
        EEC_dose_bird_BP_BG_md_temp=table_all_out[2]['EEC_dose_bird_BP_md']
        EEC_dose_bird_BP_BG_md_out.append(EEC_dose_bird_BP_BG_md_temp)
        EEC_dose_bird_BP_BG_lg_temp=table_all_out[2]['EEC_dose_bird_BP_lg']
        EEC_dose_bird_BP_BG_lg_out.append(EEC_dose_bird_BP_BG_lg_temp)
        EEC_dose_bird_FP_BG_sm_temp=table_all_out[2]['EEC_dose_bird_FP_sm']
        EEC_dose_bird_FP_BG_sm_out.append(EEC_dose_bird_FP_BG_sm_temp)
        EEC_dose_bird_FP_BG_md_temp=table_all_out[2]['EEC_dose_bird_FP_md']
        EEC_dose_bird_FP_BG_md_out.append(EEC_dose_bird_FP_BG_md_temp)
        EEC_dose_bird_FP_BG_lg_temp=table_all_out[2]['EEC_dose_bird_FP_lg']
        EEC_dose_bird_FP_BG_lg_out.append(EEC_dose_bird_FP_BG_lg_temp)
        EEC_dose_bird_AR_BG_sm_temp=table_all_out[2]['EEC_dose_bird_AR_sm']
        EEC_dose_bird_AR_BG_sm_out.append(EEC_dose_bird_AR_BG_sm_temp)
        EEC_dose_bird_AR_BG_md_temp=table_all_out[2]['EEC_dose_bird_AR_md']
        EEC_dose_bird_AR_BG_md_out.append(EEC_dose_bird_AR_BG_md_temp)
        EEC_dose_bird_AR_BG_lg_temp=table_all_out[2]['EEC_dose_bird_AR_lg']
        EEC_dose_bird_AR_BG_lg_out.append(EEC_dose_bird_AR_BG_lg_temp)
        EEC_dose_bird_SE_BG_sm_temp=table_all_out[2]['EEC_dose_bird_SE_sm']
        EEC_dose_bird_SE_BG_sm_out.append(EEC_dose_bird_SE_BG_sm_temp)
        EEC_dose_bird_SE_BG_md_temp=table_all_out[2]['EEC_dose_bird_SE_md']
        EEC_dose_bird_SE_BG_md_out.append(EEC_dose_bird_SE_BG_md_temp)
        EEC_dose_bird_SE_BG_lg_temp=table_all_out[2]['EEC_dose_bird_SE_lg']
        EEC_dose_bird_SE_BG_lg_out.append(EEC_dose_bird_SE_BG_lg_temp)

###Table 8#######
        ARQ_diet_bird_SG_A_BG_temp=table_all_out[3]['ARQ_diet_bird_SG_A']
        ARQ_diet_bird_SG_A_BG_out.append(ARQ_diet_bird_SG_A_BG_temp)
        ARQ_diet_bird_SG_C_BG_temp=table_all_out[3]['ARQ_diet_bird_SG_C']
        ARQ_diet_bird_SG_C_BG_out.append(ARQ_diet_bird_SG_C_BG_temp)
        ARQ_diet_bird_TG_A_BG_temp=table_all_out[3]['ARQ_diet_bird_TG_A']
        ARQ_diet_bird_TG_A_BG_out.append(ARQ_diet_bird_TG_A_BG_temp)
        ARQ_diet_bird_TG_C_BG_temp=table_all_out[3]['ARQ_diet_bird_TG_C']
        ARQ_diet_bird_TG_C_BG_out.append(ARQ_diet_bird_TG_C_BG_temp)
        ARQ_diet_bird_BP_A_BG_temp=table_all_out[3]['ARQ_diet_bird_BP_A']
        ARQ_diet_bird_BP_A_BG_out.append(ARQ_diet_bird_BP_A_BG_temp)
        ARQ_diet_bird_BP_C_BG_temp=table_all_out[3]['ARQ_diet_bird_BP_C']
        ARQ_diet_bird_BP_C_BG_out.append(ARQ_diet_bird_BP_C_BG_temp)
        ARQ_diet_bird_FP_A_BG_temp=table_all_out[3]['ARQ_diet_bird_FP_A']
        ARQ_diet_bird_FP_A_BG_out.append(ARQ_diet_bird_FP_A_BG_temp)
        ARQ_diet_bird_FP_C_BG_temp=table_all_out[3]['ARQ_diet_bird_FP_C']
        ARQ_diet_bird_FP_C_BG_out.append(ARQ_diet_bird_FP_C_BG_temp)
        ARQ_diet_bird_AR_A_BG_temp=table_all_out[3]['ARQ_diet_bird_AR_A']
        ARQ_diet_bird_AR_A_BG_out.append(ARQ_diet_bird_AR_A_BG_temp)
        ARQ_diet_bird_AR_C_BG_temp=table_all_out[3]['ARQ_diet_bird_AR_C']
        ARQ_diet_bird_AR_C_BG_out.append(ARQ_diet_bird_AR_C_BG_temp)

###Table 9#######
        EEC_dose_mamm_SG_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_SG_sm']
        EEC_dose_mamm_SG_sm_BG_out.append(EEC_dose_mamm_SG_sm_BG_temp)
        EEC_dose_mamm_SG_md_BG_temp=table_all_out[4]['EEC_dose_mamm_SG_md']
        EEC_dose_mamm_SG_md_BG_out.append(EEC_dose_mamm_SG_md_BG_temp)
        EEC_dose_mamm_SG_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_SG_lg']
        EEC_dose_mamm_SG_lg_BG_out.append(EEC_dose_mamm_SG_lg_BG_temp)
        EEC_dose_mamm_TG_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_TG_sm']
        EEC_dose_mamm_TG_sm_BG_out.append(EEC_dose_mamm_TG_sm_BG_temp)
        EEC_dose_mamm_TG_md_BG_temp=table_all_out[4]['EEC_dose_mamm_TG_md']
        EEC_dose_mamm_TG_md_BG_out.append(EEC_dose_mamm_TG_md_BG_temp)
        EEC_dose_mamm_TG_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_TG_lg']
        EEC_dose_mamm_TG_lg_BG_out.append(EEC_dose_mamm_TG_lg_BG_temp)
        EEC_dose_mamm_BP_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_BP_sm']
        EEC_dose_mamm_BP_sm_BG_out.append(EEC_dose_mamm_BP_sm_BG_temp)
        EEC_dose_mamm_BP_md_BG_temp=table_all_out[4]['EEC_dose_mamm_BP_md']
        EEC_dose_mamm_BP_md_BG_out.append(EEC_dose_mamm_BP_md_BG_temp)
        EEC_dose_mamm_BP_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_BP_lg']
        EEC_dose_mamm_BP_lg_BG_out.append(EEC_dose_mamm_BP_lg_BG_temp)
        EEC_dose_mamm_FP_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_FP_sm']
        EEC_dose_mamm_FP_sm_BG_out.append(EEC_dose_mamm_FP_sm_BG_temp)
        EEC_dose_mamm_FP_md_BG_temp=table_all_out[4]['EEC_dose_mamm_FP_md']
        EEC_dose_mamm_FP_md_BG_out.append(EEC_dose_mamm_FP_md_BG_temp)
        EEC_dose_mamm_FP_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_FP_lg']
        EEC_dose_mamm_FP_lg_BG_out.append(EEC_dose_mamm_FP_lg_BG_temp)
        EEC_dose_mamm_AR_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_AR_sm']
        EEC_dose_mamm_AR_sm_BG_out.append(EEC_dose_mamm_AR_sm_BG_temp)
        EEC_dose_mamm_AR_md_BG_temp=table_all_out[4]['EEC_dose_mamm_AR_md']
        EEC_dose_mamm_AR_md_BG_out.append(EEC_dose_mamm_AR_md_BG_temp)
        EEC_dose_mamm_AR_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_AR_lg']
        EEC_dose_mamm_AR_lg_BG_out.append(EEC_dose_mamm_AR_lg_BG_temp)
        EEC_dose_mamm_SE_sm_BG_temp=table_all_out[4]['EEC_dose_mamm_SE_sm']
        EEC_dose_mamm_SE_sm_BG_out.append(EEC_dose_mamm_SE_sm_BG_temp)
        EEC_dose_mamm_SE_md_BG_temp=table_all_out[4]['EEC_dose_mamm_SE_md']
        EEC_dose_mamm_SE_md_BG_out.append(EEC_dose_mamm_SE_md_BG_temp)
        EEC_dose_mamm_SE_lg_BG_temp=table_all_out[4]['EEC_dose_mamm_SE_lg']
        EEC_dose_mamm_SE_lg_BG_out.append(EEC_dose_mamm_SE_lg_BG_temp)

###Table 10#######
        ARQ_dose_mamm_SG_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_SG_sm']
        ARQ_dose_mamm_SG_sm_BG_out.append(ARQ_dose_mamm_SG_sm_BG_temp)
        CRQ_dose_mamm_SG_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_SG_sm']
        CRQ_dose_mamm_SG_sm_BG_out.append(CRQ_dose_mamm_SG_sm_BG_temp)
        ARQ_dose_mamm_SG_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_SG_md']
        ARQ_dose_mamm_SG_md_BG_out.append(ARQ_dose_mamm_SG_md_BG_temp)
        CRQ_dose_mamm_SG_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_SG_md']
        CRQ_dose_mamm_SG_md_BG_out.append(CRQ_dose_mamm_SG_md_BG_temp)
        ARQ_dose_mamm_SG_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_SG_lg']
        ARQ_dose_mamm_SG_lg_BG_out.append(ARQ_dose_mamm_SG_lg_BG_temp)
        CRQ_dose_mamm_SG_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_SG_lg']
        CRQ_dose_mamm_SG_lg_BG_out.append(CRQ_dose_mamm_SG_lg_BG_temp)
        ARQ_dose_mamm_TG_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_TG_sm']
        ARQ_dose_mamm_TG_sm_BG_out.append(ARQ_dose_mamm_TG_sm_BG_temp)
        CRQ_dose_mamm_TG_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_TG_sm']
        CRQ_dose_mamm_TG_sm_BG_out.append(CRQ_dose_mamm_TG_sm_BG_temp)
        ARQ_dose_mamm_TG_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_TG_md']
        ARQ_dose_mamm_TG_md_BG_out.append(ARQ_dose_mamm_TG_md_BG_temp)
        CRQ_dose_mamm_TG_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_TG_md']
        CRQ_dose_mamm_TG_md_BG_out.append(CRQ_dose_mamm_TG_md_BG_temp)
        ARQ_dose_mamm_TG_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_TG_lg']
        ARQ_dose_mamm_TG_lg_BG_out.append(ARQ_dose_mamm_TG_lg_BG_temp)
        CRQ_dose_mamm_TG_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_TG_lg']
        CRQ_dose_mamm_TG_lg_BG_out.append(CRQ_dose_mamm_TG_lg_BG_temp)
        ARQ_dose_mamm_BP_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_BP_sm']
        ARQ_dose_mamm_BP_sm_BG_out.append(ARQ_dose_mamm_BP_sm_BG_temp)
        CRQ_dose_mamm_BP_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_BP_sm']
        CRQ_dose_mamm_BP_sm_BG_out.append(CRQ_dose_mamm_BP_sm_BG_temp)
        ARQ_dose_mamm_BP_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_BP_md']
        ARQ_dose_mamm_BP_md_BG_out.append(ARQ_dose_mamm_BP_md_BG_temp)
        CRQ_dose_mamm_BP_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_BP_md']
        CRQ_dose_mamm_BP_md_BG_out.append(CRQ_dose_mamm_BP_md_BG_temp)
        ARQ_dose_mamm_BP_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_BP_lg']
        ARQ_dose_mamm_BP_lg_BG_out.append(ARQ_dose_mamm_BP_lg_BG_temp)
        CRQ_dose_mamm_BP_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_BP_lg']
        CRQ_dose_mamm_BP_lg_BG_out.append(CRQ_dose_mamm_BP_lg_BG_temp)
        ARQ_dose_mamm_FP_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_FP_sm']
        ARQ_dose_mamm_FP_sm_BG_out.append(ARQ_dose_mamm_FP_sm_BG_temp)
        CRQ_dose_mamm_FP_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_FP_sm']
        CRQ_dose_mamm_FP_sm_BG_out.append(CRQ_dose_mamm_FP_sm_BG_temp)
        ARQ_dose_mamm_FP_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_FP_md']
        ARQ_dose_mamm_FP_md_BG_out.append(ARQ_dose_mamm_FP_md_BG_temp)
        CRQ_dose_mamm_FP_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_FP_md']
        CRQ_dose_mamm_FP_md_BG_out.append(CRQ_dose_mamm_FP_md_BG_temp)
        ARQ_dose_mamm_FP_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_FP_lg']
        ARQ_dose_mamm_FP_lg_BG_out.append(ARQ_dose_mamm_FP_lg_BG_temp)
        CRQ_dose_mamm_FP_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_FP_lg']
        CRQ_dose_mamm_FP_lg_BG_out.append(CRQ_dose_mamm_FP_lg_BG_temp)
        ARQ_dose_mamm_AR_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_AR_sm']
        ARQ_dose_mamm_AR_sm_BG_out.append(ARQ_dose_mamm_AR_sm_BG_temp)
        CRQ_dose_mamm_AR_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_AR_sm']
        CRQ_dose_mamm_AR_sm_BG_out.append(CRQ_dose_mamm_AR_sm_BG_temp)
        ARQ_dose_mamm_AR_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_AR_md']
        ARQ_dose_mamm_AR_md_BG_out.append(ARQ_dose_mamm_AR_md_BG_temp)
        CRQ_dose_mamm_AR_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_AR_md']
        CRQ_dose_mamm_AR_md_BG_out.append(CRQ_dose_mamm_AR_md_BG_temp)
        ARQ_dose_mamm_AR_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_AR_lg']
        ARQ_dose_mamm_AR_lg_BG_out.append(ARQ_dose_mamm_AR_lg_BG_temp)
        CRQ_dose_mamm_AR_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_AR_lg']
        CRQ_dose_mamm_AR_lg_BG_out.append(CRQ_dose_mamm_AR_lg_BG_temp)
        ARQ_dose_mamm_SE_sm_BG_temp=table_all_out[5]['ARQ_dose_mamm_SE_sm']
        ARQ_dose_mamm_SE_sm_BG_out.append(ARQ_dose_mamm_SE_sm_BG_temp)
        CRQ_dose_mamm_SE_sm_BG_temp=table_all_out[5]['CRQ_dose_mamm_SE_sm']
        CRQ_dose_mamm_SE_sm_BG_out.append(CRQ_dose_mamm_SE_sm_BG_temp)
        ARQ_dose_mamm_SE_md_BG_temp=table_all_out[5]['ARQ_dose_mamm_SE_md']
        ARQ_dose_mamm_SE_md_BG_out.append(ARQ_dose_mamm_SE_md_BG_temp)
        CRQ_dose_mamm_SE_md_BG_temp=table_all_out[5]['CRQ_dose_mamm_SE_md']
        CRQ_dose_mamm_SE_md_BG_out.append(CRQ_dose_mamm_SE_md_BG_temp)
        ARQ_dose_mamm_SE_lg_BG_temp=table_all_out[5]['ARQ_dose_mamm_SE_lg']
        ARQ_dose_mamm_SE_lg_BG_out.append(ARQ_dose_mamm_SE_lg_BG_temp)
        CRQ_dose_mamm_SE_lg_BG_temp=table_all_out[5]['CRQ_dose_mamm_SE_lg']
        CRQ_dose_mamm_SE_lg_BG_out.append(CRQ_dose_mamm_SE_lg_BG_temp)

###Table 11#######
        ARQ_diet_mamm_SG_BG_temp=table_all_out[6]['ARQ_diet_mamm_SG']
        ARQ_diet_mamm_SG_BG_out.append(ARQ_diet_mamm_SG_BG_temp)
        CRQ_diet_mamm_SG_BG_temp=table_all_out[6]['CRQ_diet_mamm_SG']
        CRQ_diet_mamm_SG_BG_out.append(CRQ_diet_mamm_SG_BG_temp)
        ARQ_diet_mamm_TG_BG_temp=table_all_out[6]['ARQ_diet_mamm_TG']
        ARQ_diet_mamm_TG_BG_out.append(ARQ_diet_mamm_TG_BG_temp)
        CRQ_diet_mamm_TG_BG_temp=table_all_out[6]['CRQ_diet_mamm_TG']
        CRQ_diet_mamm_TG_BG_out.append(CRQ_diet_mamm_TG_BG_temp)
        ARQ_diet_mamm_BP_BG_temp=table_all_out[6]['ARQ_diet_mamm_BP']
        ARQ_diet_mamm_BP_BG_out.append(ARQ_diet_mamm_BP_BG_temp)
        CRQ_diet_mamm_BP_BG_temp=table_all_out[6]['CRQ_diet_mamm_BP']
        CRQ_diet_mamm_BP_BG_out.append(CRQ_diet_mamm_BP_BG_temp)
        ARQ_diet_mamm_FP_BG_temp=table_all_out[6]['ARQ_diet_mamm_FP']
        ARQ_diet_mamm_FP_BG_out.append(ARQ_diet_mamm_FP_BG_temp)
        CRQ_diet_mamm_FP_BG_temp=table_all_out[6]['CRQ_diet_mamm_FP']
        CRQ_diet_mamm_FP_BG_out.append(CRQ_diet_mamm_FP_BG_temp)
        ARQ_diet_mamm_AR_BG_temp=table_all_out[6]['ARQ_diet_mamm_AR']
        ARQ_diet_mamm_AR_BG_out.append(ARQ_diet_mamm_AR_BG_temp)
        CRQ_diet_mamm_AR_BG_temp=table_all_out[6]['CRQ_diet_mamm_AR']
        CRQ_diet_mamm_AR_BG_out.append(CRQ_diet_mamm_AR_BG_temp)

    if Application_type_temp == 'Broadcast-Liquid':
        LD50_bl_bird_sm_temp=table_all_out[7]['LD50_bl_bird_sm']
        LD50_bl_bird_sm_out.append(LD50_bl_bird_sm_temp)
        LD50_bl_mamm_sm_temp=table_all_out[7]['LD50_bl_mamm_sm']
        LD50_bl_mamm_sm_out.append(LD50_bl_mamm_sm_temp)
        LD50_bl_bird_md_temp=table_all_out[7]['LD50_bl_bird_md']
        LD50_bl_bird_md_out.append(LD50_bl_bird_md_temp)
        LD50_bl_mamm_md_temp=table_all_out[7]['LD50_bl_mamm_md']
        LD50_bl_mamm_md_out.append(LD50_bl_mamm_md_temp)
        LD50_bl_bird_lg_temp=table_all_out[7]['LD50_bl_bird_lg']
        LD50_bl_bird_lg_out.append(LD50_bl_bird_lg_temp)
        LD50_bl_mamm_lg_temp=table_all_out[7]['LD50_bl_mamm_lg']
        LD50_bl_mamm_lg_out.append(LD50_bl_mamm_lg_temp)

####Table 6##
        EEC_diet_SG_BL_temp=table_all_out[1]['EEC_diet_SG']
        EEC_diet_SG_BL_out.append(EEC_diet_SG_BL_temp)
        EEC_diet_TG_BL_temp=table_all_out[1]['EEC_diet_TG']
        EEC_diet_TG_BL_out.append(EEC_diet_TG_BL_temp)
        EEC_diet_BP_BL_temp=table_all_out[1]['EEC_diet_BP']
        EEC_diet_BP_BL_out.append(EEC_diet_BP_BL_temp)
        EEC_diet_FR_BL_temp=table_all_out[1]['EEC_diet_FR']
        EEC_diet_FR_BL_out.append(EEC_diet_FR_BL_temp)
        EEC_diet_AR_BL_temp=table_all_out[1]['EEC_diet_AR']
        EEC_diet_AR_BL_out.append(EEC_diet_AR_BL_temp)

####Table 7##
        EEC_dose_bird_SG_BL_sm_temp=table_all_out[2]['EEC_dose_bird_SG_sm']
        EEC_dose_bird_SG_BL_sm_out.append(EEC_dose_bird_SG_BL_sm_temp)
        EEC_dose_bird_SG_BL_md_temp=table_all_out[2]['EEC_dose_bird_SG_md']
        EEC_dose_bird_SG_BL_md_out.append(EEC_dose_bird_SG_BL_md_temp)
        EEC_dose_bird_SG_BL_lg_temp=table_all_out[2]['EEC_dose_bird_SG_lg']
        EEC_dose_bird_SG_BL_lg_out.append(EEC_dose_bird_SG_BL_lg_temp)
        EEC_dose_bird_TG_BL_sm_temp=table_all_out[2]['EEC_dose_bird_TG_sm']
        EEC_dose_bird_TG_BL_sm_out.append(EEC_dose_bird_TG_BL_sm_temp)
        EEC_dose_bird_TG_BL_md_temp=table_all_out[2]['EEC_dose_bird_TG_md']
        EEC_dose_bird_TG_BL_md_out.append(EEC_dose_bird_TG_BL_md_temp)
        EEC_dose_bird_TG_BL_lg_temp=table_all_out[2]['EEC_dose_bird_TG_lg']
        EEC_dose_bird_TG_BL_lg_out.append(EEC_dose_bird_TG_BL_lg_temp)
        EEC_dose_bird_BP_BL_sm_temp=table_all_out[2]['EEC_dose_bird_BP_sm']
        EEC_dose_bird_BP_BL_sm_out.append(EEC_dose_bird_BP_BL_sm_temp)
        EEC_dose_bird_BP_BL_md_temp=table_all_out[2]['EEC_dose_bird_BP_md']
        EEC_dose_bird_BP_BL_md_out.append(EEC_dose_bird_BP_BL_md_temp)
        EEC_dose_bird_BP_BL_lg_temp=table_all_out[2]['EEC_dose_bird_BP_lg']
        EEC_dose_bird_BP_BL_lg_out.append(EEC_dose_bird_BP_BL_lg_temp)
        EEC_dose_bird_FP_BL_sm_temp=table_all_out[2]['EEC_dose_bird_FP_sm']
        EEC_dose_bird_FP_BL_sm_out.append(EEC_dose_bird_FP_BL_sm_temp)
        EEC_dose_bird_FP_BL_md_temp=table_all_out[2]['EEC_dose_bird_FP_md']
        EEC_dose_bird_FP_BL_md_out.append(EEC_dose_bird_FP_BL_md_temp)
        EEC_dose_bird_FP_BL_lg_temp=table_all_out[2]['EEC_dose_bird_FP_lg']
        EEC_dose_bird_FP_BL_lg_out.append(EEC_dose_bird_FP_BL_lg_temp)
        EEC_dose_bird_AR_BL_sm_temp=table_all_out[2]['EEC_dose_bird_AR_sm']
        EEC_dose_bird_AR_BL_sm_out.append(EEC_dose_bird_AR_BL_sm_temp)
        EEC_dose_bird_AR_BL_md_temp=table_all_out[2]['EEC_dose_bird_AR_md']
        EEC_dose_bird_AR_BL_md_out.append(EEC_dose_bird_AR_BL_md_temp)
        EEC_dose_bird_AR_BL_lg_temp=table_all_out[2]['EEC_dose_bird_AR_lg']
        EEC_dose_bird_AR_BL_lg_out.append(EEC_dose_bird_AR_BL_lg_temp)
        EEC_dose_bird_SE_BL_sm_temp=table_all_out[2]['EEC_dose_bird_SE_sm']
        EEC_dose_bird_SE_BL_sm_out.append(EEC_dose_bird_SE_BL_sm_temp)
        EEC_dose_bird_SE_BL_md_temp=table_all_out[2]['EEC_dose_bird_SE_md']
        EEC_dose_bird_SE_BL_md_out.append(EEC_dose_bird_SE_BL_md_temp)
        EEC_dose_bird_SE_BL_lg_temp=table_all_out[2]['EEC_dose_bird_SE_lg']
        EEC_dose_bird_SE_BL_lg_out.append(EEC_dose_bird_SE_BL_lg_temp)

###Table 8#######
        ARQ_diet_bird_SG_A_BL_temp=table_all_out[3]['ARQ_diet_bird_SG_A']
        ARQ_diet_bird_SG_A_BL_out.append(ARQ_diet_bird_SG_A_BL_temp)
        ARQ_diet_bird_SG_C_BL_temp=table_all_out[3]['ARQ_diet_bird_SG_C']
        ARQ_diet_bird_SG_C_BL_out.append(ARQ_diet_bird_SG_C_BL_temp)
        ARQ_diet_bird_TG_A_BL_temp=table_all_out[3]['ARQ_diet_bird_TG_A']
        ARQ_diet_bird_TG_A_BL_out.append(ARQ_diet_bird_TG_A_BL_temp)
        ARQ_diet_bird_TG_C_BL_temp=table_all_out[3]['ARQ_diet_bird_TG_C']
        ARQ_diet_bird_TG_C_BL_out.append(ARQ_diet_bird_TG_C_BL_temp)
        ARQ_diet_bird_BP_A_BL_temp=table_all_out[3]['ARQ_diet_bird_BP_A']
        ARQ_diet_bird_BP_A_BL_out.append(ARQ_diet_bird_BP_A_BL_temp)
        ARQ_diet_bird_BP_C_BL_temp=table_all_out[3]['ARQ_diet_bird_BP_C']
        ARQ_diet_bird_BP_C_BL_out.append(ARQ_diet_bird_BP_C_BL_temp)
        ARQ_diet_bird_FP_A_BL_temp=table_all_out[3]['ARQ_diet_bird_FP_A']
        ARQ_diet_bird_FP_A_BL_out.append(ARQ_diet_bird_FP_A_BL_temp)
        ARQ_diet_bird_FP_C_BL_temp=table_all_out[3]['ARQ_diet_bird_FP_C']
        ARQ_diet_bird_FP_C_BL_out.append(ARQ_diet_bird_FP_C_BL_temp)
        ARQ_diet_bird_AR_A_BL_temp=table_all_out[3]['ARQ_diet_bird_AR_A']
        ARQ_diet_bird_AR_A_BL_out.append(ARQ_diet_bird_AR_A_BL_temp)
        ARQ_diet_bird_AR_C_BL_temp=table_all_out[3]['ARQ_diet_bird_AR_C']
        ARQ_diet_bird_AR_C_BL_out.append(ARQ_diet_bird_AR_C_BL_temp)

###Table 9#######
        EEC_dose_mamm_SG_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_SG_sm']
        EEC_dose_mamm_SG_sm_BL_out.append(EEC_dose_mamm_SG_sm_BL_temp)
        EEC_dose_mamm_SG_md_BL_temp=table_all_out[4]['EEC_dose_mamm_SG_md']
        EEC_dose_mamm_SG_md_BL_out.append(EEC_dose_mamm_SG_md_BL_temp)
        EEC_dose_mamm_SG_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_SG_lg']
        EEC_dose_mamm_SG_lg_BL_out.append(EEC_dose_mamm_SG_lg_BL_temp)
        EEC_dose_mamm_TG_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_TG_sm']
        EEC_dose_mamm_TG_sm_BL_out.append(EEC_dose_mamm_TG_sm_BL_temp)
        EEC_dose_mamm_TG_md_BL_temp=table_all_out[4]['EEC_dose_mamm_TG_md']
        EEC_dose_mamm_TG_md_BL_out.append(EEC_dose_mamm_TG_md_BL_temp)
        EEC_dose_mamm_TG_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_TG_lg']
        EEC_dose_mamm_TG_lg_BL_out.append(EEC_dose_mamm_TG_lg_BL_temp)
        EEC_dose_mamm_BP_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_BP_sm']
        EEC_dose_mamm_BP_sm_BL_out.append(EEC_dose_mamm_BP_sm_BL_temp)
        EEC_dose_mamm_BP_md_BL_temp=table_all_out[4]['EEC_dose_mamm_BP_md']
        EEC_dose_mamm_BP_md_BL_out.append(EEC_dose_mamm_BP_md_BL_temp)
        EEC_dose_mamm_BP_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_BP_lg']
        EEC_dose_mamm_BP_lg_BL_out.append(EEC_dose_mamm_BP_lg_BL_temp)
        EEC_dose_mamm_FP_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_FP_sm']
        EEC_dose_mamm_FP_sm_BL_out.append(EEC_dose_mamm_FP_sm_BL_temp)
        EEC_dose_mamm_FP_md_BL_temp=table_all_out[4]['EEC_dose_mamm_FP_md']
        EEC_dose_mamm_FP_md_BL_out.append(EEC_dose_mamm_FP_md_BL_temp)
        EEC_dose_mamm_FP_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_FP_lg']
        EEC_dose_mamm_FP_lg_BL_out.append(EEC_dose_mamm_FP_lg_BL_temp)
        EEC_dose_mamm_AR_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_AR_sm']
        EEC_dose_mamm_AR_sm_BL_out.append(EEC_dose_mamm_AR_sm_BL_temp)
        EEC_dose_mamm_AR_md_BL_temp=table_all_out[4]['EEC_dose_mamm_AR_md']
        EEC_dose_mamm_AR_md_BL_out.append(EEC_dose_mamm_AR_md_BL_temp)
        EEC_dose_mamm_AR_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_AR_lg']
        EEC_dose_mamm_AR_lg_BL_out.append(EEC_dose_mamm_AR_lg_BL_temp)
        EEC_dose_mamm_SE_sm_BL_temp=table_all_out[4]['EEC_dose_mamm_SE_sm']
        EEC_dose_mamm_SE_sm_BL_out.append(EEC_dose_mamm_SE_sm_BL_temp)
        EEC_dose_mamm_SE_md_BL_temp=table_all_out[4]['EEC_dose_mamm_SE_md']
        EEC_dose_mamm_SE_md_BL_out.append(EEC_dose_mamm_SE_md_BL_temp)
        EEC_dose_mamm_SE_lg_BL_temp=table_all_out[4]['EEC_dose_mamm_SE_lg']
        EEC_dose_mamm_SE_lg_BL_out.append(EEC_dose_mamm_SE_lg_BL_temp)

###Table 10#######
        ARQ_dose_mamm_SG_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_SG_sm']
        ARQ_dose_mamm_SG_sm_BL_out.append(ARQ_dose_mamm_SG_sm_BL_temp)
        CRQ_dose_mamm_SG_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_SG_sm']
        CRQ_dose_mamm_SG_sm_BL_out.append(CRQ_dose_mamm_SG_sm_BL_temp)
        ARQ_dose_mamm_SG_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_SG_md']
        ARQ_dose_mamm_SG_md_BL_out.append(ARQ_dose_mamm_SG_md_BL_temp)
        CRQ_dose_mamm_SG_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_SG_md']
        CRQ_dose_mamm_SG_md_BL_out.append(CRQ_dose_mamm_SG_md_BL_temp)
        ARQ_dose_mamm_SG_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_SG_lg']
        ARQ_dose_mamm_SG_lg_BL_out.append(ARQ_dose_mamm_SG_lg_BL_temp)
        CRQ_dose_mamm_SG_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_SG_lg']
        CRQ_dose_mamm_SG_lg_BL_out.append(CRQ_dose_mamm_SG_lg_BL_temp)
        ARQ_dose_mamm_TG_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_TG_sm']
        ARQ_dose_mamm_TG_sm_BL_out.append(ARQ_dose_mamm_TG_sm_BL_temp)
        CRQ_dose_mamm_TG_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_TG_sm']
        CRQ_dose_mamm_TG_sm_BL_out.append(CRQ_dose_mamm_TG_sm_BL_temp)
        ARQ_dose_mamm_TG_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_TG_md']
        ARQ_dose_mamm_TG_md_BL_out.append(ARQ_dose_mamm_TG_md_BL_temp)
        CRQ_dose_mamm_TG_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_TG_md']
        CRQ_dose_mamm_TG_md_BL_out.append(CRQ_dose_mamm_TG_md_BL_temp)
        ARQ_dose_mamm_TG_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_TG_lg']
        ARQ_dose_mamm_TG_lg_BL_out.append(ARQ_dose_mamm_TG_lg_BL_temp)
        CRQ_dose_mamm_TG_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_TG_lg']
        CRQ_dose_mamm_TG_lg_BL_out.append(CRQ_dose_mamm_TG_lg_BL_temp)
        ARQ_dose_mamm_BP_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_BP_sm']
        ARQ_dose_mamm_BP_sm_BL_out.append(ARQ_dose_mamm_BP_sm_BL_temp)
        CRQ_dose_mamm_BP_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_BP_sm']
        CRQ_dose_mamm_BP_sm_BL_out.append(CRQ_dose_mamm_BP_sm_BL_temp)
        ARQ_dose_mamm_BP_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_BP_md']
        ARQ_dose_mamm_BP_md_BL_out.append(ARQ_dose_mamm_BP_md_BL_temp)
        CRQ_dose_mamm_BP_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_BP_md']
        CRQ_dose_mamm_BP_md_BL_out.append(CRQ_dose_mamm_BP_md_BL_temp)
        ARQ_dose_mamm_BP_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_BP_lg']
        ARQ_dose_mamm_BP_lg_BL_out.append(ARQ_dose_mamm_BP_lg_BL_temp)
        CRQ_dose_mamm_BP_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_BP_lg']
        CRQ_dose_mamm_BP_lg_BL_out.append(CRQ_dose_mamm_BP_lg_BL_temp)
        ARQ_dose_mamm_FP_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_FP_sm']
        ARQ_dose_mamm_FP_sm_BL_out.append(ARQ_dose_mamm_FP_sm_BL_temp)
        CRQ_dose_mamm_FP_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_FP_sm']
        CRQ_dose_mamm_FP_sm_BL_out.append(CRQ_dose_mamm_FP_sm_BL_temp)
        ARQ_dose_mamm_FP_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_FP_md']
        ARQ_dose_mamm_FP_md_BL_out.append(ARQ_dose_mamm_FP_md_BL_temp)
        CRQ_dose_mamm_FP_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_FP_md']
        CRQ_dose_mamm_FP_md_BL_out.append(CRQ_dose_mamm_FP_md_BL_temp)
        ARQ_dose_mamm_FP_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_FP_lg']
        ARQ_dose_mamm_FP_lg_BL_out.append(ARQ_dose_mamm_FP_lg_BL_temp)
        CRQ_dose_mamm_FP_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_FP_lg']
        CRQ_dose_mamm_FP_lg_BL_out.append(CRQ_dose_mamm_FP_lg_BL_temp)
        ARQ_dose_mamm_AR_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_AR_sm']
        ARQ_dose_mamm_AR_sm_BL_out.append(ARQ_dose_mamm_AR_sm_BL_temp)
        CRQ_dose_mamm_AR_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_AR_sm']
        CRQ_dose_mamm_AR_sm_BL_out.append(CRQ_dose_mamm_AR_sm_BL_temp)
        ARQ_dose_mamm_AR_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_AR_md']
        ARQ_dose_mamm_AR_md_BL_out.append(ARQ_dose_mamm_AR_md_BL_temp)
        CRQ_dose_mamm_AR_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_AR_md']
        CRQ_dose_mamm_AR_md_BL_out.append(CRQ_dose_mamm_AR_md_BL_temp)
        ARQ_dose_mamm_AR_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_AR_lg']
        ARQ_dose_mamm_AR_lg_BL_out.append(ARQ_dose_mamm_AR_lg_BL_temp)
        CRQ_dose_mamm_AR_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_AR_lg']
        CRQ_dose_mamm_AR_lg_BL_out.append(CRQ_dose_mamm_AR_lg_BL_temp)
        ARQ_dose_mamm_SE_sm_BL_temp=table_all_out[5]['ARQ_dose_mamm_SE_sm']
        ARQ_dose_mamm_SE_sm_BL_out.append(ARQ_dose_mamm_SE_sm_BL_temp)
        CRQ_dose_mamm_SE_sm_BL_temp=table_all_out[5]['CRQ_dose_mamm_SE_sm']
        CRQ_dose_mamm_SE_sm_BL_out.append(CRQ_dose_mamm_SE_sm_BL_temp)
        ARQ_dose_mamm_SE_md_BL_temp=table_all_out[5]['ARQ_dose_mamm_SE_md']
        ARQ_dose_mamm_SE_md_BL_out.append(ARQ_dose_mamm_SE_md_BL_temp)
        CRQ_dose_mamm_SE_md_BL_temp=table_all_out[5]['CRQ_dose_mamm_SE_md']
        CRQ_dose_mamm_SE_md_BL_out.append(CRQ_dose_mamm_SE_md_BL_temp)
        ARQ_dose_mamm_SE_lg_BL_temp=table_all_out[5]['ARQ_dose_mamm_SE_lg']
        ARQ_dose_mamm_SE_lg_BL_out.append(ARQ_dose_mamm_SE_lg_BL_temp)
        CRQ_dose_mamm_SE_lg_BL_temp=table_all_out[5]['CRQ_dose_mamm_SE_lg']
        CRQ_dose_mamm_SE_lg_BL_out.append(CRQ_dose_mamm_SE_lg_BL_temp)

###Table 11#######
        ARQ_diet_mamm_SG_BL_temp=table_all_out[6]['ARQ_diet_mamm_SG']
        ARQ_diet_mamm_SG_BL_out.append(ARQ_diet_mamm_SG_BL_temp)
        CRQ_diet_mamm_SG_BL_temp=table_all_out[6]['CRQ_diet_mamm_SG']
        CRQ_diet_mamm_SG_BL_out.append(CRQ_diet_mamm_SG_BL_temp)
        ARQ_diet_mamm_TG_BL_temp=table_all_out[6]['ARQ_diet_mamm_TG']
        ARQ_diet_mamm_TG_BL_out.append(ARQ_diet_mamm_TG_BL_temp)
        CRQ_diet_mamm_TG_BL_temp=table_all_out[6]['CRQ_diet_mamm_TG']
        CRQ_diet_mamm_TG_BL_out.append(CRQ_diet_mamm_TG_BL_temp)
        ARQ_diet_mamm_BP_BL_temp=table_all_out[6]['ARQ_diet_mamm_BP']
        ARQ_diet_mamm_BP_BL_out.append(ARQ_diet_mamm_BP_BL_temp)
        CRQ_diet_mamm_BP_BL_temp=table_all_out[6]['CRQ_diet_mamm_BP']
        CRQ_diet_mamm_BP_BL_out.append(CRQ_diet_mamm_BP_BL_temp)
        ARQ_diet_mamm_FP_BL_temp=table_all_out[6]['ARQ_diet_mamm_FP']
        ARQ_diet_mamm_FP_BL_out.append(ARQ_diet_mamm_FP_BL_temp)
        CRQ_diet_mamm_FP_BL_temp=table_all_out[6]['CRQ_diet_mamm_FP']
        CRQ_diet_mamm_FP_BL_out.append(CRQ_diet_mamm_FP_BL_temp)
        ARQ_diet_mamm_AR_BL_temp=table_all_out[6]['ARQ_diet_mamm_AR']
        ARQ_diet_mamm_AR_BL_out.append(ARQ_diet_mamm_AR_BL_temp)
        CRQ_diet_mamm_AR_BL_temp=table_all_out[6]['CRQ_diet_mamm_AR']
        CRQ_diet_mamm_AR_BL_out.append(CRQ_diet_mamm_AR_BL_temp)

    return html_table_temp  

######Output###########

def loop_html(thefile):
    reader = csv.reader(thefile.file.read().splitlines())
    header = reader.next()
    exclud_list = ['', " ", "  ", "   ", "    ", "     ", "      ", "       ", "        ", "         ", "          "]
    i=1

    iter_html=""
    for row in reader:
        if row[3] in exclud_list:
            break
        iter_html = iter_html +html_table(row,i)
        # print row
        i=i+1


    sum_1 = trex2_tables.table_sum_1(i, a_i, r_s, b_w, p_i, den, h_l, n_a, rate_out)
    sum_2 = trex2_tables.table_sum_2(ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, tw_bird, x)
    sum_3 = trex2_tables.table_sum_3(ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm)

    html_sum = sum_1+sum_2+sum_3

    Application_type_ST=Application_type.count('Seed Treatment')
    Application_type_RBG=Application_type.count('Row/Band/In-furrow-Granular')
    Application_type_RBL=Application_type.count('Row/Band/In-furrow-Liquid')
    Application_type_BG=Application_type.count('Broadcast-Granular')
    Application_type_BL=Application_type.count('Broadcast-Liquid')

    if 'Seed Treatment' in Application_type:
        sum_5 = trex2_tables.table_sum_5(Application_type_ST, sa_bird_1_s_out, sa_bird_2_s_out, sc_bird_s_out, sa_mamm_1_s_out, sa_mamm_2_s_out, sc_mamm_s_out, sa_bird_1_m_out, sa_bird_2_m_out, sc_bird_m_out, sa_mamm_1_m_out, sa_mamm_2_m_out, sc_mamm_m_out, sa_bird_1_l_out, sa_bird_2_l_out, sc_bird_l_out, sa_mamm_1_l_out, sa_mamm_2_l_out, sc_mamm_l_out)
        html_sum = html_sum+ sum_5

    if 'Row/Band/In-furrow-Granular' in Application_type:
        sum_6_RBG = trex2_tables.table_sum_6(Application_type_RBG, 'Row/Band/In-furrow-Granular', EEC_diet_SG_RBG_out, EEC_diet_TG_RBG_out, EEC_diet_BP_RBG_out, EEC_diet_FR_RBG_out, EEC_diet_AR_RBG_out)
        sum_7_RBG = trex2_tables.table_sum_7(EEC_dose_bird_SG_RBG_sm_out, EEC_dose_bird_SG_RBG_md_out, EEC_dose_bird_SG_RBG_lg_out, EEC_dose_bird_TG_RBG_sm_out, EEC_dose_bird_TG_RBG_md_out, EEC_dose_bird_TG_RBG_lg_out, EEC_dose_bird_BP_RBG_sm_out, EEC_dose_bird_BP_RBG_md_out, EEC_dose_bird_BP_RBG_lg_out, EEC_dose_bird_FP_RBG_sm_out, EEC_dose_bird_FP_RBG_md_out, EEC_dose_bird_FP_RBG_lg_out, EEC_dose_bird_AR_RBG_sm_out, EEC_dose_bird_AR_RBG_md_out, EEC_dose_bird_AR_RBG_lg_out, EEC_dose_bird_SE_RBG_sm_out, EEC_dose_bird_SE_RBG_md_out, EEC_dose_bird_SE_RBG_lg_out)
        sum_8_RBG = trex2_tables.table_sum_8(ARQ_diet_bird_SG_A_RBG_out, ARQ_diet_bird_SG_C_RBG_out, ARQ_diet_bird_TG_A_RBG_out, ARQ_diet_bird_TG_C_RBG_out, ARQ_diet_bird_BP_A_RBG_out, ARQ_diet_bird_BP_C_RBG_out, ARQ_diet_bird_FP_A_RBG_out, ARQ_diet_bird_FP_C_RBG_out, ARQ_diet_bird_AR_A_RBG_out, ARQ_diet_bird_AR_C_RBG_out)
        sum_9_RBG = trex2_tables.table_sum_9(EEC_dose_mamm_SG_sm_RBG_out, EEC_dose_mamm_SG_md_RBG_out, EEC_dose_mamm_SG_lg_RBG_out, EEC_dose_mamm_TG_sm_RBG_out, EEC_dose_mamm_TG_md_RBG_out, EEC_dose_mamm_TG_lg_RBG_out, EEC_dose_mamm_BP_sm_RBG_out, EEC_dose_mamm_BP_md_RBG_out, EEC_dose_mamm_BP_lg_RBG_out, EEC_dose_mamm_FP_sm_RBG_out, EEC_dose_mamm_FP_md_RBG_out, EEC_dose_mamm_FP_lg_RBG_out, EEC_dose_mamm_AR_sm_RBG_out, EEC_dose_mamm_AR_md_RBG_out, EEC_dose_mamm_AR_lg_RBG_out, EEC_dose_mamm_SE_sm_RBG_out, EEC_dose_mamm_SE_md_RBG_out, EEC_dose_mamm_SE_lg_RBG_out)
        sum_10_RBG = trex2_tables.table_sum_10(ARQ_dose_mamm_SG_sm_RBG_out, CRQ_dose_mamm_SG_sm_RBG_out, ARQ_dose_mamm_SG_md_RBG_out, CRQ_dose_mamm_SG_md_RBG_out, ARQ_dose_mamm_SG_lg_RBG_out, CRQ_dose_mamm_SG_lg_RBG_out, ARQ_dose_mamm_TG_sm_RBG_out, CRQ_dose_mamm_TG_sm_RBG_out, ARQ_dose_mamm_TG_md_RBG_out, CRQ_dose_mamm_TG_md_RBG_out, ARQ_dose_mamm_TG_lg_RBG_out, CRQ_dose_mamm_TG_lg_RBG_out, ARQ_dose_mamm_BP_sm_RBG_out, CRQ_dose_mamm_BP_sm_RBG_out, ARQ_dose_mamm_BP_md_RBG_out, CRQ_dose_mamm_BP_md_RBG_out, ARQ_dose_mamm_BP_lg_RBG_out, CRQ_dose_mamm_BP_lg_RBG_out, ARQ_dose_mamm_FP_sm_RBG_out, CRQ_dose_mamm_FP_sm_RBG_out, ARQ_dose_mamm_FP_md_RBG_out, CRQ_dose_mamm_FP_md_RBG_out, ARQ_dose_mamm_FP_lg_RBG_out, CRQ_dose_mamm_FP_lg_RBG_out, ARQ_dose_mamm_AR_sm_RBG_out, CRQ_dose_mamm_AR_sm_RBG_out, ARQ_dose_mamm_AR_md_RBG_out, CRQ_dose_mamm_AR_md_RBG_out, ARQ_dose_mamm_AR_lg_RBG_out, CRQ_dose_mamm_AR_lg_RBG_out, ARQ_dose_mamm_SE_sm_RBG_out, CRQ_dose_mamm_SE_sm_RBG_out, ARQ_dose_mamm_SE_md_RBG_out, CRQ_dose_mamm_SE_md_RBG_out, ARQ_dose_mamm_SE_lg_RBG_out, CRQ_dose_mamm_SE_lg_RBG_out)
        sum_11_RBG = trex2_tables.table_sum_11(ARQ_diet_mamm_SG_RBG_out, CRQ_diet_mamm_SG_RBG_out, ARQ_diet_mamm_TG_RBG_out, CRQ_diet_mamm_TG_RBG_out, ARQ_diet_mamm_BP_RBG_out, CRQ_diet_mamm_BP_RBG_out, ARQ_diet_mamm_FP_RBG_out, CRQ_diet_mamm_FP_RBG_out, ARQ_diet_mamm_AR_RBG_out, CRQ_diet_mamm_AR_RBG_out)
        sum_12 = trex2_tables.table_sum_12(LD50_rg_bird_sm_out, LD50_rg_mamm_sm_out, LD50_rg_bird_md_out, LD50_rg_mamm_md_out, LD50_rg_bird_lg_out, LD50_rg_mamm_lg_out)
        html_sum = html_sum + sum_6_RBG + sum_7_RBG + sum_8_RBG + sum_9_RBG + sum_10_RBG + sum_11_RBG + sum_12

    if 'Row/Band/In-furrow-Liquid' in Application_type:
        sum_6_RBL = trex2_tables.table_sum_6(Application_type_RBL, 'Row/Band/In-furrow-Liquid', EEC_diet_SG_RBL_out, EEC_diet_TG_RBL_out, EEC_diet_BP_RBL_out, EEC_diet_FR_RBL_out, EEC_diet_AR_RBL_out)
        sum_7_RBL = trex2_tables.table_sum_7(EEC_dose_bird_SG_RBL_sm_out, EEC_dose_bird_SG_RBL_md_out, EEC_dose_bird_SG_RBL_lg_out, EEC_dose_bird_TG_RBL_sm_out, EEC_dose_bird_TG_RBL_md_out, EEC_dose_bird_TG_RBL_lg_out, EEC_dose_bird_BP_RBL_sm_out, EEC_dose_bird_BP_RBL_md_out, EEC_dose_bird_BP_RBL_lg_out, EEC_dose_bird_FP_RBL_sm_out, EEC_dose_bird_FP_RBL_md_out, EEC_dose_bird_FP_RBL_lg_out, EEC_dose_bird_AR_RBL_sm_out, EEC_dose_bird_AR_RBL_md_out, EEC_dose_bird_AR_RBL_lg_out, EEC_dose_bird_SE_RBL_sm_out, EEC_dose_bird_SE_RBL_md_out, EEC_dose_bird_SE_RBL_lg_out)
        sum_8_RBL = trex2_tables.table_sum_8(ARQ_diet_bird_SG_A_RBL_out, ARQ_diet_bird_SG_C_RBL_out, ARQ_diet_bird_TG_A_RBL_out, ARQ_diet_bird_TG_C_RBL_out, ARQ_diet_bird_BP_A_RBL_out, ARQ_diet_bird_BP_C_RBL_out, ARQ_diet_bird_FP_A_RBL_out, ARQ_diet_bird_FP_C_RBL_out, ARQ_diet_bird_AR_A_RBL_out, ARQ_diet_bird_AR_C_RBL_out)
        sum_9_RBL = trex2_tables.table_sum_9(EEC_dose_mamm_SG_sm_RBL_out, EEC_dose_mamm_SG_md_RBL_out, EEC_dose_mamm_SG_lg_RBL_out, EEC_dose_mamm_TG_sm_RBL_out, EEC_dose_mamm_TG_md_RBL_out, EEC_dose_mamm_TG_lg_RBL_out, EEC_dose_mamm_BP_sm_RBL_out, EEC_dose_mamm_BP_md_RBL_out, EEC_dose_mamm_BP_lg_RBL_out, EEC_dose_mamm_FP_sm_RBL_out, EEC_dose_mamm_FP_md_RBL_out, EEC_dose_mamm_FP_lg_RBL_out, EEC_dose_mamm_AR_sm_RBL_out, EEC_dose_mamm_AR_md_RBL_out, EEC_dose_mamm_AR_lg_RBL_out, EEC_dose_mamm_SE_sm_RBL_out, EEC_dose_mamm_SE_md_RBL_out, EEC_dose_mamm_SE_lg_RBL_out)
        sum_10_RBL = trex2_tables.table_sum_10(ARQ_dose_mamm_SG_sm_RBL_out, CRQ_dose_mamm_SG_sm_RBL_out, ARQ_dose_mamm_SG_md_RBL_out, CRQ_dose_mamm_SG_md_RBL_out, ARQ_dose_mamm_SG_lg_RBL_out, CRQ_dose_mamm_SG_lg_RBL_out, ARQ_dose_mamm_TG_sm_RBL_out, CRQ_dose_mamm_TG_sm_RBL_out, ARQ_dose_mamm_TG_md_RBL_out, CRQ_dose_mamm_TG_md_RBL_out, ARQ_dose_mamm_TG_lg_RBL_out, CRQ_dose_mamm_TG_lg_RBL_out, ARQ_dose_mamm_BP_sm_RBL_out, CRQ_dose_mamm_BP_sm_RBL_out, ARQ_dose_mamm_BP_md_RBL_out, CRQ_dose_mamm_BP_md_RBL_out, ARQ_dose_mamm_BP_lg_RBL_out, CRQ_dose_mamm_BP_lg_RBL_out, ARQ_dose_mamm_FP_sm_RBL_out, CRQ_dose_mamm_FP_sm_RBL_out, ARQ_dose_mamm_FP_md_RBL_out, CRQ_dose_mamm_FP_md_RBL_out, ARQ_dose_mamm_FP_lg_RBL_out, CRQ_dose_mamm_FP_lg_RBL_out, ARQ_dose_mamm_AR_sm_RBL_out, CRQ_dose_mamm_AR_sm_RBL_out, ARQ_dose_mamm_AR_md_RBL_out, CRQ_dose_mamm_AR_md_RBL_out, ARQ_dose_mamm_AR_lg_RBL_out, CRQ_dose_mamm_AR_lg_RBL_out, ARQ_dose_mamm_SE_sm_RBL_out, CRQ_dose_mamm_SE_sm_RBL_out, ARQ_dose_mamm_SE_md_RBL_out, CRQ_dose_mamm_SE_md_RBL_out, ARQ_dose_mamm_SE_lg_RBL_out, CRQ_dose_mamm_SE_lg_RBL_out)
        sum_11_RBL = trex2_tables.table_sum_11(ARQ_diet_mamm_SG_RBL_out, CRQ_diet_mamm_SG_RBL_out, ARQ_diet_mamm_TG_RBL_out, CRQ_diet_mamm_TG_RBL_out, ARQ_diet_mamm_BP_RBL_out, CRQ_diet_mamm_BP_RBL_out, ARQ_diet_mamm_FP_RBL_out, CRQ_diet_mamm_FP_RBL_out, ARQ_diet_mamm_AR_RBL_out, CRQ_diet_mamm_AR_RBL_out)
        sum_13 = trex2_tables.table_sum_13(LD50_rl_bird_sm_out, LD50_rl_mamm_sm_out, LD50_rl_bird_md_out, LD50_rl_mamm_md_out, LD50_rl_bird_lg_out, LD50_rl_mamm_lg_out)
        html_sum = html_sum + sum_6_RBL + sum_7_RBL + sum_8_RBL + sum_9_RBL + sum_10_RBL + sum_11_RBL + sum_13

    if 'Broadcast-Granular' in Application_type:
        sum_6_BG = trex2_tables.table_sum_6(Application_type_BG, 'Broadcast-Granular', EEC_diet_SG_BG_out, EEC_diet_TG_BG_out, EEC_diet_BP_BG_out, EEC_diet_FR_BG_out, EEC_diet_AR_BG_out)
        sum_7_BG = trex2_tables.table_sum_7(EEC_dose_bird_SG_BG_sm_out, EEC_dose_bird_SG_BG_md_out, EEC_dose_bird_SG_BG_lg_out, EEC_dose_bird_TG_BG_sm_out, EEC_dose_bird_TG_BG_md_out, EEC_dose_bird_TG_BG_lg_out, EEC_dose_bird_BP_BG_sm_out, EEC_dose_bird_BP_BG_md_out, EEC_dose_bird_BP_BG_lg_out, EEC_dose_bird_FP_BG_sm_out, EEC_dose_bird_FP_BG_md_out, EEC_dose_bird_FP_BG_lg_out, EEC_dose_bird_AR_BG_sm_out, EEC_dose_bird_AR_BG_md_out, EEC_dose_bird_AR_BG_lg_out, EEC_dose_bird_SE_BG_sm_out, EEC_dose_bird_SE_BG_md_out, EEC_dose_bird_SE_BG_lg_out)
        sum_8_BG = trex2_tables.table_sum_8(ARQ_diet_bird_SG_A_BG_out, ARQ_diet_bird_SG_C_BG_out, ARQ_diet_bird_TG_A_BG_out, ARQ_diet_bird_TG_C_BG_out, ARQ_diet_bird_BP_A_BG_out, ARQ_diet_bird_BP_C_BG_out, ARQ_diet_bird_FP_A_BG_out, ARQ_diet_bird_FP_C_BG_out, ARQ_diet_bird_AR_A_BG_out, ARQ_diet_bird_AR_C_BG_out)
        sum_9_BG = trex2_tables.table_sum_9(EEC_dose_mamm_SG_sm_BG_out, EEC_dose_mamm_SG_md_BG_out, EEC_dose_mamm_SG_lg_BG_out, EEC_dose_mamm_TG_sm_BG_out, EEC_dose_mamm_TG_md_BG_out, EEC_dose_mamm_TG_lg_BG_out, EEC_dose_mamm_BP_sm_BG_out, EEC_dose_mamm_BP_md_BG_out, EEC_dose_mamm_BP_lg_BG_out, EEC_dose_mamm_FP_sm_BG_out, EEC_dose_mamm_FP_md_BG_out, EEC_dose_mamm_FP_lg_BG_out, EEC_dose_mamm_AR_sm_BG_out, EEC_dose_mamm_AR_md_BG_out, EEC_dose_mamm_AR_lg_BG_out, EEC_dose_mamm_SE_sm_BG_out, EEC_dose_mamm_SE_md_BG_out, EEC_dose_mamm_SE_lg_BG_out)
        sum_10_BG = trex2_tables.table_sum_10(ARQ_dose_mamm_SG_sm_BG_out, CRQ_dose_mamm_SG_sm_BG_out, ARQ_dose_mamm_SG_md_BG_out, CRQ_dose_mamm_SG_md_BG_out, ARQ_dose_mamm_SG_lg_BG_out, CRQ_dose_mamm_SG_lg_BG_out, ARQ_dose_mamm_TG_sm_BG_out, CRQ_dose_mamm_TG_sm_BG_out, ARQ_dose_mamm_TG_md_BG_out, CRQ_dose_mamm_TG_md_BG_out, ARQ_dose_mamm_TG_lg_BG_out, CRQ_dose_mamm_TG_lg_BG_out, ARQ_dose_mamm_BP_sm_BG_out, CRQ_dose_mamm_BP_sm_BG_out, ARQ_dose_mamm_BP_md_BG_out, CRQ_dose_mamm_BP_md_BG_out, ARQ_dose_mamm_BP_lg_BG_out, CRQ_dose_mamm_BP_lg_BG_out, ARQ_dose_mamm_FP_sm_BG_out, CRQ_dose_mamm_FP_sm_BG_out, ARQ_dose_mamm_FP_md_BG_out, CRQ_dose_mamm_FP_md_BG_out, ARQ_dose_mamm_FP_lg_BG_out, CRQ_dose_mamm_FP_lg_BG_out, ARQ_dose_mamm_AR_sm_BG_out, CRQ_dose_mamm_AR_sm_BG_out, ARQ_dose_mamm_AR_md_BG_out, CRQ_dose_mamm_AR_md_BG_out, ARQ_dose_mamm_AR_lg_BG_out, CRQ_dose_mamm_AR_lg_BG_out, ARQ_dose_mamm_SE_sm_BG_out, CRQ_dose_mamm_SE_sm_BG_out, ARQ_dose_mamm_SE_md_BG_out, CRQ_dose_mamm_SE_md_BG_out, ARQ_dose_mamm_SE_lg_BG_out, CRQ_dose_mamm_SE_lg_BG_out)
        sum_11_BG = trex2_tables.table_sum_11(ARQ_diet_mamm_SG_BG_out, CRQ_diet_mamm_SG_BG_out, ARQ_diet_mamm_TG_BG_out, CRQ_diet_mamm_TG_BG_out, ARQ_diet_mamm_BP_BG_out, CRQ_diet_mamm_BP_BG_out, ARQ_diet_mamm_FP_BG_out, CRQ_diet_mamm_FP_BG_out, ARQ_diet_mamm_AR_BG_out, CRQ_diet_mamm_AR_BG_out)
        sum_14 = trex2_tables.table_sum_14(LD50_bg_bird_sm_out, LD50_bg_mamm_sm_out, LD50_bg_bird_md_out, LD50_bg_mamm_md_out, LD50_bg_bird_lg_out, LD50_bg_mamm_lg_out)
        html_sum = html_sum + sum_6_BG + sum_7_BG + sum_8_BG + sum_9_BG + sum_10_BG + sum_11_BG + sum_14

    if 'Broadcast-Liquid' in Application_type:
        sum_6_BL = trex2_tables.table_sum_6(Application_type_BL, 'Broadcast-Liquid', EEC_diet_SG_BL_out, EEC_diet_TG_BL_out, EEC_diet_BP_BL_out, EEC_diet_FR_BL_out, EEC_diet_AR_BL_out)
        sum_7_BL = trex2_tables.table_sum_7(EEC_dose_bird_SG_BL_sm_out, EEC_dose_bird_SG_BL_md_out, EEC_dose_bird_SG_BL_lg_out, EEC_dose_bird_TG_BL_sm_out, EEC_dose_bird_TG_BL_md_out, EEC_dose_bird_TG_BL_lg_out, EEC_dose_bird_BP_BL_sm_out, EEC_dose_bird_BP_BL_md_out, EEC_dose_bird_BP_BL_lg_out, EEC_dose_bird_FP_BL_sm_out, EEC_dose_bird_FP_BL_md_out, EEC_dose_bird_FP_BL_lg_out, EEC_dose_bird_AR_BL_sm_out, EEC_dose_bird_AR_BL_md_out, EEC_dose_bird_AR_BL_lg_out, EEC_dose_bird_SE_BL_sm_out, EEC_dose_bird_SE_BL_md_out, EEC_dose_bird_SE_BL_lg_out)
        sum_8_BL = trex2_tables.table_sum_8(ARQ_diet_bird_SG_A_BL_out, ARQ_diet_bird_SG_C_BL_out, ARQ_diet_bird_TG_A_BL_out, ARQ_diet_bird_TG_C_BL_out, ARQ_diet_bird_BP_A_BL_out, ARQ_diet_bird_BP_C_BL_out, ARQ_diet_bird_FP_A_BL_out, ARQ_diet_bird_FP_C_BL_out, ARQ_diet_bird_AR_A_BL_out, ARQ_diet_bird_AR_C_BL_out)
        sum_9_BL = trex2_tables.table_sum_9(EEC_dose_mamm_SG_sm_BL_out, EEC_dose_mamm_SG_md_BL_out, EEC_dose_mamm_SG_lg_BL_out, EEC_dose_mamm_TG_sm_BL_out, EEC_dose_mamm_TG_md_BL_out, EEC_dose_mamm_TG_lg_BL_out, EEC_dose_mamm_BP_sm_BL_out, EEC_dose_mamm_BP_md_BL_out, EEC_dose_mamm_BP_lg_BL_out, EEC_dose_mamm_FP_sm_BL_out, EEC_dose_mamm_FP_md_BL_out, EEC_dose_mamm_FP_lg_BL_out, EEC_dose_mamm_AR_sm_BL_out, EEC_dose_mamm_AR_md_BL_out, EEC_dose_mamm_AR_lg_BL_out, EEC_dose_mamm_SE_sm_BL_out, EEC_dose_mamm_SE_md_BL_out, EEC_dose_mamm_SE_lg_BL_out)
        sum_10_BL = trex2_tables.table_sum_10(ARQ_dose_mamm_SG_sm_BL_out, CRQ_dose_mamm_SG_sm_BL_out, ARQ_dose_mamm_SG_md_BL_out, CRQ_dose_mamm_SG_md_BL_out, ARQ_dose_mamm_SG_lg_BL_out, CRQ_dose_mamm_SG_lg_BL_out, ARQ_dose_mamm_TG_sm_BL_out, CRQ_dose_mamm_TG_sm_BL_out, ARQ_dose_mamm_TG_md_BL_out, CRQ_dose_mamm_TG_md_BL_out, ARQ_dose_mamm_TG_lg_BL_out, CRQ_dose_mamm_TG_lg_BL_out, ARQ_dose_mamm_BP_sm_BL_out, CRQ_dose_mamm_BP_sm_BL_out, ARQ_dose_mamm_BP_md_BL_out, CRQ_dose_mamm_BP_md_BL_out, ARQ_dose_mamm_BP_lg_BL_out, CRQ_dose_mamm_BP_lg_BL_out, ARQ_dose_mamm_FP_sm_BL_out, CRQ_dose_mamm_FP_sm_BL_out, ARQ_dose_mamm_FP_md_BL_out, CRQ_dose_mamm_FP_md_BL_out, ARQ_dose_mamm_FP_lg_BL_out, CRQ_dose_mamm_FP_lg_BL_out, ARQ_dose_mamm_AR_sm_BL_out, CRQ_dose_mamm_AR_sm_BL_out, ARQ_dose_mamm_AR_md_BL_out, CRQ_dose_mamm_AR_md_BL_out, ARQ_dose_mamm_AR_lg_BL_out, CRQ_dose_mamm_AR_lg_BL_out, ARQ_dose_mamm_SE_sm_BL_out, CRQ_dose_mamm_SE_sm_BL_out, ARQ_dose_mamm_SE_md_BL_out, CRQ_dose_mamm_SE_md_BL_out, ARQ_dose_mamm_SE_lg_BL_out, CRQ_dose_mamm_SE_lg_BL_out)
        sum_11_BL = trex2_tables.table_sum_11(ARQ_diet_mamm_SG_BL_out, CRQ_diet_mamm_SG_BL_out, ARQ_diet_mamm_TG_BL_out, CRQ_diet_mamm_TG_BL_out, ARQ_diet_mamm_BP_BL_out, CRQ_diet_mamm_BP_BL_out, ARQ_diet_mamm_FP_BL_out, CRQ_diet_mamm_FP_BL_out, ARQ_diet_mamm_AR_BL_out, CRQ_diet_mamm_AR_BL_out)
        sum_15 = trex2_tables.table_sum_15(LD50_bl_bird_sm_out, LD50_bl_mamm_sm_out, LD50_bl_bird_md_out, LD50_bl_mamm_md_out, LD50_bl_bird_lg_out, LD50_bl_mamm_lg_out)
        html_sum = html_sum + sum_6_BL + sum_7_BL + sum_8_BL + sum_9_BL + sum_10_BL + sum_11_BL + sum_15

    return html_sum + iter_html

class Trex2BatchOutputPage(webapp.RequestHandler):
    def post(self):
        form = cgi.FieldStorage()
        thefile = form['upfile']
        iter_html=loop_html(thefile)
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', 'title')
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'trex2','page':'batchinput'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        html = html + template.render(templatepath + '04uberbatch_start.html', {})
        html = html + iter_html
        html = html + template.render(templatepath + '04uberoutput_end.html', {'sub_title': ''})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', Trex2BatchOutputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    
    

