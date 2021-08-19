var menu_btn = document.querySelector("#menu-toggle");
var sidebar = document.querySelector(".sidebar-wrapper");
var content = document.querySelector(".page-content-wrapper");

menu_btn.addEventListener("click", ()=>{
    sidebar.classList.toggle("hide-nav")
    content.classList.toggle("expand-cont")
});