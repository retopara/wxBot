#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        # if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
        #     self.send_msg_by_uid(u'hi', msg['user']['id'])
        #     #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
        #     #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

        print("inside handle all msg, msg_id = ", msg['msg_id'])
        print("msg_type_id = ", msg['msg_type_id'], "msg_content_type = ", msg['content']['type'])

        if msg['msg_type_id'] == 3 and msg['content']['type'] == 3:
            print("this should be a image message, pic saved to ./temp/", self.get_msg_img(msg['msg_id']))
            # print("pic saved to ./temp/", self.get_msg_img(msg['msg_id']))

        if msg['msg_type_id'] == 3 and msg['content']['type'] == 13:
            print("this should be a SMALL VIDEO, saved to ./temp/", self.get_video(msg['msg_id']))

        if msg['msg_type_id'] == 3 and msg['content']['type'] == 8:
            print("this should be a video message, saved to ./temp/", self.get_video(msg['msg_id']))
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()