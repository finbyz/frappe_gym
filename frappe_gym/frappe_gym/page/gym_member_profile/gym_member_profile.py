import frappe

@frappe.whitelist()
def get_details(doctype,user,role):
    if user=="Administrator" or role:
       data=frappe.db.get_list(doctype,{},['full_name','plan','price','start_date','end_date','days_left','status','trainer'])
    else:
       data=frappe.db.get_list(doctype,{'email':user},['full_name','plan','price','start_date','end_date','days_left','status','trainer']) 
    return data