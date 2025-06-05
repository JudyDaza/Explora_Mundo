from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Datos de paquetes turísticos
paquetes = [
    {
        "id": 1,
        "nombre": "Villa de Leyva",
        "descripcion": "Explora la plaza más grande de Colombia y sus fascinantes museos.",
        "imagen": "https://images.unsplash.com/photo-1580234838923-c2e1a0439ad8",
        "precio": 180000,
        "duracion": "2 días / 1 noche",
        "incluye": ["Hospedaje", "Guía turístico", "Desayuno"]
    },
    {
        "id": 2,
        "nombre": "Lago de Tota",
        "descripcion": "Disfruta del lago más grande de Colombia y sus playas de arena blanca.",
        "imagen": "https://images.unsplash.com/photo-1589987606224-7c8860a6b044",
        "precio": 150000,
        "duracion": "3 días / 2 noches",
        "incluye": ["Hospedaje", "Alimentación completa", "Actividades acuáticas"]
    },
    {
        "id": 3,
        "nombre": "Sierra del Cocuy",
        "descripcion": "Aventúrate en el parque natural con los glaciares más hermosos.",
        "imagen": "https://images.unsplash.com/photo-1621451537084-482c73073a0f",
        "precio": 250000,
        "duracion": "4 días / 3 noches",
        "incluye": ["Hospedaje en refugio", "Guía especializado", "Equipo básico"]
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', paquetes=paquetes)

@app.route('/api/paquetes')
def obtener_paquetes():
    return jsonify(paquetes)

@app.route('/api/cotizar', methods=['POST'])
def cotizar():
    data = request.json
    destino_id = data.get('destino_id')
    personas = data.get('personas', 1)
    dias = data.get('dias', 1)
    
    paquete = next((p for p in paquetes if p['id'] == destino_id), None)
    
    if not paquete:
        return jsonify({"error": "Destino no encontrado"}), 404
    
    subtotal = paquete['precio'] * personas * dias
    
    # Aplicar descuentos
    descuento = 0
    if personas >= 4:
        descuento = 0.1
    elif dias >= 3:
        descuento = 0.05
        
    total = subtotal * (1 - descuento)
    
    return jsonify({
        "paquete": paquete['nombre'],
        "personas": personas,
        "dias": dias,
        "precio_unitario": paquete['precio'],
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total
    })

if __name__ == '__main__':
    app.run(debug=True)