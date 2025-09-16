// Capturamos el formulario
const form = document.getElementById("mentoriaForm");
const respuesta = document.getElementById("respuesta");

form.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita recargar la página

    // Obtenemos valores
    const nombre = document.getElementById("nombre").value;
    const materia = document.getElementById("materia").value;

    // Mostramos mensaje de confirmación
    respuesta.textContent = `¡Gracias ${nombre}! Tu solicitud para reforzar ${materia} ha sido enviada. Un profesor se pondrá en contacto contigo pronto.`;

    // Limpia el formulario
    form.reset();
});
