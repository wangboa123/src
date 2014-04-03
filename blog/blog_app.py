import web

urls=(
		'','reblog',
		'/test','test'
)


blog_app = web.application(urls,locals())

class reblog:
	def GET(self):raise web.seeother('/')
	def POST(self):raise web.seeother('/')
class test:
	def GET(self):
		return 'hello,blog'
	def POST(self):
		return 'hello,post blog'

if __name__=="__main__":
	blog_app.run()


