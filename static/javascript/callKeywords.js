        function keywordsForm () {
        fetch('../static/forms/keywords.html')
        .then(response => response.text())
        .then(data => {
        document.getElementById('tipoForm').innerHTML = data;
        });
}   
