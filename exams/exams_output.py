# -*- coding: utf-8 -*-

# IEC
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
#from iec import iec_input      <---- HAS THIS BEEN DONE?  (I JUST CHANGED THE NAME)
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
#import numpy as np
#import cgi
#import math 
#import cgitb
#cgitb.enable()


  
 
class IecOutputPage(webapp.RequestHandler):
    def post(self):
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title':'Ubertool'})        
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html',  {'model':'iec'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                               
        html = html + template.render(templatepath + '04uberoutput_start.html', {
                'model':'generic', 
                'model_attributes':'generic Output'})
        html = html + """
        <table width="600" border="1">
          <tr>
            <th width="300" scope="col">User Inputs</div></th>
            <th width="300" scope="col">Values</div></th>
          </tr>
          <tr>
            <td>LC50 or LD50</td>
            <td>%.2f</td>
          </tr>          
          <tr>
           <td>Threshold</td>
           <td>%.2f</td>
          </tr>          
          <tr>
           <td>Slope</td>
           <td>%.2f</td>
          </tr>
        </table>
        <p>&nbsp;</p>                     
        """%(LC50, threshold, dose_response)                   
        html = html + """
        <table width="600" border="1">
          <tr>
            <th width="300" scope="col">IEC Outputs</div></th>
            <th width="300" scope="col">Values</div></th>
          </tr>
            <td>Z Score</td>
            <td>%.2f</td>
          </tr>           
          <tr>
          <tr>
            <td>"F8"</td>
            <td>%.8f</td>
          </tr>           
          <tr>
            <td>Chance of Individual Effect</td>
            <td>%.2f</td>
          </tr>          
        </table>
        """%(z_score_f(dose_response, LC50, threshold), F8_f(dose_response, LC50, threshold),chance_f(dose_response, LC50, threshold))
        html = html + template.render(templatepath + '04uberoutput_end.html', {})
        html = html + template.render(templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', IecOutputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()

 

    