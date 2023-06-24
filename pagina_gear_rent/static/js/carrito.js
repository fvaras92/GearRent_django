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
    function agregarProducto() {
        // Aquí puedes obtener los datos del producto que deseas agregar al carrito
        // Puedes obtenerlos de elementos HTML o mediante alguna otra lógica de tu aplicación
        const productId = 123; // Reemplaza 123 con el ID del producto seleccionado

        // Realiza una llamada AJAX a tu vista de Django que maneja la acción de agregar al carrito existente
        fetch('/ruta-de-la-vista-de-agregar-al-carrito-existente/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}' // Asegúrate de incluir el token CSRF si es necesario
                },
                body: JSON.stringify({ product_id: productId }) // Envía el ID del producto seleccionado
            })
            .then(response => {
                if (response.ok) {
                    // La solicitud fue exitosa, puedes realizar alguna acción adicional si es necesario
                    console.log('Producto agregado al carrito existente');
                } else {
                    // La solicitud falló, puedes mostrar un mensaje de error o realizar alguna otra acción
                    console.log('Error al agregar el producto al carrito existente');
                }
            })
            .catch(error => {
                // Ocurrió un error en la solicitud, puedes mostrar un mensaje de error o realizar alguna otra acción
                console.log('Error en la solicitud: ' + error);
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