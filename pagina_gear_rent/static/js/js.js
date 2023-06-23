document.addEventListener("DOMContentLoaded", function() {
    var preamplificadoresLink = document.getElementById("preamplificadores-link");
    var compresoresLink = document.getElementById("compresores-link");
    var equalizadoresLink = document.getElementById("equalizadores-link");

    if (preamplificadoresLink) {
        preamplificadoresLink.addEventListener("click", function(event) {
            event.preventDefault();
            cambiarNombreSeccion("Preamplificadores");
            window.location.href = event.target.href;
        });
    }

    if (compresoresLink) {
        compresoresLink.addEventListener("click", function(event) {
            event.preventDefault();
            cambiarNombreSeccion("Compresores");
            window.location.href = event.target.href;
        });
    }

    if (equalizadoresLink) {
        equalizadoresLink.addEventListener("click", function(event) {
            event.preventDefault();
            cambiarNombreSeccion("Equalizadores");
            window.location.href = event.target.href;
        });
    }

    function cambiarNombreSeccion(nombreSeccion) {
        var tituloSeccion = document.getElementById("titulo-seccion");
        if (tituloSeccion) {
            tituloSeccion.innerHTML = nombreSeccion;
        }
    }
});



// Espera a que se cargue el documento
document.addEventListener("DOMContentLoaded", function() {
    // Obtiene el enlace del modal
    var modalLink = document.getElementById("openModalProducto2");

    // Escucha el evento de clic en el enlace
    modalLink.addEventListener("click", function(event) {
        event.preventDefault(); // Evita el comportamiento predeterminado del enlace

        // Muestra el modal
        var modal = document.getElementById("modalProducto2");
        modal.style.display = "block";
    });
});