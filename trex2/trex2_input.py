# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012
@author: thong
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import cgitb
cgitb.enable()
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from trex2 import trex2_parameters
from django import forms

class trexInputPage(webapp.RequestHandler):
    def get(self):
        text_file = open('trex/trex_description.txt','r')
        x = text_file.read()
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title':'Ubertool'})
        html = html + template.render (templatepath + 'trex2-jquery.html', {})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'trex2','page':'input'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})        
        html = html + template.render (templatepath + '04uberinput_start.html', {
                'model':'trex2', 
                'model_attributes':'TREX 1.5.1 Inputs'})
        html = html + """<a href="trex_input.html" class="TREX1"> Want to Use TREX 1.4.1?</a>"""
        html = html + """<table><H4  align="center" id="id_tab">
            |<a class="Chemical" style="color:#FFA500; font-weight:bold"> Chemical </a>|
             <a class="Avian" style="font-weight:bold"> Avian </a>|
             <a class="Mammal" style="font-weight:bold"> Mammal </a>|
            </H4>"""
        html = html + """</table><br><table class="tab tab_Chemical" border="0">"""
        html = html + str(trex2_parameters.trexInp_chem())
        html = html + """</table><table class="tab tab_Application" border="0">
                                    <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                        <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                            <option value="">Make a selection</option>
                                            <option value="1">1</option>
                                            <option value="2">2</option>
                                            <option value="3">3</option></select>
                                        </td>
                                    </tr>""" 
        html = html + """</table><table class="tab tab_Avian" border="0" style="display:none">"""
        html = html + str(trex2_parameters.trexInp_bird())
        html = html + """</table><table class="tab tab_Mammal" border="0" style="display:none">"""
        html = html + str(trex2_parameters.trexInp_mammal())
        html = html + template.render(templatepath + 'trex2_input_end.html', {'sub_title': 'Submit'})
      #  html = html + str(trexdb2.trexInp())
        # html = html + str(trexdb2.trexApp())     
        # html = html + template.render (templatepath + '04uberinput_end.html', {'sub_title': 'Submit'})
        # html = html + template.render (templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', trexInputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    
    