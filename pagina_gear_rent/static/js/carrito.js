document.addEventListener('DOMContentLoaded', function() {
    const listaProductos = document.getElementById('lista-productos');
    const btnAgregar = document.getElementById('btn-agregar');
    const btnEliminar = document.getElementById('btn-eliminar');
    const totalElement = document.getElementById('total');


    let carrito = []; // Array para almacenar los productos agregados

    function agregarProducto() {

        const productId = tipoprod;

        fetch('/ruta-de-la-vista-de-agregar-al-carrito-existente/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ product_id: tipoprod })
            })
            .then(response => {
                if (response.ok) {
                    console.log('Producto agregado al carrito existente');
                } else {
                    console.log('Error al agregar el producto al carrito existente');
                }
            })
            .catch(error => {
                console.log('Error en la solicitud: ' + error);
            });
    }

    function eliminarProducto(nombre) {
        fetch(`/eliminar-producto/${nombre}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // Obtener el token CSRF de las cookies
                },
                body: JSON.stringify({}), // Puedes enviar datos adicionales si es necesario
            })
            .then(response => response.json())
            .then(data => {})
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
    }

    // Función para calcular y mostrar el total
    function calcularTotal() {}

    // Eventos de clic para agregar y eliminar productos
    btnAgregar.addEventListener('click', function() {
        const productoId = 0;
        agregarProducto(productoId);
    });

    btnEliminar.addEventListener('click', function() {
        const productoId = 0;
        eliminarProducto(productoId);
    });
});