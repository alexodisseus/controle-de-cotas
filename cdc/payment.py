import app
import model
import math

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for



payment = Blueprint('payment' , __name__ , url_prefix='/pagamentos')





#usado para administrar os pagamentos
"""
@payment.route('/', methods = ['GET','POST'])
def index():
	
	#if 'username' not in session:
	#	return redirect(url_for('admin.login'))

	

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


"""


@payment.route('/', methods = ['GET','POST'])
def index():
	# carregar todos os filtros
	# listar todos os pendentes
	# filtrar conforme necessario
	# separar os pagamentos selecionados para concluir

	dtribute=model.tribute_last()
	
	data = model.list_payment_filters(1)
	
	return render_template('payment/index.html',data=data ,  dtribute=dtribute , tribute = tribute_rules)


@payment.route('/ajax/', methods = ['GET'])
def ajax():
	# carregar todos os filtros
	# listar todos os pendentes
	# filtrar conforme necessario
	# separar os pagamentos selecionados para concluir


	page = int(request.args.get('page', 1))

    # Obtenha os dados da página atual
	payment_data = model.list_payment_filters(page) 
	
	if payment_data:
		return render_template('payment/ajax.html',data=payment_data)
	else:
		return "asd"
	


def tribute_rules(data, tribute):
    alicota = 0
    
    if data < float(tribute.isento):
        data =  "{:.2f}".format(round(data,2))
        return data
    
    if data < float(tribute.faixa1):
    	data = data - (data*7.5/100) +  142.80
    	data =  "{:.2f}".format(round(data,2))
    	return data

    if data < float(tribute.faixa2):
    	data = data - (data*15/100) + 354.80
    	data =  "{:.2f}".format(round(data,2))
    	return data

    if data < float(tribute.faixa3):
    	data = data - (data*22.5/100) + 636.13
    	data =  "{:.2f}".format(round(data,2))
    	return data

    data = data - (data*27.5/100) + 869.36
    data =  "{:.2f}".format(round(data,2))
    return data
    

@payment.route('/edit/<id>', methods = ['GET','POST'])
def edit(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	"""
	
	bank = request.args.get('bank', None)

	fechamento = model.get_closure(id)
	
	dtribute=model.tribute_last()
	if fechamento.type == 'comum':

		data = model.list_report_comum(id , bank)
	else:
		data = model.list_report_full(id , bank)

	return render_template('report/edit.html' ,data=data , fechamento = fechamento , tribute = tribute_rules, dtribute=dtribute)



"""
@payment.route('/print/', methods = ['GET','POST'])
def print():
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	
	data = request.args.get('')

		
	return render_template('report/print.html' ,data=data )

"""	
	




@payment.route('/view/<id>', methods = ['GET','POST'])
async def view(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	"""

	asd = model.create_report_pay_check(id)

	if asd:
		relatorio = model.create_report_pay_auto(id)
		pendentes =  model.list_closure_pending(id)


		model.save_report(relatorio , pendentes)

	
	data = model.list_report_resume_id(id)
	fechamento = model.get_closure(id)


	return render_template('report/view.html' , data = data  , fechamento = fechamento)
	



def configure(app):
	app.register_blueprint(payment)
