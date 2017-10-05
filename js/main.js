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

var i;
var a = ["apple", "facebook", "twitter"]
var b = ["apple.com", "facebook.com", "twitter.com"]
var h = "http://"
var displayloop="";
i=0;
while (i<3){
    displayloop += "<h1>This is <b><a href='"+h+b[i]+"' target='_blank'>"+a[i] + "</a></b></h1> <BR>";
    i++;
}
document.getElementById("p1").innerHTML = displayloop;