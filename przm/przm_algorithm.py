# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012

@author: jharston
"""

import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

class PRZMAlgorithmPage(webapp.RequestHandler):
    def get(self):
        text_file1 = open('przm/przm_algorithm.txt','r')
        x = text_file1.read()
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title'})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'przm','page':'algorithm'})
        html = html + template.render(templatepath + '03ubertext_links_left.html', {})                        
        html = html + template.render(templatepath + '04uberalgorithm_start.html', {
                'model':'przm', 
                'model_attributes':'PRZM Algorithms', 
                'text_paragraph':x})
        html = html + template.render(templatepath + '04ubertext_end.html', {})
        html = html + template.render(templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', PRZMAlgorithmPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    