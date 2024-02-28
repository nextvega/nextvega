document.addEventListener("DOMContentLoaded", (e) => {

    const items = document.querySelectorAll(".code__editor__principal__main__skills__item-backgroundMove");

    items.forEach(item => {
        item.addEventListener("mouseenter", function() {
            item.classList.add("active");
        });

        item.addEventListener("mouseleave", function() {
            item.classList.remove("active");
        });
    });

    document.addEventListener("mousemove", function(e) {
        const mouseX = e.clientX;
        const mouseY = e.clientY;

        items.forEach(item => {
            if (item.classList.contains("active")) {
                const itemRect = item.getBoundingClientRect();
                const itemCenterX = itemRect.left + itemRect.width / 2;
                const itemCenterY = itemRect.top + itemRect.height / 2;
                const distance = Math.sqrt(Math.pow(mouseX - itemCenterX, 2) + Math.pow(mouseY - itemCenterY, 2));

                const maxDistance = Math.sqrt(Math.pow(itemRect.width / 2, 2) + Math.pow(itemRect.height / 2, 2));

                const gradientStrength = (1 - (distance / maxDistance)) * 110; // Adjust as needed
                item.style.background = `radial-gradient(circle at ${mouseX}px ${mouseY}px, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.1) ${gradientStrength}%)`;
            } else {
                item.style.background = "";
            }
        });
    });


    const headerBackground = document.querySelector(".header__principal")
    const menuMobile = document.querySelector(".menu-mobile__close");
    const navMobile = document.querySelector(".header__principal__nav__list");
    const descripcion = document.querySelector(".main__principal__text__description__menu");
    const body = document.querySelector('body')

    

    menuMobile.addEventListener("click", handleMobileMenuClick);

    // Lógica para manejar el clic en el menú móvil
    function handleMobileMenuClick() {
        if (!navMobile.classList.contains("header__principal__nav__list__mobile")) {
            // Si el menú no está abierto, ábrelo
            navMobile.classList.add("header__principal__nav__list__mobile");
            headerBackground.classList.add("header__principal-active");
            menuMobile.innerHTML = '<i class="bi bi-x"></i>';
            body.style.overflow = 'hidden';
            descripcion.classList.add("main__principal__text__description__menu-active");
        } else {
            // Si el menú está abierto, ciérralo
            navMobile.classList.remove("header__principal__nav__list__mobile");
            headerBackground.classList.remove("header__principal-active");
            descripcion.classList.remove("main__principal__text__description__menu-active");
            body.style.overflow = 'auto';
            menuMobile.innerHTML = '<i class="bi bi-list"></i>';
        }
    }

    function handleResize() {
        var windowWidth = window.innerWidth;
        var isMobileMenuOpen = navMobile.classList.contains("header__principal__nav__list__mobile");
    
        // Si la ventana es mayor o igual a 1025px y el menú móvil está abierto, ciérralo
        if (windowWidth >= 1025 && isMobileMenuOpen) {
            navMobile.classList.remove("header__principal__nav__list__mobile");
            headerBackground.classList.remove("header__principal-active");
            descripcion.classList.remove("main__principal__text__description__menu-active");
            body.style.overflow = 'auto';
            menuMobile.innerHTML = '<i class="bi bi-list"></i>';
        }
    }
    
    window.addEventListener("resize", handleResize);
    
    handleResize();



    // let headerPrincipal = document.querySelector(".header__principal")
    // let lastScrollTop = 0;
    // let delta = 50;

    // window.addEventListener("scroll", function() {
    //     let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
    //     if (currentScroll > lastScrollTop && currentScroll > delta){
    //         headerPrincipal.style.top = '-80px'
    //     } else {
    //         headerPrincipal.style.top = '0px'
    //     }
        
    //     lastScrollTop = currentScroll;
    // }, false);

})