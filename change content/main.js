var a = document.getElementById("contact_us")
var c = document.getElementById("about_us")

function about_us(){
	a.setAttribute("class", "elem_hidden")
	c.setAttribute("class", "")
	document.getElementById("t").style.fontFamily = 'Exo 2, Charcoal,sans-serif'
}

function contact_us(x){
	c.setAttribute("class", "elem_hidden")
	a.setAttribute("class", "")
	c.style.fontFamily = 'Indie+Flower'
}