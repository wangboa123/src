import web

db = web.database(dbn='mysql',db='blog',user='root',pw='root')

#user class is used to crud users
#this is dao layer

class mydb:
	def __init__(self):
		pass
	@classmethod
	def test(cls,data,**values):
		print "data = %s" % data
	@classmethod
	def create(cls, tables, **values):
		return db.insert(tables,seqname=None,_test=False,**values)		
	@classmethod
	def update(cls,tables,where_cond,**values):
		return db.update(tables,where=where_cond,vars=None,\
				_test= False,**values)
	@classmethod
	def delete(cls,tabels,where_conditon):
		return db.delete(tables,where=where_condition)
	#this is the sql operator
	@classmethod
	def query(cls,sql):
		return list(db.query(sql))

	
	#the real use of select is 
	#1. get top n(1,2...,100)
	#2. get where condition
	#3. order
	#4. maybe group,

	#get all data from one table
	@classmethod
	def selectall(cls,tables):
		return list(db.select(tables))

	@classmethod
	def selecttopn(cls,tables,n):
		return list(db.select(tables,limit=n))
	@classmethod
	def selectwhere(cls,tables,condition):
		return list(db.select(tables,where=condition))
	#orderdata maybe like order="post_date DESC"
	@classmethod
	def selectorder(cls,tables,orderdata):
		return list(db.select(tables,order=orderdata))

#testcode use localdatabase and test table 
if __name__=="__main__":

	mydb.test("hello,world!",**{})
	#use transcation
	t = db.transaction()
	try:
		#test create
		insertdata = {'user_name':'wangke',
			'passwd':'123',
			'user_job':'teacher'
			}
		ret=mydb.create('test',**insertdata)
		if ret > 0:
			print "test create ok \n"
		else:
			print "test create fail \n"
	except:
		t.rollback()
		print "transaction fail \n"
		raise
	else:
		t.commit()

	#test selectwhere and update
	t = db.transaction()
	try:
		ret = mydb.selectwhere('test','user_name="wangke"')
		getid = str(ret[0].id)
		mydb.update('test',where_cond='id='+getid,**{'user_name':'shuaike'})
	except:
		t.rollback()
		print "transaction fail \n"
		raise
	else:
		t.commit()
	
	#test selectall
	ret = mydb.selectall('test')
	if len(ret)>0:
		print "selectall is ok \n"
	else:
		print "selectall is fail \n"

	#test query
	ret = mydb.query("select * from test")
	if len(ret)>0:
		print "query is ok \n"
	else:
		print "query is fail \n"


	


	



