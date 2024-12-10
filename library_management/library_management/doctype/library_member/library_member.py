# Copyright (c) 2024, Asha Melius Kisonga and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Librarymember(Document):
	def before_save(self):
		self.Full_name = f'{self.First_name} {self.Last_name or ""}'
 

