import app
import model
import math

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


report = Blueprint('report' , __name__ , url_prefix='/relatorios')





#usado para administrar os usuarios do sistema
@report.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	filters = request.args.get('search')
	page = request.args.get('page', 1, type=int)
	per_page = 10
	offset = (page - 1) * per_page

	
	data = model.list_report(filters, offset, per_page )
	
	count = model.count_report(filters, offset, per_page )

	count = math.ceil(count/ per_page)
	pagination =[
	filters,
	page,
	offset,
	per_page,
	count
	]
	
	pendentes =  model.list_closure_pending()

	return render_template('report/index.html' , 
		data=data , 
		pagination = pagination , 
		pending = pendentes)
	
	#return render_template('login.html' )



@report.route('/edit/<id>', methods = ['GET','POST'])
def edit(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	"""

	#buscar dados relatorios
	return render_template('report/edit.html'  )




@report.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	"""
	"""
	asd = model.create_report_pay_check(id)
	print(asd)
	if asd:
		relatorio = model.create_report_pay_auto(id)
		pendentes =  model.list_closure_pending(id)


		model.save_report(relatorio , pendentes)

	"""
	#esse é o ponto de ruptura
	#encontrar uma nova forma para o calculo
	#o antigo demora para calcular o pagamento

	data = model.list_report_id(id)


	return render_template('report/view.html' , data = data  , id=id)
	



def configure(app):
	app.register_blueprint(report)

