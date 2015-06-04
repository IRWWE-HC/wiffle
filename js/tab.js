//function tabFunc() {
//	if(

$(document).ready(function(){
	$(document).keydown(function(press){
		var key = press.which;
		var frm = document.getElementById("insertInput");
		var txtText = document.createElement("input"); 
		var txtLink = document.createElement("input");
		// Upon tab press, do this
		if(key == '17') {
			txtText.type = "text";
			txtText.name = "sB-text";
			txtText.id = "sB-text";
			txtText.className = "sB";
			txtText.placeholder = "Sidebar Names Here.";
			frm.appendChild(txtText);
			txtLink.type = "text";
			txtLink.name = "sB-link";
			txtLink.id = "sB-link";
			txtLink.className = "sB";
			txtLink.placeholder = "Sidebar Links Here.";
			frm.appendChild(txtLink);
			frm.appendChild(document.createElement("br"))
		}
	})});
