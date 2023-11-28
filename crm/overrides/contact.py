# import frappe
from frappe import _
from frappe.contacts.doctype.contact.contact import Contact


class CustomContact(Contact):
	@staticmethod
	def sort_options():
		return [
			{ "label": 'Created', "value": 'creation' },
			{ "label": 'Modified', "value": 'modified' },
			{ "label": 'Organization', "value": 'company_name' },
			{ "label": 'Full Name', "value": 'full_name' },
			{ "label": 'First Name', "value": 'first_name' },
			{ "label": 'Last Name', "value": 'last_name' },
			{ "label": 'Email', "value": 'email' },
			{ "label": 'Mobile no', "value": 'mobile_no' },
		]

	@staticmethod
	def default_list_data():
		columns = [
			{
				'label': 'Name',
				'type': 'Data',
				'key': 'full_name',
				'width': '17rem',
			},
			{
				'label': 'Email',
				'type': 'Data',
				'key': 'email_id',
				'width': '12rem',
			},
			{
				'label': 'Phone',
				'type': 'Data',
				'key': 'mobile_no',
				'width': '12rem',
			},
			{
				'label': 'Organization',
				'type': 'Data',
				'key': 'company_name',
				'width': '12rem',
			},
			{
				'label': 'Last modified',
				'type': 'Datetime',
				'key': 'modified',
				'width': '8rem',
			},
		]
		rows = [
			"name",
			"full_name",
			"company_name",
			"email_id",
			"mobile_no",
			"modified",
			"image",
		]
		return {'columns': columns, 'rows': rows}
