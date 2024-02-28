document.addEventListener("DOMContentLoaded", (e) => {
    AOS.init();
    
    let navbar = document.querySelector('.header__principal')  
    let currentURL = window.location.pathname;



    if(currentURL == '/'){
        window.addEventListener("scroll", () =>{
            let scroll = window.scrollY
            if(scroll > 700 ){
                navbar.classList.add("background__opacity");
            }else{
                navbar.classList.remove("background__opacity");
            }
        })
    }else{
        window.addEventListener("scroll", () =>{
            let scroll = window.scrollY
            if(scroll > 100 ){
                navbar.classList.add("background__opacity");
            }else{
                navbar.classList.remove("background__opacity");
            }
        })
    }




})


