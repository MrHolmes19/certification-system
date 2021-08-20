/* navbar adptations*/

var current_url = window.location.href;
var back_link = document.querySelector(".back-button");
var sidebar_toggler = document.querySelector(".navbar-toggler-icon");
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