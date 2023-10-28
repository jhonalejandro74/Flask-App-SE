        function temaForm () {
        fetch('../static/forms/tema.html')
        .then(response => response.text())
        .then(data => {
        document.getElementById('tipoForm').innerHTML = data;
        });
}   

