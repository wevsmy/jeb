# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: robot.py
# @Time: 2020/6/8 10:52
from werobot import WeRoBot
from werobot.client import Client
from werobot.messages.messages import *

from app.config.settings import WX_PUBLIC_TOKEN

wx_robot = WeRoBot(token=WX_PUBLIC_TOKEN)


# Event
# #################################################################

# 新用户关注的消息
@wx_robot.subscribe
def subscribe(message):
    return 'Hello My Friend!'


# 取消关注事件
@wx_robot.unsubscribe
def unsubscribe(message):
    return 'unsubscribe'


# Message
# #################################################################


@wx_robot.filter("帮助")
def show_help(message):
    return """
    帮助
    XXXXX
    """


@wx_robot.text
def text(message: TextMessage, session: dict):
    print("text:", type(message), type(session))

    print(message.message_id)
    print(message.target)
    print(message.source)
    print(message.time)

    print(message.__type__)
    print(message.content)

    if 'first' in session:
        return '你之前给我发过消息' + message.content
    session['first'] = True
    return '你之前没给我发过消息' + message.content


@wx_robot.image
def image(message: ImageMessage, session):
    print("image:", type(message), type(session))

    print(message.__type__)
    print(message.img)
    return message.img


@wx_robot.link
def link(message: LinkMessage, session):
    print("link:", type(message), type(session))

    print(message.__type__)
    print(message.title)
    print(message.description)
    print(message.url)
    return "我点不了 link"


@wx_robot.location
def location(message: LocationMessage, session):
    print("location:", type(message), type(session))

    print(message.__type__)
    print(message.location)
    print(message.scale)
    print(message.label)
    return "我去不了 location"


@wx_robot.voice
def link(message: VoiceMessage, session):
    print("voice:", type(message), type(session))

    print(message.message_id)
    print(message.target)
    print(message.source)
    print(message.time)

    print(message.media_id)
    print(message.format)
    print(message.recognition)

    return "我听不懂 voice"


@wx_robot.video
def link(message: VideoMessage, session):
    print("video:", type(message), type(session))
    return "我看不到 video"


# Error
# #################################################################

# Signature 验证不通过时显示的错误页面
@wx_robot.error_page
def make_error_page(url):
    return "<h1>喵喵喵 %s 不是给麻瓜访问的快走开</h1>" % url


# Handler
# #################################################################
@wx_robot.handler
def hello(message, session):
    print("handler:", type(message), type(session))
    print(message.__type__)
    return '不支持消息类型：{}'.format(type(message))


if __name__ == '__main__':
    # Client
    # #################################################################
    c = Client(config={
        "APP_ID": "wx8df663f95f624ddc",
        "APP_SECRET": "9af6b8495185cfc6c4b5cea7e8bf7f07"
    })

    res = c.get_followers(first_user_id=None)
    print(res)
    c.send_text_message(user_id="oBCxywNx_nthmopfu914jLSVuobU", content="你好")

    pass
