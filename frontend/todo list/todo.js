var new_task = document.getElementById("new_task");
var add = document.getElementById("add");
var list = document.getElementById("list");
var block = document.getElementById("block")

function add_new(){	
	var li = document.createElement('LI')
	var btn = document.createElement('SPAN')
	var check = document.createElement('input');
	check.type = 'checkbox';
	check.checked = false;
	var firstLi = list.getElementsByTagName('LI')[0]
	li.innerHTML = new_task.value
	btn.innerHTML = "X"
	list.insertBefore(li, firstLi)
	li.appendChild(btn)
	li.appendChild(check)
	new_task.value = ""
	btn.onclick = function(){
		list.removeChild(li, firstLi)
		this.parentNode.removeChild(btn)
		check.parentNode.removeChild(check)
	}
	check.onclick = function(){
		if (this.checked == true){
    	li.setAttribute("class", "checked");}
    	else if (this.checked ==false){
    		li.setAttribute("class", "")
    	}
  }
}




