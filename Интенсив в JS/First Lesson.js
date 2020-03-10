

let skills =["JS","R","C#"]

for(let i=0;i<skills.length;i++)
    document.write("Я владею "+skills[i]+"<br>");

let age = prompt("Возраст?");
if(age<18) alert("Меньше 18!");
else alert("Сойдёт");


let square = function(x) {console.log(x*x)};
