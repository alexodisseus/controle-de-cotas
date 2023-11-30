import app
import model
import math

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


shareholder = Blueprint('shareholder' , __name__ , url_prefix='/cotistas')





#usado para administrar os usuarios do sistema
@shareholder.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""



	filters = request.args.get('search')
	page = request.args.get('page', 1, type=int)
	per_page = 10
	offset = (page - 1) * per_page

	
	data = model.list_users_shareholder(filters, offset, per_page )
	
	count = model.count_users_shareholder(filters, offset, per_page )

	count = math.ceil(count/ per_page)
	pagination =[
	filters,
	page,
	offset,
	per_page,
	count
	]
	
	return render_template('shareholder/index.html' , data=data , pagination = pagination)
	#return render_template('login.html' )




@shareholder.route('/create', methods = ['GET','POST'])
def create():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':
		nome = request.form.get('name')
		email = request.form.get('email')
		cpf = request.form.get('cpf')
		birth = request.form.get('birth')
		telephone = request.form.get('telephone')
		cell = request.form.get('cell')
		addresses = request.form.get('addresses')
		accounts = request.form.get('accounts')
	
		model.create_shareholder(nome, email,cpf,birth,telephone, cell)

		return redirect(url_for('shareholder.index'))

	
	return render_template('shareholder/create.html' )
	

@shareholder.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	data = model.view_user_shareholder(id)
	
	return render_template('shareholder/view.html', data=data)





@shareholder.route('/quote/<id>', methods = ['GET','POST'])
def quote(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	data = model.view_user_shareholder_quote(id)
	
	

	return render_template('shareholder/view_quote.html', data=data)
	

@shareholder.route('/edit/<id>', methods = ['GET','POST'])

def edit(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':
		nome = request.form.get('name')
		email = request.form.get('email')
		cpf = request.form.get('cpf')
		birth = request.form.get('birth')
		telephone = request.form.get('telephone')
		cell = request.form.get('cell')
		street = request.form.get('street')
		number = request.form.get('number')
		city = request.form.get('city')
		state = request.form.get('state')
		cep = request.form.get('cep')
		accounts = request.form.get('accounts')
		print(id)
	
		model.update_shareholder(nome, email,cpf,birth,telephone, cell, street, number, city, state, cep, id)


		return redirect(url_for('shareholder.view' , id = id))

	data = model.view_user_shareholder(id)
	
	return render_template('shareholder/edit.html' , data=data )
	#return render_template('login.html' )

def configure(app):
	app.register_blueprint(shareholder)

