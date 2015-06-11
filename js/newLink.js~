//Following function courtesy of https://css-tricks.com/dangers-stopping-event-propagation/

/*
function getInputValue() {
	var inputValue = $('input#heading').val();
	return inputValue;
}

function getTextareaValue() {
	var splitLines = $('textarea#m-text').val().split('/\n/');
	var textareaValue = document.createElement('div');
	textareaValue.appendChild(document.createTextNode(splitLines[0]));
	var brVal = document.createElement('br');
	textareaValue.appendChild(brVal);
	for (var i=1; i < splitLines.length; i++) {
		textareaValue.appendChild(document.createTextNode(splitLines[i]));
		textareaValue.appendChild(brVal);
	}
	return textareaValue;
}

//Make the following part more modular

$(document).on('click', function(event) {
	if (document.getElementById('heading')) {
		if (getInputValue() != '') {
			if (!$(event.target).closest('#heading').length) {
				var textValue = document.createTextNode(getInputValue());
				console.log(textValue);	
				var parent = document.getElementById('titleCenter');
				var oldChild = document.getElementById("heading");
				parent.removeChild(oldChild);
				var newChild = document.createElement("span");
				newChild.id = "headingText";
				newChild.className = "s1";
				newChild.appendChild(textValue);
				parent.appendChild(newChild);
  }}}
});

$(document).on('click', function(event) {
	if (document.getElementById('m-text')) {
		if ($('textarea#m-text').val().length != 0) {
			if (!$(event.target).closest('#m-text').length) {
				var parent = document.getElementById('formId');
				var oldChild = document.getElementById("m-text");
				parent.removeChild(oldChild);
				var newChild = getTextareaValue();
				newChild.id = "m-textText";
				newChild.className = "s1";
				parent.appendChild(newChild);
  }}}
});
*/

$(document).ready(function(){
	var ctr = 0
	$(document).keydown(function(press){
		var key = press.which;
		var frm = document.getElementById("insertSB");
		var txtText = document.createElement("input"); 
		var txtLink = document.createElement("input");
		// Upon alt press, do this
		if(key == '18') {
			ctr += 1
			txtText.type = "text";
			txtText.name = "sB-text" + ctr;
			txtText.id = "sB-text";
			txtText.className = "s1";
			txtText.placeholder = "Sidebar Text Here.";
			frm.appendChild(txtText);
			txtLink.type = "text";
			txtLink.name = "sB-link" + ctr;
			txtLink.id = "sB-link";
			txtLink.className = "s1";
			txtLink.placeholder = "Sidebar Link Here.";
			frm.appendChild(txtLink);
			frm.appendChild(document.createElement("br"))
		}
	})});
