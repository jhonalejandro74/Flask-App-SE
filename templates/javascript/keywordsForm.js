function keywordsForm() {
 fetch('forms/keywords.html')
	.then(response => response.text())
	.then(data => {
	document.getElementById('tipoForm').innerHTML = data
	});
}
