import app
import model
import math

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


quote = Blueprint('quote' , __name__ , url_prefix='/cotas')





#usado para administrar os usuarios do sistema
@quote.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""


	filters = request.args.get('search')
	page = request.args.get('page', 1, type=int)
	per_page = 10
	offset = (page - 1) * per_page

	
	data = model.list_quote_all(filters, offset, per_page )
	
	count = model.count_quote(filters, offset, per_page )

	count = math.ceil(count/ per_page)
	pagination =[
	filters,
	page,
	offset,
	per_page,
	count
	]
	
	return render_template('quote/index.html' , data=data , pagination = pagination)
	#return render_template('login.html' )

@quote.route('/create', methods = ['GET','POST'])
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

	
	return render_template('quote/create.html' )
	


def configure(app):
	app.register_blueprint(quote)

