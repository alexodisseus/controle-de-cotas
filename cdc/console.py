print("ola")
import model

asd = model.populqte()
"""
a = model.Quota()
a.id=1
a.code=123
a.status="A"
a.date="12/12/2023"
a.old=321
a.grouping=2
a.user_id=2

model.save(a)
"""


for x in asd:
    asdf = model.titi(x.code)
    for y in asdf:
        a = model.Quota()
        a.code=y.numero
        a.status=y.situacao
        a.date=y.data_aquis
        if y.cotista2:
            a.old=y.cotista2
        else:
            a.old = 0000
                
        a.grouping=y.cotas
        a.user_id=x.id
        print(a)

        model.save(a)
        
        

"""
id=773 
data_aquis='1/10/1987' 
numero='B002679' 
cotista2='056340' 
situacao='A' 
mes_transf=7 
cotista=84782 
ano_transf=2014 
cotas=2
"""