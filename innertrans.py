#Open account
#import SOAPpy
from suds.client import Client
import random
import string
from suds.xsd.doctor import Import, ImportDoctor

url = 'http://innertrans.stable.alipay.net:8080/services/innerAccountManageFacade?wsdl'
client = Client(url, autoblend=True)

openCashAccountReq = client.factory.create('ns7:OpenCashAccountReq')
#OpenSettleAccountReq = client.factory.create('ns7:OpenSettleAccountReq')
#OpenTransitionAccountReq = client.factory.create('ns7:OpenTransitionAccountReq')

#closeAccountReq.accountNo = "20880000002111160156"
#closeAccountReq.lastModifyOperator = "yz"
#client.service.closeAccount(closeAccountReq)

#1¡¢cash account
openCashAccountReq.accountNo = "2088"+ string.join(random.sample('1234567890123456789012345678901234567890',12)).replace(" ","") +"0156"
openCashAccountReq.accountRange = "OUTER"
openCashAccountReq.aliasName=openCashAccountReq.accountNo
openCashAccountReq.allowOverDraftFlag = "TRUE"
openCashAccountReq.balanceDirection ="DEBIT"
openCashAccountReq.city ="SH"
openCashAccountReq.createOperator="yz"
openCashAccountReq.currency="156"
openCashAccountReq.entityAccountFlag="TRUE"
openCashAccountReq.instAccountDate="20081001"
openCashAccountReq.instAccountName="ICBC-BANK"
openCashAccountReq.instAccountNo="123123123"
openCashAccountReq.instId="ICBC"
openCashAccountReq.instProdType="NORMAL"
openCashAccountReq.instType="MANAGER"
openCashAccountReq.memo="add by python tool"
openCashAccountReq.overdraftQuota="Y"
openCashAccountReq.province="SH"
openCashAccountReq.reconInst="3009"
openCashAccountReq.subAccountType=" BANK_DEPOSIT"
openCashAccountReq.writeOffFlag="FALSE"

client.service.createCashAccount(openCashAccountReq)

#2¡¢settle account

#3¡¢shoule settle account
