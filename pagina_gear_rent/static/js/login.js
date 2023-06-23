document.getElementById("btn-registro").addEventListener("click",register);
document.getElementById("btn-init").addEventListener("click",iniciar);
window.addEventListener("resize",anchoPag);

var contenedor_doble = document.querySelector(".contenedor-doble");
var form_login = document.querySelector(".form-login");
var form_registro = document.querySelector(".form-registro");
var caja_login = document.querySelector(".caja.login");
var caja_registro = document.querySelector(".caja.registro");

//Reponsiva

function anchoPag(){
    if(window.innerWidth > 850){
        caja_login.style.display = "block";
        caja_registro.style.display = "block";
    }else{
        caja_registro.style.display = "block";
        caja_registro.style.opacity = "1";
        caja_login.style.display = "none";
        form_login.style.display = "block";
        form_registro.style.display = "none";
        contenedor_doble.style.left = "0px";
    }

}



//funcion para el registro
function register(){
    if(window.innerWidth > 850){
        form_registro.style.display ="block";
        contenedor_doble.style.left="410px";
        form_login.style.display="none";
        caja_registro.style.opacity="0";
        caja_login.style.opacity="1";
    }else{
        form_registro.style.display ="block";
        contenedor_doble.style.left="0px";
        form_login.style.display="none";
        caja_registro.style.display="none";
        caja_login.style.display="block";
        caja_login.style.opacity="1";

    }

}

//funcion para el iniciar
function iniciar(){
    if(window.innerWidth > 850){
        form_registro.style.display ="none";
        contenedor_doble.style.left="10px";
        form_login.style.display="block";
        caja_registro.style.opacity="1";
        caja_login.style.opacity="0";
}else{
    form_registro.style.display ="none";
    contenedor_doble.style.left="0px";
    form_login.style.display="block";
    caja_registro.style.display="block";
    caja_login.style.display="none";
    }
}

//validar correo
document.getElementById("btn-cuentaNueva").addEventListener("click", validarRegistro);

function validarRegistro(event) {
    event.preventDefault();
  
    var nombreInput = document.querySelector(".form-registro input[type='text'][placeholder='Nombre Usuario']");
    var correoInput = document.getElementById("user-email");
    var contrasenaInput = document.querySelector(".form-registro input[type='password']");
    var nombre = nombreInput.value.trim();
    var correo = correoInput.value.trim();
    var contrasena = contrasenaInput.value;
  
    // Validar nombre completo
    if (nombre === "") {
      mostrarError("Nombre Usuario no puede estar vacío.");
      return;
    }
  
    // Validar correo electrónico
    if (!validarCorreo(correo)) {
      mostrarError("Correo electrónico inválido.");
      return;
    }
  
    // Validar contraseña
    if (contrasena.length < 5) {
      mostrarError("La contraseña debe tener al menos 5 caracteres.");
      return;
    }
  
    // Si todas las validaciones pasan, mostrar mensaje de registro exitoso
    mostrarRegistroExitoso();
  }
  
  function validarCorreo(correo) {
    var regex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;
    return regex.test(correo);
  }
  
  function mostrarError(mensaje) {
    var errorDiv = document.getElementById("mensaje-registro");
    errorDiv.innerHTML = mensaje;
    errorDiv.style.display = "block";
  }
  
  function mostrarRegistroExitoso() {
    var mensajeDiv = document.getElementById("mensaje-registro");
    mensajeDiv.innerHTML = "Registro exitoso.";
    mensajeDiv.style.display = "block";
  }
  
  
  
  
  
  
