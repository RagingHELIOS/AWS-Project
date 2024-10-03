from django.shortcuts import render

import mysql.connector as sql

# Create your views here.


def insertqry():
	qry = 'INSERT INTO reg( name, email, password) VALUES (%s,%s,%s)'
	return qry

def fetchdataqry():
	qry = 'select * from reg where email=%s'
	return qry

def datainsert(n,e,p):

	con = sql.connect(host='database-1.cliq6ukgombg.us-east-1.rds.amazonaws.com',user='admin',password='Qwerty789',database='HIT2',port=3306)
	db = con.cursor()

	db.execute(insertqry(),(n,e,p,))
	con.commit()

	db.close()
	con.close()
	print('Data inserted successfully')


def fetchdata(e):

	con = sql.connect(host='database-1.cliq6ukgombg.us-east-1.rds.amazonaws.com',user='admin',password='Qwerty789',database='HIT2',port=3306)
	db = con.cursor()

	db.execute(fetchdataqry(),(e,))
	x = db.fetchall()

	db.close()
	con.close()

	return x


def signup(request):

	if request.method == "POST":
		n = request.POST.get('name')
		e = request.POST.get('email')
		p = request.POST.get('password')

		print(n,e,p)

		if n!=None and e!=None and p!=None:
			datainsert(n,e,p)

	return render(request,'signup.html')



def login(request):

	l = []
	
	if request.method == "POST":
		
		e = request.POST.get('email')
		p = request.POST.get('password')

		print(e,p)

		if e!=None and p!=None:
			
			d = fetchdata(e)   #print(x[0][1])

			for data in d:
				l.append(data[3])
				l.append(data[1])

			if p in l:
				return render(request,'home_page.html',{'name':l[1]})
			else:
				return render(request,'login.html',{'msg':'Credential missmatch'})

				
		

	return render(request,'login.html')

