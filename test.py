#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        """
        This function auto saves pics/videos in group messages
        :param msg: the message dict
        :return: None
        """

        if msg['msg_type_id'] == 3:
            print("inside handle all msg "
                  , "msg_id = ", msg['msg_id']
                  , "msg_type_id = ", msg['msg_type_id']
                  , "msg_content_type = ", msg['content']['type']
                  , "group_name = ", msg['user']['name'].decode('utf-8')
                  )

            if msg['content']['type'] == 3:
                print("this should be a image message, pic saved to ./temp/", self.get_msg_img(msg))
                # print("pic saved to ./temp/", self.get_msg_img(msg['msg_id']))

            if msg['content']['type'] == 13:
                print("this should be a SMALL VIDEO, saved to ./temp/", self.get_video(msg))

            if msg['content']['type'] == 8:
                print("this should be a video message, saved to ./temp/", self.get_video(msg))

    def get_msg_img(self, msg):
        """
        获取图片消息，下载群内图片到本地分为不同群名的文件夹
        :param msg: 消息
        :return: 保存的本地图片文件路径
        """
        url = self.base_uri + '/webwxgetmsgimg?MsgID=%s&skey=%s' % (msg['msg_id'], self.skey)
        r = self.session.get(url)
        data = r.content
        fn = 'img_' + msg['msg_id'] + '.jpg'
        fpath = os.path.join(os.getcwd(), msg['user']['name'].decode('utf-8'))
        if not os.path.isdir(fpath):
            os.makedirs(fpath)
        with open(os.path.join(fpath, fn), 'wb') as f:
            f.write(data)
        return fn

    def get_video(self, msg):
        """
        获取视频消息，下载视频到本地
        :param msg: 视频消息
        :return: 保存的本地视频文件路径
        """
        url = self.base_uri + '/webwxgetvideo?msgid=%s&skey=%s' % (msg['msg_id'], self.skey)
        headers = {'Range': 'bytes=0-'}
        r = self.session.get(url, headers=headers)
        data = r.content
        fn = 'video_' + msg['msg_id'] + '.mp4'
        fpath = os.path.join(os.getcwd(), msg['user']['name'].decode('utf-8'))
        if not os.path.isdir(fpath):
            os.makedirs(fpath)
        with open(os.path.join(fpath, fn), 'wb') as f:
            f.write(data)
        return fn


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
