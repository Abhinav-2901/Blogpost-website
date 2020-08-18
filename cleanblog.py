from flask import *

import sqlite3

app=Flask(__name__)


app.secret_key="very-secret-key"






@app.route('/')

def home():
	
	
	conn=sqlite3.connect('cleanblog.db')
	
	temp=conn.execute("select * from post")
	
	temp1=conn.execute("select * from header")
	
	temp2=conn.execute("select * from mainheading")
	
	temp3=conn.execute("select * from footer")
	
	
	return render_template('index.html',temp=temp,data1=temp1,data2=temp2,data3=temp3)
	
	
	
	
	


@app.route('/about')

def about():
	
	
	conn=sqlite3.connect('cleanblog.db')
	
	temp1=conn.execute("select * from header")
	
	temp3=conn.execute("select * from footer")
	
	
	
	return render_template('about.html',data1=temp1,data3=temp3)
	
	
	
	
	
	
	
@app.route('/contact', methods=['POST','GET'])

def contact():
	
	if request.method=='POST':
			
		name=request.form['nm']
		email=request.form['em']
		phone=request.form['ph']
		msgg=request.form['msg']
		
		conn=sqlite3.connect('cleanblog.db')
		
		input="insert into contact(name,email,phone,message)values(?,?,?,?)"
		
		conn.execute(input,(name,email,phone,msgg))
		
		conn.commit()
		
		return redirect('/contact')
		
	else:
		
		conn=sqlite3.connect('cleanblog.db')
		
	
		temp1=conn.execute("select * from header")
	
	
		temp3=conn.execute("select * from footer")
		
		
		
		return render_template('contact.html',data1=temp1,data3=temp3)
		







@app.route('/post/<int:id>')

def post(id):
	
	
	conn=sqlite3.connect('cleanblog.db')
	
	temp=conn.execute("select * from post where id=?",(id,))
	
	conn.commit()
	
	temp1=conn.execute("select * from header")
	
	temp3=conn.execute("select * from footer")

	
	return render_template('post.html',data=temp,data1=temp1,data3=temp3)
	







@app.route('/login', methods=['POST','GET'])

def login():
	
	
	#if 'username' in session:
		
		#return redirect('/dashbord')
	
	
		
		
	
	if request.method=='POST':
		
		username=request.form['un']
		
		session["username"]=username
		
		password=request.form['pass']
		
		conn=sqlite3.connect('cleanblog.db')
		
		data=conn.execute("select * from login")
		
		for row in data:
			
			if (username==row[0]) and (password==row[1]):
			
				return redirect('/dashbord')
			
			else:
			
				return redirect('/login')
		
		
		
	
	
	else:
		
		return render_template('login.html')
		





@app.route('/dashbord')

def dashbord():
	
	if 'username' in session:
		
		return render_template('dashbordhome.html')
		
	else:
		
		
		return render_template('login.html')
		
		
	
	
	
	





@app.route('/manageposts')

def manageposts():
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		temp=conn.execute("select * from post")
	
		conn.commit()

	
		return render_template('managepost.html',data=temp)
		
		
	
	else:
		
		return render_template('login.html')
	
	
	
	
	
	
	
	
	
	

@app.route('/managecontacts')

def managecontacts():
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
	
		temp=conn.execute("select * from contact")
	
		conn.commit()

	
		return render_template('managecontacts.html',data=temp)
	
	
	
	else:
		
		return render_template('/login.html')
	
	
	
	
	
	
	
	
	
@app.route('/deletepost/<int:id>')

def deletepost(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		conn.execute("delete from post where id=?",(id,))
	
		conn.commit()
	
		return redirect('/manageposts')
		
	else:
		
		return render_template('login.html')
	
	
	
	
	
	
	
	
	
@app.route('/deletecontact/<int:id>')

def deletecontact(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		conn.execute("delete from contact where id=?",(id,))
	
		conn.commit()
	
		return redirect('/managecontacts')
		
	else:
		
		
		return render_template('login.html')
	
	
	
	
	
	
	
	
@app.route('/add', methods=['POST','GET'])

def add():
	
	
	
	if 'username' in session:
		
		if request.method=='POST':
		
		
			title=request.form['ttl']
		
			subtitle=request.form['sbtl']
		
			content=request.form['cnt']
		
			by=request.form['by']
		
			date=request.form['dt']
			
			image=request.form['img']
		
		
		
			conn=sqlite3.connect('cleanblog.db')
		
			conn.execute("insert into post(title,subhead,content,by,date,image)values(?,?,?,?,?,?)",(title,subtitle,content,by,date,image))
		
			conn.commit()
		
			return redirect('/manageposts')
	
		else:
		
			return render_template('managepost.html')
			
			
		
	else:
		
		return render_template('login.html')
		
		
	
	
	
	
		
		
		
		
		
@app.route('/editpost/<int:id>')

def editpost(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		temp=conn.execute("select * from post where id=?",(id,))
	
		return render_template('editpost.html',data=temp)
		
		
		
	else:
		
		return render_template('login.html')
	
	
	
	
	
	

@app.route('/updatepost/<int:id>', methods=['POST','GET'])



def updatepost(id):
	
	
	if 'username' in session:
		
		
		if request.method=='POST':
			title=request.form['tl']
			subtitle=request.form['sbtl']
			content=request.form['cnt']
			by=request.form['by']
			date=request.form['dt']
			image=request.form['img']
		
			conn=sqlite3.connect('cleanblog.db')
		
		
			change="update post set title=?,subhead=?,content=?,by=?,date=?,image=? where Id=?"
			data=(title,subtitle,content,by,date,image,id)
		
			conn.execute(change,data)
		
			conn.commit()
		
			return redirect('/manageposts')
			
			
			
		
	else:
		
		return render_template('login.html')
		
		
		
@app.route('/settings')

def settings():
	
	if 'username' in session:
		
		conn=sqlite3.connect('cleanblog.db')
		
		temp1=conn.execute("select * from header")
	
		conn.commit()
		
		temp2=conn.execute("select * from mainheading")
	
		conn.commit()
		
		temp3=conn.execute("select * from footer")
	
		conn.commit()
		
		
		
		return render_template('setting.html',data1=temp1,data2=temp2,data3=temp3)
		
	else:
		
		return render_template('login.html')
		
		
		
		
		
		
@app.route('/editheader/<int:id>')

def editheader(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		temp=conn.execute("select * from header where id=?",(id,))
	
		return render_template('editheader.html',data=temp)
		
		
		
	else:
		
		return render_template('login.html')
		
		
	
		
@app.route('/updateheader/<int:id>', methods=['POST','GET'])		
		

def updateheader(id):
	
	
	if 'username' in session:
		
		
		if request.method=='POST':
			header=request.form['hd']
		
			conn=sqlite3.connect('cleanblog.db')
		
		
			change="update header set title=? where Id=?"
			data=(header,id)
		
			conn.execute(change,data)
		
			conn.commit()
		
			return redirect('/settings')
			
			
			
		
	else:
		
		return render_template('login.html')
		
		
		
		



		
		
@app.route('/editmainheading/<int:id>')

def editmainheading(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		temp=conn.execute("select * from mainheading where id=?",(id,))
	
		return render_template('editmainheading.html',data=temp)
		
		
		
	else:
		
		return render_template('login.html')
		
		
		
		
@app.route('/updatemainheading/<int:id>', methods=['POST','GET'])		
		

def updatemainheading(id):
	
	
	if 'username' in session:
		
		
		if request.method=='POST':
			
			title=request.form['ttl']
			
			subtitle=request.form['sbtl']
			
			conn=sqlite3.connect('cleanblog.db')
		
		
			change="update mainheading set title=?, subtitel=? where Id=?"
			data=(title,subtitle,id)
		
			conn.execute(change,data)
		
			conn.commit()
		
			return redirect('/settings')
			
			
			
		
	else:
		
		return render_template('login.html')
		
		
		
@app.route('/editfooter/<int:id>')

def editfooter(id):
	
	
	if 'username' in session:
		
		
		conn=sqlite3.connect('cleanblog.db')
	
		temp=conn.execute("select * from footer where id=?",(id,))
	
		return render_template('editfooter.html',data=temp)
		
		
		
	else:
		
		return render_template('login.html')
		
		
		
@app.route('/updatefooter/<int:id>', methods=['POST','GET'])		
		

def updatefooter(id):
	
	
	if 'username' in session:
		
		
		if request.method=='POST':
			footer=request.form['ft']
		
			conn=sqlite3.connect('cleanblog.db')
		
		
			change="update footer set title=? where Id=?"
			data=(footer,id)
		
			conn.execute(change,data)
		
			conn.commit()
		
			return redirect('/settings')
			
			
			
		
	else:
		
		return render_template('login.html')
		
		
		
		
		
@app.route('/logout')


def logout():
   
   session.pop('username', None)
   
   return redirect('/login')
	
	
	
	
		
	
	
	
		
		
	
if __name__=='__main__':
	
	app.run(debug=True)
	