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
	displayloop = displayloop+ a[x]+"<br>"+"ksdkf `hello ${x}`";
}

document.getElementById("p1").innerHTML = displayloop;