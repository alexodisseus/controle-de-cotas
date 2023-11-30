import app
import model
import math

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


closure = Blueprint('closure' , __name__ , url_prefix='/fechamento')




@closure.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""


	filters = request.args.get('search')
	page = request.args.get('page', 1, type=int)
	per_page = 10
	offset = (page - 1) * per_page

	
	data = model.list_closure(filters, offset, per_page )
	
	count = model.count_closure(filters, offset, per_page )

	count = math.ceil(count/ per_page)
	pagination =[
	filters,
	page,
	offset,
	per_page,
	count
	]
	
	return render_template('closure/index.html' , data=data , pagination = pagination)
	#return render_template('login.html' )


@closure.route('/listar', methods = ['GET','POST'])
def list():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""


	filters = request.args.get('search')
	page = request.args.get('page', 1, type=int)
	per_page = 10
	offset = (page - 1) * per_page

	
	data = model.list_closure(filters, offset, per_page )
	
	count = model.count_closure(filters, offset, per_page )

	count = math.ceil(count/ per_page)
	pagination =[
	filters,
	page,
	offset,
	per_page,
	count
	]
	
	return render_template('closure/list.html' , data=data , pagination = pagination)
	#return render_template('login.html' )

@closure.route('/create', methods = ['GET','POST'])
def create():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':
		date = request.form.get('data')
		value = request.form.get('valorTitulo')
		
		model.create_closure(date, value)

		return redirect(url_for('closure.index'))

	
	return render_template('closure/create.html' )
	


def configure(app):
	app.register_blueprint(closure)

