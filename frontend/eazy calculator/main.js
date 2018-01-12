  var op = document.getElementById('Operation');
  var one = document.getElementById('one');
  var two = document.getElementById('two');

  op.addEventListener('change', function() {

    var r = eval(one.value + op.value + two.value)
    if (op.value=="/" && two.value=="0"){
    	r="Нельзя делить на ноль!"
    }
    document.getElementById('result').value = r;

  }, false);

function nol(){
	var elem = document.getElementsByClassName("input")
	for (x in elem){
		elem[x].value=""
	}
	}	