# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012

@author: jharston
"""

import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

class TRexAlgorithmPage(webapp.RequestHandler):
    def get(self):
        text_file1 = open('trex/trex_algorithm.txt','r')
        x = text_file1.read()        
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title':'Ubertool'})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'trex2','page':'algorithm'})
        html = html + template.render(templatepath + '03ubertext_links_left.html', {})                      
        html = html + template.render(templatepath + '04uberalgorithm_start.html', {
                'model':'trex', 
                'model_attributes':'TREX 1.5.1 Algorithms', 
                'text_paragraph':x})
#        html = html + template.render(templatepath + 'trex_algorithm.html', {}) 
#        html = html + '<iframe src="http://docs.google.com/gview?url=https://s3.amazonaws.com/przm/11.pdf&embedded=true" style="width:700px; height:900px;" frameborder="0"></iframe>'

        html = html + template.render(templatepath + '04ubertext_end.html', {})
        html = html + template.render(templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', TRexAlgorithmPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    
    
    
