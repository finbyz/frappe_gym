frappe.ui.form.on("Trainer", {
    
    full_name_concate:function(frm){
       frm.set_value("full_name", frm.doc.first_name +" "+frm.doc.last_name)
    },
   
    last_name:function(frm){
        frm.trigger('full_name_concate')
    }
});
