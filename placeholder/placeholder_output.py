# -*- coding: utf-8 -*-

# IEC
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
#from iec import iec_input      <---- HAS THIS BEEN DONE?  (I JUST CHANGED THE NAME)
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
#import numpy as np
import cgi
import math 
import cgitb
cgitb.enable()



 
class placeholderOutputPage(webapp.RequestHandler):
    def post(self):        
        form = cgi.FieldStorage()   
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01hh_uberheader.html', {'title':'Ubertool'})        
        html = html + template.render(templatepath + '02hh_uberintroblock_wmodellinks.html',  {'model':'placeholder','page':'output'})
        html = html + template.render (templatepath + '03hh_ubertext_links_left.html', {})                               
        html = html + template.render(templatepath + '04uberoutput_start.html', {
                'model':'placeholder', 
                'model_attributes':'Placeholder Output'})
        html = html + """
        <table width="600" border="1">
          
        </table>
        <p>&nbsp;</p>                     
        """
        html = html + """
        <table width="600" border="1">
        </table>
        """
        html = html + template.render(templatepath + '04uberoutput_end.html', {})
        html = html + template.render(templatepath + '05hh_ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06hh_uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', placeholderOutputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()

 

    