from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ExploraMundo API", description="API para cotización de viajes a Boyacá")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Precios por día por persona en COP
destinos = {
    "villa_de_leyva": 180000,
    "lago_de_tota": 150000,
    "tunja": 120000,
    "sierra_del_cocuy": 250000,
    "paipa": 140000
}

class Viaje(BaseModel):
    destino: str
    personas: int
    dias: int

@app.get("/destinos")
def listar_destinos():
    """Devuelve la lista de destinos disponibles"""
    return {"destinos": list(destinos.keys())}

@app.post("/cotizar")
def cotizar(viaje: Viaje):
    """Calcula el costo total de un viaje"""
    precio_base = destinos.get(viaje.destino.lower())
    
    if not precio_base:
        return {"error": "Destino no disponible"}
    
    subtotal = precio_base * viaje.personas * viaje.dias
    
    # Aplicar descuentos
    descuento = 0
    if viaje.personas >= 4:
        descuento = 0.1
    elif viaje.dias >= 7:
        descuento = 0.05
        
    monto_descuento = subtotal * descuento
    total = subtotal - monto_descuento
    
    return {
        "destino": viaje.destino,
        "personas": viaje.personas,
        "dias": viaje.dias,
        "precio_base": precio_base,
        "subtotal": subtotal,
        "descuento": descuento,
        "monto_descuento": monto_descuento,
        "total": total
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)