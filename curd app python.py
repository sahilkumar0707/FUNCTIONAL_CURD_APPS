from flask import Flask,render_template,request, flash
import mysql.connector
import curd_app_database

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('curd_app_gui.html')

try:
    db = mysql.connector.connect(host='localhost', user='root', password='1234', database='crudapp')
except:
    print('off, database connectivity failed')
else:
    print('database connected successfully')



@app.route('/script1', methods=['POST'])
def handle_script1():
    data = curd_app_database.read_record()
    return render_template('read.html' ,result = data)
'''mycursor = db.cursor(buffered=True)
    mycursor.execute('SELECT * FROM FRONT')
    result = mycursor.fetchall()
    mv = str(result)'''





@app.route('/delete', methods=['POST'])
def delete():

    return render_template('delete.html')

# Add more routes for additional scripts


@app.route('/create', methods=['POST'])
def create():



    return render_template('create.html')

# Add more routes for additional scripts

@app.route('/update', methods=['POST'])
def update():
    # Code to handle the second button click
    # Execute the desired Python script for button 2

    return render_template('update.html')

@app.route('/create_done', methods=['POST'])
def create_done():
    mycursor = db.cursor(buffered=True)
    # Code to handle the second button click
    # Execute the desired Python script for button 2
    id = request.form.get('id')
    companyname = request.form.get('companyname')
    owners = request.form.get('owners')
    location = request.form.get('location')
    turnover = request.form.get('turnover')
    create_result = [id, companyname, owners, location, turnover]
    curd_app_database.create_record(id, companyname, owners, location, turnover)

    db.commit()
    # Code to handle the second button click
    # Execute the desired Python script for button 2

    return render_template('curd_app_gui.html')

@app.route('/delete_done', methods=['POST'])
def delete_done():
    ids =request.form.get('delete')
    mycursor = db.cursor()
    flash('deleted sucessfully')
    curd_app_database.delete_record(ids)

    #mycursor.execute('DELETE FROM FRONT WHERE ID = %s',(ids,))

    db.commit()

    return render_template('delete.html')


@app.route('/update_id', methods=['POST'])
def update_id():
    global idss
    idss =request.form.get('update')
    global reading
    reading = curd_app_database.read_record_id(idss)

    db.commit()

    return render_template('update_info.html' ,result3 = reading)

@app.route('/update_info', methods=['POST'])
def update_info():
    mycursor = db.cursor()
    id = idss
    companyname = request.form.get('companyname')
    owners = request.form.get('owners')
    location = request.form.get('location')
    turnover = request.form.get('turnover')
    curd_app_database.update_record(companyname,owners,location,turnover,id)

    '''query = "UPDATE FRONT SET COMPANYNAME = %s, OWNERS = %s , LOCATION = %s , TURNOVER = %s WHERE id = %s"
    val = (companyname,owners,location,turnover,id)
    mycursor.execute(query,val)'''
    db.commit()
    return render_template('curd_app_gui.html')


if __name__ == '__main__':
    app.run(debug=True)