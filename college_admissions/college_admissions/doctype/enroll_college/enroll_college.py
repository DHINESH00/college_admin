# Copyright (c) 2021, dhinesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class enroll_college(Document):
	def on_submit(self):
		self.append("semesters",{"semester_1_fees":11000,"semester_2_fees":12000,"semester_3_fees":13000,"semester_4_fees":14000,"semester_5_fees":15000,"semester_6_fees":16000,"semester_7_fees":17000,"semester_8_fees":20000})
		doc1=frappe.new_doc("payment")
		doc1.college_name= self.college_name
		doc1.student_name= self.student_name
		doc1.student_branch= self.branch
		doc1.semester=1
		doc1.amount= 11000
		doc1.save()