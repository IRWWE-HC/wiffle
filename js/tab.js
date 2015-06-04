$(document).keydown(function(stuff){
    var key = stuff.which;
    // Upon tab press, do this
    if(key == '9') {
       document.getElementById("form").innerHTML += "<textarea name='sB-text' id='sB-text' placeholder='Sidebar Names Here.  New Line for Each Name.'></textarea>"
    }
});
