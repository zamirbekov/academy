//Программа калькулятор работает на основе строкового типа данных
//Нужно доработать некоторые исключения, улучшить стиль

var display = document.getElementById("display"), //экран
	key = document.getElementsByClassName("key"); //все кнопки собираем в типа массив
for (var i = 0; i < key.length; i++) { //обработка кнопок, чтобы каждую кнопку получить по отдельности
	var a = false; //этот флажок установлен, чтобы обнулять экран, после ввода новой цифры за выводом результата
    key[i].addEventListener('click', function () { 
    	var key_value = this.getAttribute("key"); //получаем значение кнопок по атрибутам 
    	display.value += key_value; //и сразу выводим на экран, добавляя к предыдущему значению
    	if (key_value=="="){
    		display.value=(eval(display.value.slice(0, -1))) //eval делает всю ариф. операцию, он тут правит всеми - хозяин и господин
    		a=true; //после вывода результата меняем флажок, чтобы в будущем применить при обнулении
    	} else if (key_value=="+" || key_value=="*" || key_value=="/" || key_value=="-"){
			a=false; //если арифм.операции флажок не меняем
		} else if (key_value=="C"){ //росто обнуляет все 
    		display.value="";
    	} else if (key_value=="DEL"){ //это бэкспейс, удаляет по одному символу при нажатии
    		display.value=display.value.slice(0, -4); //-4 это с учетом 3 символов от DEL и 1 от строки экрана
    	} else if (a==true){ //тут происходит обнуление
    		display.value=""; 
    		a = false; //здесь же меняем флажок, чтобы он вечно не обнулял
    		display.value=key_value; //сразу же пишем то, что польз. ввел после вывода результата
		} else if (display.value.substr(-2)=="/0"){ //при делении на ноль ловим последние 2 символы: "/0"
			alert ("Нельзя делить на ноль!"); //а при нажатии на ноль сразу вызываем сообщение, мол "ты где учился вообще?"
			display.value=display.value.slice(0, -1); //это чтобы, после сообщения ноль не появлялся на экране
		} else if (display.value.length==12){ //если число достигает 12
				if (key_value=="+" || key_value=="*" || key_value=="/" || key_value=="-"){ //чтобы мог делать операции при 12 симв.
					var current_var = display.value.substr(-1); //чтобы запомнил арифм.символ
					display.value=display.value+current_var; //и добавил в конце строки
				}
			display.value=display.value.slice(0, -1); //после 12 симв.ничего кроме ариф. симв. не печатается
		} 		
})}
   