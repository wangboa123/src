import web

urls=(
		'','reblog',
		'/','blog'
)


blog_app = web.application(urls,locals())

class reblog:
	def GET(self):raise web.seeother('/')
	def POST(self):raise web.seeother('/')
class blog:
	def GET(self):
		return 'hello,blog'
	def POST(self):
		return 'hello,post blog'

if __name__=="__main__":
	blog_app.run()


