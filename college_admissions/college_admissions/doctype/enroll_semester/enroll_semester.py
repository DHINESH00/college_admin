# Copyright (c) 2021, dhinesh and contributors
# For license information, please see license.txt
#!/usr/bin/python -tt

import frappe
from frappe.model.document import Document

class enroll_semester(Document):
	def on_submit(self):
		student_exist=frappe.db.get_value("student_details",{"college_name":self.college_name,"parent":self.student_name},"student_semester")
		if student_exist:
			self.branch=frappe.db.get_value("student_details",{"college_name":self.college_name,"parent":self.student_name},"student_branch")
			student_exist=int(student_exist)+1
			self.semester=student_exist
			if student_exist == 2:
				self.coures_1="Mathematics-2"
				self.coures_2="C-programing"
				self.semester_fee=12000
			elif student_exist == 3:
				self.coures_1="Mathematics-3"
				self.coures_2="BEEE"
				self.semester_fee=13000
			elif student_exist == 4:
				self.coures_1="Mathematics-4"
				self.coures_2="Thermodynamics"
				self.semester_fee=14000
			elif student_exist== 5:
				self.coures_1="material engineering"
				self.coures_2="OOPS"
				self.semester_fee=15000
			elif student_exist == 6:
				self.coures_1="material engineering-2"
				self.coures_2="Data structure"
				self.semester_fee=16000
			elif student_exist == 7:
				self.coures_1="Engineering physics-2"
				self.coures_2="DAA"
				self.semester_fee=17000
			else:
				self.coures_1="ECE"
				self.coures_2="project"
				self.semester_fee=20000
			doc1=frappe.new_doc("payment")
			doc1.college_name= self.college_name
			doc1.student_name= self.student_name
			doc1.student_branch= self.branch
			doc1.semester=student_exist
			doc1.amount= self.semester_fee
			doc1.save()
		else:
			frappe.throw("invalid student name or college name")
		
