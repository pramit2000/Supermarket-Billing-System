 function addHtmlTableRow()
            {
               
                var table=document.getElementById("sales"),
                 newRow = table.insertRow(table.length),
                    cell1 = newRow.insertCell(0),
                    cell2 = newRow.insertCell(1),
                    p_name = document.getElementById("p-name").value,
                    p_price = document.getElementById("p-rice").value,
                    
            
                cell1.innerHTML = p_name;
                cell2.innerHTML = p_price;
                
                
            }
            