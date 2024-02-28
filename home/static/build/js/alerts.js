document.addEventListener("DOMContentLoaded", (e) => {
  let download_cv = document.querySelector('.download_cv')  
  download_cv.addEventListener("click", () =>{
      Swal.fire({
          title: "Are you sure?",
          text: "You won't be able to revert this!",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Yes, download"
        }).then((result) => {
          if (result.isConfirmed) {
            Swal.fire({
              title: "Deleted!",
              text: "Your file has been deleted.",
              icon: "success"
            });
          }
        });
    })


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
