# Copyright (c) 2024, Asha Melius Kisonga and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


#class Librarymember(Document):
	#def before_save(self):
		#self.full_name = f'{self.first_name} {self.last_name or ""}'

class Librarymember(Document):
    def validate(self):
        # Handle cases where last_name might be empty or None
        self.full_name = f"{self.first_name.strip()} {self.last_name.strip() if self.last_name else ''}".strip()

 

