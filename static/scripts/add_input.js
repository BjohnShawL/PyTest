function add() {
    var container = document.getElementById("failForm");
   	var para= document.createElement("p");
    var lab = document.createElement("label");
    lab.innerText="Failure Id";
    var inp =document.createElement("input");
    inp.type="text";
    inp.name="_failureId";
    var button = document.getElementById("submitBtn")
        
    para.appendChild(lab);
    para.appendChild(inp);
        
    container.insertBefore(para,button);


}
