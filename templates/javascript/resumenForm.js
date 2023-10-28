function resumenForm () {
  fetch('/forms/resumen.html')
	.then(response => response.text())
	.then(data => {
	document.getElementById('tipoForm'.innerHTML = data;
	)});
}
