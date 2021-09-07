# Copyright (c) 2021, dhinesh and contributors
#For license information, please see license.txt
import frappe
from frappe.model.document import Document

class payment(Document):
	def on_submit(self):
		if(self.pay_amount==self.amount):
			self.balance=0

		elif(self.pay_amount>self.amount):
			self.balance=self.pay_amount-self.amount
			frappe.msgprint("thanks here is your balance")
		else:
			frappe.throw("please pay the full amount")
		doc2=frappe.get_doc("student_main",self.student_name)
		
		text=" semester "+str(self.semester)+" paid"

		doc2.append("student_details",{"college_name":self.college_name,"student_branch":self.student_branch,"student_semester":self.semester,"student_status":text})
		doc2.save()