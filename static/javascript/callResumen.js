        function resumenForm () {
        fetch('../static/forms/resumen.html')
        .then(response => response.text())
        .then(data => {
        document.getElementById('tipoForm').innerHTML = data;
        });
}   
