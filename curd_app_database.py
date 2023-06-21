import mysql.connector

try:
    db = mysql.connector.connect(host='localhost', user='root', password='1234', database='crudapp')
except:
    print('off, database connectivity failed')
else:
    print('database connected successfully')

mycursor = db.cursor(buffered=True)


def create_record(id, companyname,owners,location,turnover):
    mycursor.execute('INSERT INTO FRONT (ID, COMPANYNAME, OWNERS , LOCATION, TURNOVER) VALUES(%s ,%s, %s, %s, %s)',(id,companyname,owners,location,turnover))
    db.commit()

def read_record():
    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM FRONT')
    mv = mycursor.fetchall()
    db.commit()
    return mv

def read_record_id(id):
    mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM FRONT WHERE ID = %s',(id,))
    mv = mycursor.fetchall()
    db.commit()
    return mv

def update_record(companyname,owners,location , turnover,id):
    mycursor.execute('UPDATE FRONT SET COMPANYNAME = %s, OWNERS = %s , LOCATION = %s, TURNOVER = %s WHERE ID = %s',(companyname,owners,location , turnover,id))
    db.commit()
def delete_record(id):
    mycursor.execute('DELETE FROM FRONT WHERE ID = %s',(id,))
    db.commit()

'''
task = int(input('what you want to do\n press 1 for create\n press 2 for get your data\n press 3 for update\n press 4 for delete'))
if task==1:
    id = input('press the id\n')
    companyname = input('company name: \n')
    owners = input('owner name: \n')
    location = input('location: \n')
    turnover = input('turnover yearly in usd: \n')
    create_record(id, companyname, owners, location, turnover)

elif task==2:
    read_record()
elif task==3:
    id = input('press the id\n')
    companyname = input('company name: \n')
    owners = input('owner name: \n')
    location = input('location: \n')
    turnover = input('turnover yearly in usd: \n')
    update_record(companyname,owners,location , turnover,id)
elif task == 4:
    id = input('press the id\n')
    delete_record(id)
'''