//Following function courtesy of https://css-tricks.com/dangers-stopping-event-propagation/

$(document).ready(function(){
	var ctr = 0
	idValTemp = -1
	
	/*
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
	})
	*/
	
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
					newChild.id = "m-textOutput";
					newChild.className = "s1";
					parent.appendChild(newChild);
	  }}}
	});
	*/
	
	
	//HOMEPAGE JS
	
	//Prevents any modal boxes or transitions to pop up before page load
	$("div").removeClass("preload");
	
	//Slides down navBar ONLY in the homepage
	$('#HP.navBar').slideDown(400);
	
	//The welcome text fade in
	$('#headingHP').fadeIn(2000);
	$('#headingHP').delay(1000).fadeOut(function() {
		$('#headingHP').text('Please Login or Create an Account to Proceed');
		$('#headingHP').css('font-size', '3em');
	}).fadeIn(2000); //Not sure if this is proper syntax, cause it looks weird. But it works.... 
	
	//Sign up fade in
	$('.signUp').fadeIn(2000);
	
	//Sign in open and close
	$('#signInOpen').click(function(){
		$('.signIn').fadeIn(500);
	});
	$('#signInClose').click(function(){
		$('.signIn').fadeOut(500);
	});
	
	//EDITING SITE JS
	//Selection menu code
	$('#optionCarousel').hover(function(){
		$('.optionButton').slideToggle();
	});
	
	$('#optionTitleAdd').click(function(){
		$('#headingDisplay').fadeIn(100);
		$(this).attr('id', 'optionTitleSub');
	});
	$('#optionMTAdd').click(function(){
		$('#m-textOutput').fadeIn(100);
		$(this).attr('id', 'optionMTSub');
	});
	$('#optionSBAdd').click(function(){
		$('#insertSB').fadeIn(100);
		$(this).attr('id', 'optionSBSub');
	});
	
	/* Removes elements if selected
	$('#optionList').on('click', (function(e){
		if ($(this).text() === '+') {
			alert('chicken');
			$(this).text('-');
		} else if ($(this).text() === '-') {
			$(this).text('+');
		}
	}));
	*/
	
	//Element Editing Code
	
	//Sidebar Code
	$('#sB-nameDisplay').click(function(){
		$('#sB-name').fadeIn();
	});
	$('.outside').click(function(){
		var newText = $('#sB-name > input').val();
		if (newText.length != 0) {
			$('#sB-nameDisplay').text(newText);
		}
		$('#sB-name').fadeOut();
	});
	
	$('#addSidebarInstruction').click(function(){
		ctr += 1
		
		var sBInput = document.getElementById("sBInput");
		
		var newChildInput = document.createElement('div');
		newChildInput.id = "val" + ctr;
		newChildInput.className = "sBInputVal";
		
		var outsideChild = document.createElement('div');
		outsideChild.className = "outside";
		outsideChild.id = "sBInputOutside";
		
		var textChild = document.createElement('input');
		textChild.type = "text";
		textChild.name = "sB-text" + ctr;
		textChild.id = "sB-text";
		textChild.className = "s1";
		textChild.placeholder = "Text.";
		
		var linkChild = document.createElement('input');
		linkChild.type = "text";
		linkChild.name = "sB-link" + ctr;
		linkChild.id = "sB-link";
		linkChild.className = "s1";
		linkChild.placeholder = "Link";
		
		newChildInput.appendChild(outsideChild);
		newChildInput.appendChild(textChild);
		newChildInput.appendChild(linkChild);
		
		sBInput.appendChild(newChildInput);
		
		
		var instruc = document.getElementById("sBInputInstruction");
		
		var newChildHeading = document.createElement('h1');
		var headingText = document.createTextNode('Click to Add New Sidebar Link')
		newChildHeading.id = "instruction" + ctr;
		newChildHeading.appendChild(headingText);
		
		instruc.appendChild(newChildHeading);
		
	});
	
	$(document).on('click', '#sBInputInstruction', function(clicked){
		var idVal = $(clicked.target).attr('id');
		idValTemp = idVal;
		var lastVal = idVal[idVal.length -1];
		var preVal = '#val';
		var callVal = preVal.concat(lastVal);
		$(callVal).fadeIn();
	});
	$(document).on('click', '#sBInputOutside', function(){
		idVal = idValTemp;
		var lastVal = idVal[idVal.length -1];
		var textLast = '[name="sB-text' + lastVal + '"]';
		var linkLast = '[name="sB-link' + lastVal + '"]';
		var textLength = $(textLast).val();
		var linkLength = $(linkLast).val();
		var preVal = '#val';
		var callVal = preVal.concat(lastVal);
		var preValInstruc = '#instruction'
		var callValInstruc = preValInstruc.concat(lastVal);
		if (textLength.length != 0 && linkLength !=0) {
			$(callValInstruc).text(textLength);
		}
		$(callVal).fadeOut();
		idValTemp = -1;
	});
	
	/*
	$('#addSidebarLink').click(function(){
		var parent = document.getElementById("sBInputInstruction");
		var appendVal = document.createElement("h1"); 
		appenddVal = document.createElement("input");
	*/
	// Main Text Code
	$('#m-textOutput').click(function(){
		$('#m-text').fadeIn();
	});
	$('#m-textOutside.outside').click(function(){
		var dataOutput = document.getElementById('m-textOutput');
		var paraNode = document.getElementById('removePlease')
		var textData = $('#m-textInput').val();
		var text = document.createTextNode(textData);
		var preTag = document.createElement('pre');
		preTag.appendChild(text);
		if (textData.length != 0) {
			if (paraNode) {
				dataOutput.removeChild(paraNode);
			}
			dataOutput.appendChild(preTag);
		}
		$('#m-text').fadeOut();
	});
	
	$('#headingDisplay').click(function(){
		$('#headingDIV').fadeIn();
	});
	$('#outsideHeading.outside').click(function(){
		var textLength = $('#heading').val();
		if (textLength.length != 0) {
			$('#headingDisplay').text(textLength);
		}
		$('#headingDIV').fadeOut();
	});
	
	//Submit Button with Empty Fields
	$(document).on('blur', '.sBInputVal input', function(){
		$('.sBInputVal input').each(function() {
			if ($(this).val().length == 0) {
				alert('Please Fill Out Both Fields'); //make into modal
			}
		})
	});
});


