// var number = prompt("Kakuyu osenku puluchil?");
// switch (number) {
//   case "2":
//     alert( "Ploho" );
//     break;
//   case "3":
//     alert( "Udovletvoritelno" );
//     break;
//   case "4":
//     alert( "Xorowo" );
//     break;
// case "5":
//     alert( "Otlichno" );
//     break;
//   default:
//     alert( "Error" );
// }
displayloop="";
var a = ["apple", "facebook", "twitter"]
for (x in a){
	displayloop = displayloop+`<a href="http://${a[x]}.com" target="_blank"><b>${a[x]}</b></a><br>`;
}

document.getElementById("p1").innerHTML = displayloop;

function getName(){
	var name = "Hello world!";
	alert(name+displayloop);
}

getName()

function second(b) {
	alert(b);
}

second("This is second function with argument")

function third(a,b,c){
	var x=a+b+c;
	return x;
}

alert(third(1,2,3));

