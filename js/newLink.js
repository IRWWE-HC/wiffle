//Following function courtesy of https://css-tricks.com/dangers-stopping-event-propagation/

$(document).on('click', function(event) {
  if (!$(event.target).closest('#title').length) {
    alert($('input#title').val())
  }
});

$(document).ready(function(){
	var ctr = 0
	$(document).keydown(function(press){
		var key = press.which;
		var frm = document.getElementById("insertInput");
		var txtText = document.createElement("input"); 
		var txtLink = document.createElement("input");
		// Upon alt press, do this
		if(key == '18') {
			ctr += 1
			txtText.type = "text";
			txtText.name = "sB-text" + ctr;
			txtText.id = "sB-text";
			txtText.className = "s1";
			txtText.placeholder = "Sidebar Names Here.";
			frm.appendChild(txtText);
			txtLink.type = "text";
			txtLink.name = "sB-link" + ctr;
			txtLink.id = "sB-link";
			txtLink.className = "s1";
			txtLink.placeholder = "Sidebar Links Here.";
			frm.appendChild(txtLink);
			frm.appendChild(document.createElement("br"))
		}
	})});
