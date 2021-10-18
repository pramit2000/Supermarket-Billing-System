function add_item(event) {
   let table=document.getElementById("table");
   let tbody=document.getElementById("tbody");
   let row = tbody.insertRow(0);
   let cell1=row.insertCell(0);
   let cell2=row.insertCell(1);
   let cell4=row.insertCell(2);

   //let p_name=document.getElementById("p-name").innerHTML;
   const p_name=document.querySelectorAll("#p-name");
   const p_price=document.querySelectorAll("#p-price");
   const buttons = event.currentTarget;
  // console.log(JSON.stringify(p_name));
   if(p_name){
   Object.keys(p_name).forEach(element => {
    //console.log("Inside if", typeof p_name);
   // console.log("Data: ", p_name[element].dataset.product);
        if(buttons.dataset.product == p_name[element].dataset.product){
       // console.log("buttons.dataset.product"+ buttons.dataset.product, "p_name[element].dataset.product"+p_name[element].dataset.product);
      //  console.log(p_name[element]);
        cell1.innerHTML = p_name[element].dataset.product;
        }
        if(buttons.dataset.price == p_price[element].dataset.price){
            cell2.innerHTML= p_price[element].dataset.price;
        }
   });
   }
   //let p_price=document.getElementById("p-price").innerHTML;
   let quant=1;
    //cell1.innerHTML=p_name;

    cell4.innerHTML=quant;


   // alert("added");
}