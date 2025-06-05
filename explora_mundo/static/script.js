/// Función para el botón "Ver más"
function verMas(boton) {
    const description = boton.previousElementSibling;
    const destino = boton.getAttribute("data-destino"); // Obtiene el valor de data-destino
    
    
    // Redirige a la página específica después de 1 segundo
    setTimeout(function() {
        window.location.href = destino; // Usa la variable con el destino dinámico
    }, 1000);

    

    // Animación de confirmación
    boton.parentElement.style.boxShadow = "0 0 20px rgba(18, 89, 54, 0.5)";
    setTimeout(() => {
        boton.parentElement.style.boxShadow = "0 5px 15px rgba(0, 0, 0, 0.1)";
    }, 1000);
}

// Cotizador de viajes
document.getElementById('cotizadorForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const destino = document.getElementById('destino').value;
    const personas = parseInt(document.getElementById('personas').value);
    const dias = parseInt(document.getElementById('dias').value);
    
    if (!destino || isNaN(personas) || isNaN(dias)) {
        alert("Por favor completa todos los campos correctamente.");
        return;
    }
    
    // Simulación de cotización (en un proyecto real, aquí se conectaría a la API)
    const precios = {
        "villa_de_leyva": 180000,
        "lago_de_tota": 150000,
        "tibasosa": 120000,
        "sierra_del_cocuy": 250000,
        "raquira": 140000
    };
    
    const precioBase = precios[destino];
    const subtotal = precioBase * personas * dias;
    
    // Aplicar descuentos
    let descuento = 0;
    if (personas >= 4) {
        descuento = 0.1; // 10% de descuento para grupos
    } else if (dias >= 7) {
        descuento = 0.05; // 5% de descuento para estadías largas
    }
    
    const montoDescuento = subtotal * descuento;
    const total = subtotal - montoDescuento;
    
    // Mostrar resultados
    const resultadoDiv = document.getElementById('resultadoCotizacion');
    resultadoDiv.innerHTML = `
        <h3>Cotización para ${document.getElementById('destino').options[document.getElementById('destino').selectedIndex].text}</h3>
        <p><strong>Personas:</strong> ${personas}</p>
        <p><strong>Días:</strong> ${dias}</p>
        <p><strong>Precio base por persona/día:</strong> $${precioBase.toLocaleString('es-CO')} COP</p>
        ${descuento > 0 ? `<p><strong>Descuento (${descuento * 100}%):</strong> -$${montoDescuento.toLocaleString('es-CO')} COP</p>` : ''}
        <p><strong>TOTAL:</strong> $${total.toLocaleString('es-CO')} COP</p>
    `;
    resultadoDiv.style.display = 'block';
});

// Validación del formulario de contacto
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Simulación de envío
    const form = e.target;
    const button = form.querySelector('button');
    const originalText = button.textContent;
    
    button.textContent = "Enviando...";
    button.disabled = true;
    
    setTimeout(() => {
        button.textContent = "¡Mensaje enviado!";
        button.style.backgroundColor = "#125936";
        form.reset();
        
        setTimeout(() => {
            button.textContent = originalText;
            button.disabled = false;
            button.style.backgroundColor = "#d52b1e";
        }, 3000);
    }, 1500);
});

// Scroll suave para enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: 'smooth'
        });
    });
});

// Efecto de aparición al hacer scroll
const fadeElements = document.querySelectorAll('.paquete, .cotizador-container');

function checkFade() {
    fadeElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementTop < windowHeight - 100) {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
        }
    });
}

// Establecer estado inicial
fadeElements.forEach(element => {
    element.style.opacity = "0";
    element.style.transform = "translateY(20px)";
    element.style.transition = "opacity 0.5s, transform 0.5s";
});

// Verificar al cargar y al hacer scroll
window.addEventListener('load', checkFade);
window.addEventListener('scroll', checkFade);