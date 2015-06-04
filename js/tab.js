$(document).keydown(function(press){
    var key = press.which;
	var frm = document.getElementById("form");
	var txtText = document.createElement("textarea"); 
	var txtLink = document.createElement("textarea");
    // Upon tab press, do this
    if(key == '9') {
		txtText.name = "sB-text";
		txtText.id = "sB-text";
		txtText.placeholder = "Sidebar Names Here.  New Line for Each Name.";
		frm.appendChild(txtText);
		txtLink.name = "sB-link";
		txtLink.id = "sB-link";
		txtLink.placeholder = "Sidebar Links Here.  New line for each Link. Links should correspond";
		frm.appendChild(txtLink);
		frm.appendChild(document.createElement("br"))
    }
});
