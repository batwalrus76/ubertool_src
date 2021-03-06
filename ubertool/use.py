import google.appengine.ext.db as db
import datetime
import time
import webapp2 as webapp
from django.utils import simplejson
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import sys
sys.path.append("../utils")
sys.path.append('../CAS')
from CAS.CASGql import CASGql
import logging

class Use(db.Model):
    config_name = db.StringProperty()
    user = db.UserProperty()
    cas_number = db.StringProperty()
    formulated_product_name = db.StringProperty()
    percent_ai = db.FloatProperty() 
    met_file = db.StringProperty()
    przm_scenario = db.StringProperty()
    exams_environment_file = db.StringProperty()
    application_method = db.StringProperty()
    application_type = db.StringProperty()
    app_type = db.StringProperty()
    weight_of_one_granule = db.FloatProperty()
    wetted_in = db.BooleanProperty()
    incorporation_depth = db.FloatProperty()
    percent_incorporated = db.FloatProperty()
    application_kg_rate = db.FloatProperty()
    application_lbs_rate = db.FloatProperty()
    seed_treatment_formulation_name = db.StringProperty()
    density_of_product = db.FloatProperty()
    maximum_seedling_rate_per_use = db.FloatProperty()
    application_rate_per_use = db.FloatProperty()
    application_date = db.DateProperty()
    number_of_applications = db.FloatProperty()
    interval_between_applications = db.FloatProperty()
    application_efficiency = db.FloatProperty()
    spray_drift = db.FloatProperty()
    runoff = db.FloatProperty()
    created = db.DateTimeProperty(auto_now_add=True)
