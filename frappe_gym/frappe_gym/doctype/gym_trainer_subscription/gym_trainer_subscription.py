# Copyright (c) 2022, Warren Eiserman and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymTrainerSubscription(WebsiteGenerator):
	# set the route for the workout plan
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
