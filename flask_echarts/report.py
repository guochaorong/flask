# coding=utf-8
import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/report_chart', methods=['GET', 'POST'])
def report_chart():
    # define a page
    page = Page()
 
    # define a pie chart
    attr1 = ["New", "Pending", "Verified", "Fix", "Success"]
    value = [11, 12, 13, 10, 10]
    pie = Pie("Pie Chart Demo")
    pie.add("", attr1, value, is_label_show=True, center=[50, 50])
    page.add_chart(pie)
 
    # define a bar chart
    attr2 = ["New", "Pending", "Verified", "Fix", "Success"]
    v1 = [5, 20, 36, 10, 75]
    v2 = [10, 25, 8, 60, 20]
    bar = Bar("Bar Chart Demo")
    bar.add("Shop A", attr2, v1, is_stack=True)
    bar.add("Shop B", attr2, v2, is_stack=True)
    page.add_chart(bar)
 
    attr3 = ["New", "Pending", "Verified", "Fix", "Success"]
    v11 = [5, 20, 36, 10, 10]
    v22 = [55, 60, 16, 20, 15]
    line = Line("Line Chart Demo")
    line.add("Shop A", attr3, v11, mark_point=["average"])
    line.add("Shop B", attr3, v22, is_smooth=True, mark_line=["max", "average"])
    page.add_chart(line)
 
    return render_template('report_chart.html',
                           chart=page.render_embed(),
                           host='http://chfw.github.io/jupyter-echarts/echarts',
    script_list=page.get_js_dependencies())
