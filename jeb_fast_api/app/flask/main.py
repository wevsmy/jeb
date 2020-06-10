# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: main.py
# @Time: 2020/6/8 10:52
from flask import Flask, escape, request
from werobot.contrib.flask import make_view

from app.flask.werobot.robot import wx_robot

flask_app = Flask(__name__)
flask_app.add_url_rule(rule='/robot/',  # WeRoBot 挂载地址
                       endpoint='werobot',  # Flask 的 endpoint
                       view_func=make_view(wx_robot),
                       methods=['GET', 'POST'])


@flask_app.route('/')
def hello_world():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


if __name__ == '__main__':
    flask_app.run()
