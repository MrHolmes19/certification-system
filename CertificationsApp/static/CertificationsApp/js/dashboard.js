/* navbar adaptations*/

var current_url = window.location.href;
var back_link = document.querySelector(".back-button");
var sidebar_toggler = document.querySelector("#menu-toggle");
var title = document.querySelector("#topnav .navbar-brand");

if(current_url.indexOf("/administrador/detalle") > 0){
    sidebar_toggler.classList.toggle("visually-hidden");
    back_link.classList.toggle("visually-hidden");
    title.innerHTML ="Detalle de la operacion";
};

/* sidebar effect */

var menu_btn = document.querySelector("#menu-toggle");
var sidebar = document.querySelector(".sidebar-wrapper");
var content = document.querySelector(".page-content-wrapper");
var fonts = document.querySelector(".body");

menu_btn.addEventListener("click", ()=>{
    sidebar.classList.toggle("hide-nav")
    content.classList.toggle("expand-cont")
    fonts.classList.toggle("expand-font")
});

/* search bar selects*/

/*
var sel1 = document.querySelector('#select1');
var sel2 = document.querySelector('#select2');
var options2 = sel2.querySelectorAll('option');

function giveSelection(selValue) {
  sel2.innerHTML = '';
  for(var i = 0; i < options2.length; i++) {
    if(options2[i].dataset.option === selValue) {
      sel2.appendChild(options2[i]);
    }
  }
}

giveSelection(sel1.value);
*/

/* real-time searching */

var search_field = document.querySelector("#search-field"); //Borrar, no se usa
var current_table = "operations";

function currentTable(actual){
  current_table = actual;
}

function search(value){
  var rows =  document.querySelectorAll("tbody tr");
  //rows.classList.add("visually-hidden");
  
  rows.forEach(row => {
    row.classList.add("visually-hidden");
    cols = Array.from(row.getElementsByTagName("td"));
    cols.forEach(col => {
        if(col.innerText.toLowerCase().indexOf(value.toLowerCase()) > -1){
          col.parentElement.classList.remove("visually-hidden");
      }
    });
  });
}

