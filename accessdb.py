from flask import Flask,render_template,request
import MySQLdb
app = Flask(__name__)
db=MySQLdb.connect("DB-IP",'DB_User','DB_user_password','DB_name')#location,username,password,dbname
#db=MySQLdb.connect("localhost",'root','root','testdb')#location,username,password,dbname
cursor = db.cursor()


@app.route('/option')
def hello_world():
	#return ('Hello world')
	return render_template('select.html')
   
   
@app.route("/add/")
def add():
	return render_template('add.html')
	
@app.route("/add_detail",methods = ['POST', 'GET'])
def add_detail():
	
	if request.method == 'POST':
		try:
			ID=request.form['ID']
			fname = request.form['fname']
			lname = request.form['lname']
			age = request.form['age']
			sex = request.form['sex']
			percentage=request.form['percentage']
			town=request.form['town']
			sql="INSERT INTO student(ID,FNAME,LNAME,AGE,SEX,PERCENTAGE,TOWN) VALUES ({},'{}','{}',{},'{}',{},'{}')".format(ID,fname,lname,age,sex,percentage,town)
			print(sql)
			cursor.execute(sql)
			db.commit()
			msg = "Record successfully added"
		except Exception as e:
			db.rollback()
			msg = "error in insert operation"
			print("exception",e)
      
		finally:
			return msg
			db.close()



@app.route("/delete/")
def delete():
	return render_template('delete.html')


@app.route("/delete_detail",methods = ['POST', 'GET'])
def delete_value():
	if request.method == 'POST':
		try:
			ID = request.form['ID']
			
			sql="DELETE FROM student WHERE ID = {};".format(ID)
			print(sql)
			cursor.execute(sql)
			db.commit()
			msg = "Record successfully Deleted"
		except Exception as e:
			db.rollback()
			msg = "error in insert operation"
			print("exception",e)
      
		finally:
			return msg
			db.close()
	
@app.route("/update/")
def update():
	return render_template("update.html")
	
@app.route("/update_detail",methods = ['POST','GET'])
def update_detail():
	if request.method == 'POST':
		try:
			fname = request.form['fname']
			
			sql="DELETE FROM student WHERE FNAME = '{}';".format(fname)
			print(sql)
			cursor.execute(sql)
			db.commit()
			msg = "Record successfully Deleted"
		except Exception as e:
			db.rollback()
			msg = "error in insert operation"
			print("exception",e)
      
		finally:
			return msg
			db.close()
	

@app.route("/fetch/")
def fetch1():
	sql = "SELECT * FROM student"
	try :
		cursor.execute(sql)
		fetch_all_record = cursor.fetchall()
	except:
		print("rollback")
		db.rollback()

	return render_template('fetch.html',data=fetch_all_record)
	



if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)
