// Manejar eventos y operaciones del carrito
document.addEventListener('DOMContentLoaded', function() {
    // Obtener elementos del DOM
    const listaProductos = document.getElementById('lista-productos');
    const btnAgregar = document.getElementById('btn-agregar');
    const btnEliminar = document.getElementById('btn-eliminar');
    const totalElement = document.getElementById('total');

    // Variables de estado
    let carrito = []; // Array para almacenar los productos agregados

    // Función para agregar un producto al carrito
    function agregarProducto(productoId) {
        // Realizar la solicitud AJAX al servidor (Django) para agregar el producto al carrito
        fetch(`/agregar-producto/${productoId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // Obtener el token CSRF de las cookies
                },
                body: JSON.stringify({}), // Puedes enviar datos adicionales si es necesario
            })
            .then(response => response.json())
            .then(data => {
                // Actualizar la interfaz y el estado del carrito en respuesta a la respuesta del servidor
            })
            .catch(error => {
                console.error('Error al agregar el producto:', error);
            });
    }

    // Función para eliminar un producto del carrito
    function eliminarProducto(productoId) {
        // Realizar la solicitud AJAX al servidor (Django) para eliminar el producto del carrito
        // Realizar la solicitud AJAX al servidor para eliminar el producto del carrito
        fetch(`/eliminar-producto/${productoId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // Obtener el token CSRF de las cookies
                },
                body: JSON.stringify({}), // Puedes enviar datos adicionales si es necesario
            })
            .then(response => response.json())
            .then(data => {
                // Actualizar la interfaz y el estado del carrito en respuesta a la respuesta del servidor
                // Puedes actualizar la lista de productos, el total, etc.
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
        // Actualizar la interfaz y el estado del carrito en respuesta a la respuesta del servidor
    }

    // Función para calcular y mostrar el total
    function calcularTotal() {
        // Calcular el total sumando los precios de los productos en el carrito
        // Actualizar el elemento totalElement en la interfaz con el resultado
    }

    // Eventos de clic para agregar y eliminar productos
    btnAgregar.addEventListener('click', function() {
        const productoId = 1; // Obtener el ID del producto seleccionado
        agregarProducto(productoId);
    });

    btnEliminar.addEventListener('click', function() {
        const productoId = 1; // Obtener el ID del producto a eliminar
        eliminarProducto(productoId);
    });
});