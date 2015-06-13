//Following function courtesy of https://css-tricks.com/dangers-stopping-event-propagation/

$(document).ready(function(){
	/*
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
	})
	*/
	
	//Prevents any modal boxes or transitions to pop up before page load
	$("div").removeClass("preload");
	
	//Slides down navBar ONLY in the homepage
	$('#HP.navBar').slideDown(400);
	
	//
	$('#headingHP').fadeIn(2000);
	$('#headingHP').delay(1000).fadeOut(function() {
		$('#headingHP').text('Please Login or Create an Account to Proceed');
		$('#headingHP').css('font-size', '3em');
	}).fadeIn(2000); //Not sure if this is proper syntax, cause it looks weird. But it works.... 
	
	$('.signUp').fadeIn(2000);
	
	$('#signInOpen').click(function(){
		$('.signIn').fadeIn(500);
	});
	
	$('#signInClose').click(function(){
		$('.signIn').fadeOut(500);
	});
	
});


