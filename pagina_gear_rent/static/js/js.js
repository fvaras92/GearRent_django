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