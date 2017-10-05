// вывод свойства обьекта
var object = {
	prop:43,
	f1:function(){
		return (this.prop);
	}
}

console.log(object.f1()) 

//наследование
var object={
f2:function(){
	return this.a+this.b}
}
var instance=Object.create(object);
instance.a=15;
instance.b=5;
console.log(instance.f2());

//call вызывает аргументы как this
function add(c,d){
	return this.a+this.b+c+d;
}
var object={
	a:1,
	b:2
}
console.log(add.call(object,3,4))

//apply-массивом
console.log(add.apply(object,[3,4]))