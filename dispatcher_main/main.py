#-*- coding:utf-8 -*-
__author__ = 'Wangboa123'

import web
import sys
sys.path.append("..")

from blog.blog_app import blog_app

urls =(
		'/blog',blog_app,
		'/test','test'
		#'/forum','forum.forum_app'
)

app = web.application(urls,locals())
class test:
	def GET(self):
		return 'hello, world! '

if __name__=="__main__":
	app.run()
