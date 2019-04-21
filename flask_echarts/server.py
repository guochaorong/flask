# coding=utf-8
import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()


from pyecharts import Bar
from pyecharts_javascripthon.api import TRANSLATOR
from flask import Flask, render_template


REMOTE_HOST = "https://pyecharts.github.io/assets/js"
#REMOTE_HOST = "https://github.com/guochaorong/assets/tree/master/js"
app = Flask(__name__)


@app.route("/")
def hello():
    _bar = bar_chart()
    print _bar
    javascript_snippet = TRANSLATOR.translate(_bar.options)
    return render_template(
        "pyecharts.html",
        chart_id=_bar.chart_id,
        host=REMOTE_HOST,
        renderer=_bar.renderer,
        my_width="100%",
        my_height=600,
        custom_function=javascript_snippet.function_snippet,
        options=javascript_snippet.option_snippet,
        script_list=_bar.get_js_dependencies(),
    )


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    return bar
