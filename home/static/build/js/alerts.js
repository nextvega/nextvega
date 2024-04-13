document.addEventListener("DOMContentLoaded", (e) => {
  const links = document.querySelectorAll("a[href='#']");
  links.forEach(link => {
      link.addEventListener("click", function(event) {
        event.preventDefault();
        Toastify({
          text: "The Link Is Not Available",
          duration: 3000,
          style: {
            background: "linear-gradient(to right bottom, rgb(71, 128, 252), rgb(139, 94, 243))",
          }
        }).showToast();
      });
  });

})
