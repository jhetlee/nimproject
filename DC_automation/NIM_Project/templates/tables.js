
var items = document.getElementById("item")
var table = document.getElementById("myTable");
var row;

for(var i = 0; i < items.length; i++){
  if(i % 3 == 0) {   //after every third cell add a new row and change the row variable to point to it
     row = table.insertRow(-1);
  }
  var cell = row.insertCell(-1);  //simply insert the row
  cell.innerHTML = items[i];
}