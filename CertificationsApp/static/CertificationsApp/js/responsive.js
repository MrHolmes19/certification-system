
const d = document
const w = window

/*
if(window.location.pathname.includes("formulario")){
    let breakpoint = w.matchMedia('(max-width: 767px)')
    console.log(breakpoint)
    const $select = document.querySelectorAll("select")
    
    const responsive= (e) =>{
        if(e.matches){
            $select[0].classList.add('w-100')
            $select[1].classList.add('w-100')
        } else {
            $select[0].classList.remove('w-100')
            $select[1].classList.remove('w-100')
        }
    }


    breakpoint.addEventListener('change', responsive)
    responsive(breakpoint)    
}
*/


if(w.location.pathname.includes("administrador") && !w.location.pathname.includes("detalle")){
    let breakpoint = w.matchMedia('(max-width: 360px)')
    const $sidebar = d.querySelector(".sidebar-wrapper")
    const $pageContent = d.querySelector(".page-content-wrapper")
    
    const responsive2= (e) =>{
        if(e.matches){
            $sidebar.classList.add('hide-nav')
            $pageContent.classList.add('expand-cont')
            
            //$sidebar.style.transition = "0s"
            //$pageContent.style.transition = "0s"

            //d.documentElement.style.setProperty('--shift-nav', '100vw')

        } else {
            $sidebar.classList.remove('hide-nav')
            $pageContent.classList.remove('expand-cont')
            //$pageContent.style.transition = "0.5s"
            //$pageContent.style.transition = "0.5s"

            //d.documentElement.style.setProperty('--shift-nav', '250px')
        }
    }

    breakpoint.addEventListener('change', responsive2)
    responsive2(breakpoint)
}