function test() {
   let table=document.getElementById("table");
   let tbody=document.getElementById("tbody")
   let row = tbody.insertRow(1);
   let cell1=row.insertCell(0);
   let cell2=row.insertCell(1);
   let cell3=document.getElementById("quantity").innerHTML;
   let cell4=cell3.insertCell(2);
   let p_name=document.getElementById("p-name").innerHTML;
   let p_price=document.getElementById("p-price").innerHTML;
   let quant=
    cell1.innerHTML=p_name;
    cell2.innerHTML=p_price;
    cell4.innerHTML=1;


    alert("added");
}