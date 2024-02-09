$(function () {
    $('#tableData').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": null}, 
            {"data": "cedula"}, 
            {"data": "nombre"}, 
            {"data": "apellidos"}, 
            {"data": "fecha_nacimiento"}, 
            {"data": "edad"}, 
            {"data": "genero"}, 
            {"data": "altura"}, 
            {"data": "peso"}, 
            {"data": "Estamento"}, 
            {"data": "SeleccionadoDeportivo"}, 
            {"data": "promedio_total_acomulado"}, 
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = `<a href="#" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                   <a href="#" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            // Puedes agregar código de inicialización adicional aquí si es necesario
        }
    });
});
