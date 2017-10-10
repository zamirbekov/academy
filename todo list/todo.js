var new_task = document.getElementById("new_task");
var add = document.getElementById("add");
var list = document.getElementById("list");
var block = document.getElementById("block")

function add_new(){	
	var li = document.createElement('LI')
	var btn = document.createElement('BUTTON')
	var newCheckBox = document.createElement('input');
	newCheckBox.type = 'checkbox';
	newCheckBox.checked = false;
	var firstLi = list.getElementsByTagName('LI')[0]
	li.innerHTML = new_task.value
	btn.innerHTML = "Удалить"
	list.insertBefore(li, firstLi)
	list.insertBefore(btn, firstLi)
	list.insertBefore(newCheckBox, firstLi)
	new_task.value = ""
	btn.onclick = function(){
		list.removeChild(li, firstLi)
		this.parentNode.removeChild(btn)
		newCheckBox.parentNode.removeChild(newCheckBox)
	}
	newCheckBox.onclick = function(){
		if (this.checked == true){
    	li.setAttribute("class", "checked");}
    	else if (this.checked ==false){
    		li.setAttribute("class", "")
    	}
  }
}




