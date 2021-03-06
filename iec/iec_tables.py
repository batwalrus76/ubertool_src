import numpy
#import django
from django.template import Context, Template
from django.utils.safestring import mark_safe
from iec import iec_model
from iec import iec_parameters

def getheaderiv():
  headings = ["User Input", "Value"]
  return headings

def getheaderov():
  headings = ["IEC Output", "Value"]
  return headings

def gethtmlrowsfromcols(data, headings):
    columns = [data[heading] for heading in headings]

    # get the length of the longest column
    max_len = len(max(columns, key=len))

    for col in columns:
        # padding the short columns with None
        col += [None,] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows

def getdjtemplate():
    dj_template ="""
    <table class="out_" >
    {# headings #}
        <tr>
        {% for heading in headings %}
            <th>{{ heading }}</th>
        {% endfor %}
        </tr>
    {# data #}
    {% for row in data %}
    <tr>
        {% for val in row %}
        <td>{{ val|default:'' }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </table>
    """
    return dj_template

def gett1data(iec_obj):
    data = { 
        "User Input": ['LC50 or LD50', 'Threshold', 'Slope',],
        "Value": [iec_obj.LC50, iec_obj.threshold, iec_obj.dose_response,],
    }
    return data

def gett2data(iec_obj):
    data = { 
        "IEC Output": ['Z Score', '"F8"', 'Chance of Individual Effect',],
        "Value": ['%.2f' % iec_obj.z_score,'%.2e' % iec_obj.F8,'%.2f' % iec_obj.chance, ],
    }
    return data

ivheadings = getheaderiv()
ovheadings = getheaderov()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(iec_obj):
    html_all = table_1(iec_obj)
    html_all = html_all + table_2(iec_obj)
    return html_all

def table_1(iec_obj):
    #pre-table 1
        html = """
        <H4 class="out_1 collapsible" id="section1"><span></span>User Inputs</H4>
            <div class="out_ container_output">
        """
    #table 1
        t1data = gett1data(iec_obj)
        t1rows = gethtmlrowsfromcols(t1data,ivheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=ivheadings)))
        html = html + """
            </div>
        """
        return html

def table_2(iec_obj):
    #pre-table 1
        html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Model Output</H4>
            <div class="out_ container_output">
        """
        # z_score_f=iec_model.z_score_f(iec_obj.dose_response, iec_obj.LC50, iec_obj.threshold)
        # F8_f=iec_model.F8_f(iec_obj.dose_response, iec_obj.LC50, iec_obj.threshold)
        # chance_f=iec_model.chance_f(iec_obj.dose_response, iec_obj.LC50, iec_obj.threshold)

    #table 2
        t2data = gett2data(iec_obj)
        t2rows = gethtmlrowsfromcols(t2data,ovheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=ovheadings)))
        html = html + """
            </div>
        """
        return html