function add_item() {
   let table=document.getElementById("table");
   let tbody=document.getElementById("tbody");
   let row = tbody.insertRow(0);
   let cell1=row.insertCell(0);
   let cell2=row.insertCell(1);
   let cell4=row.insertCell(2);

   let p_name=document.getElementById("p-name").innerHTML;
   let p_price=document.getElementById("p-price").innerHTML;
   let quant=1;
    cell1.innerHTML=p_name;
    cell2.innerHTML=p_price;
    cell4.innerHTML=quant;
   

    alert("added");
}