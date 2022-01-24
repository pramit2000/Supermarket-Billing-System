 sum=0;
const list=[];
mytable=document.getElementById("table");

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
   let quant=1;
  // console.log(JSON.stringify(p_name));


   //console.log(JSON.stringify(p_name));
   if(p_name){
   Object.keys(p_name).forEach(element => {
    //console.log("Inside if", typeof p_name);
    //console.log("Data: ", p_name[element].dataset.product);
        if(buttons.dataset.product == p_name[element].dataset.product){
        //console.log("buttons.dataset.product"+ buttons.dataset.product, "p_name[element].dataset.product"+p_name[element].dataset.product);
        //console.log(p_name[element]);

        cell1.innerHTML = p_name[element].dataset.product;
        cell2.innerHTML= p_price[element].dataset.price;
        cell4.innerHTML=quant;
        price=p_price[element].dataset.price;
        list.push(parseFloat(Math.round(price)));
        console.log(list);
        }
       // if(buttons.dataset.price == p_price[element].dataset.price){
           
       // }
   });
   }
sum=(d3.sum(list));
document.getElementById("tt").value=sum+"₹";
console.log(sum);
  
    //cell1.innerHTML=p_name;

   


   // alert("added");
}
function exportCsv() {
    var csv = '';
    var rows = document.querySelectorAll("table tr");
    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++) 
            row.push(cols[j].innerText);
        csv += row.join(",") + "\r\n";
    }
    // Download CSV file
    this.downloadCSV(csv, "table.csv");
}