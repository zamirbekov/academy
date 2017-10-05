var display = document.getElementById("display"),
	key = document.getElementsByClassName("key");
for (var i = 0; i < key.length; i++) {
	var a = false;
    key[i].addEventListener('click', function () {
    	var key_value = this.getAttribute("key");
    	display.value += key_value;
    	if (key_value=="="){
    		display.value=(eval(display.value.slice(0, -1)))
    		a=true;
    	} else if (key_value=="+" || key_value=="*" || key_value=="/" || key_value=="-"){
			a=false;
		} else if (key_value=="C"){
    		display.value="";
    	} else if (key_value=="DEL"){
    		display.value=display.value.slice(0, -4);
    	} else if (a==true){
    		display.value="";
    		a = false; 
    		display.value=key_value;
		} else if (display.value.substr(-2)=="/0"){
			alert ("Нельзя делить на ноль!");
			display.value=display.value.slice(0, -1);
		} else if (display.value.length==12){
			
				if (key_value=="+" || key_value=="*" || key_value=="/" || key_value=="-"){
					var current_var = display.value.substr(-1);
					display.value=display.value+current_var;
				}
			display.value=display.value.slice(0, -1);
		} 		
})}
   