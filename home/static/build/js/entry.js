document.addEventListener("DOMContentLoaded", (e) => {

    let modal = document.getElementById('modalLogin');
    let modalContenido = document.querySelector('.modal__contenido');

    try {
        let btnPrimaryLogin = document.querySelector('.entryblog__principal__comment__form-button-nologin') 
        btnPrimaryLogin.addEventListener('click', (e) =>{
            e.preventDefault()
            mostrarModal()
        })
    } catch (error) {
        console.log('error de boton');
    }

    

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



    try {
        const entrys = document.querySelectorAll('.published__article__principal__body-button-item')

        entrys.forEach(entry => {
            entry.addEventListener('click', (e) =>{
                if(entry.classList.contains('published__article__principal__body-button-item-notlogin')){
                    mostrarModal()
                }else{
                    let prueba = 'prueba_'+entry.id
                    if(entry.nextElementSibling !== null){
                        let eliminarPrueba = document.querySelector(`#entryForm${prueba}`)
                        eliminarPrueba.remove()
                    }else{
                        if (tinymce.get(prueba)) {
                            tinymce.get(prueba).remove();
                        }
                        let tinyMCE = `
                            <form  class="entryblog__principal__comment__form entryblog__principal__comment__form-alternative" id="entryForm${prueba}" method="post">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                <input type="hidden" id="relationship" name="relationship" value="${entry.id}">
                                <input type="hidden" id="identifier" name="identifier" value="children">
                                <input type="hidden" name="usuario" value="${userID}">
                                <input type="hidden" id="idpost" name="idpost" value="${postID}">
                                <textarea class="entryblog__principal__comment__form-editor" name="contenido" id="${prueba}" placeholder="Write a comment that helps the community...">
                                    ${contenidoSaveChildren}
                                </textarea>
                                <button class="entryblog__principal__comment__form-button" type="submit">Published</button>
                            </form>
                        `;
                        entry.insertAdjacentHTML("afterend", tinyMCE);
                        tinymce.init({
                            selector: `#${prueba}`,
                            plugins: 'link emoticons',
                            toolbar_mode: 'floating',
                            toolbar: 'undo redo | bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent |  removeformat | help',
                            menubar: false,
                        });
                    }
                }


            })
        })
    } catch (error) {
        console.log('no se encontraron comentarios');
    }   

})