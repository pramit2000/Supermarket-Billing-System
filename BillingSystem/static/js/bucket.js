function test() {
   let table=document.getElementById("table");
   let row = table.insertRow(1);
   let cell1=row.insertCell(0);
   let cell2=row.insertCell(1);
   let p_name=document.getElementById("p-name").innerHTML;
   let p_price=document.getElementById("p-price").innerHTML;
    cell1.innerHTML=p_name;
    cell2.innerHTML=p_price;
    alert("added");
}