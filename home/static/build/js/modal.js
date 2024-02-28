// Obtén el modal y el botón para mostrarlo
var modal = document.getElementById('modalLogin');

var btnMostrarModal = document.getElementById('mostrarModal');

var modalContenido = document.querySelector('.modal__contenido');

function mostrarModal() {
    modal.style.display = 'block';
    setTimeout(function() {
      modal.classList.add('mostrar');
      modalContenido.style.opacity = "1"
    }, 300); 
  }


function cerrarModal() {
    modalContenido.style.opacity = "0"
    setTimeout(function() {
        modal.classList.remove('mostrar');
        modal.style.display = 'none';
    }, 300);
}

btnMostrarModal.onclick = mostrarModal;


var modal2 = document.getElementById('modalLogin2');
var btnMostrarModal2 = document.getElementById('mostrarModal2');
var modalContenido2 = document.querySelector('.modal__contenido2');

function mostrarModal2() {
  modal2.style.display = 'block';
  setTimeout(function() {
    modal2.classList.add('mostrar');
    modalContenido2.style.opacity = "1"
  }, 300); 
}


function cerrarModal2() {
  modalContenido2.style.opacity = "0"
  setTimeout(function() {
      modal2.classList.remove('mostrar');
      modal2.style.display = 'none';
  }, 300);
}

btnMostrarModal2.onclick = mostrarModal2;






window.onclick = function(event) {
  if (event.target == modal) {
    modalContenido.style.opacity = "0"
    setTimeout(function() {
        modal.classList.remove('mostrar');
        modal.style.display = 'none';
    }, 300);
  }

  else if (event.target == modal2) {
    modalContenido2.style.opacity = "0"
    setTimeout(function() {
        modal2.classList.remove('mostrar');
        modal2.style.display = 'none';
    }, 300);
  }
}