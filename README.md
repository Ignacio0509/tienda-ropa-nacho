# Primer Proyecto- tienda-ropa-nacho

## Descripción del Proyecto
Este proyecto implementa una base de datos NoSQL para una tienda de ropa
utilizando MongoDB, gestionando usuarios, marcas, prendas y ventas

## Colecciones y Ejemplos JSON

### Usuarios
```json
{
  "usuarioId": "305340427",
  "nombre": "Ignacio Cedeño",
  "email": "luis.ignacio.cedeno.martinez@outlook.com",
  "rol": "cliente",
  "fechaRegistro": "2025-06-20"
}
```
### Marcas
```json
{
  "nombreMarca": "Nike",
  "paisOrigen": "Estados Unidos",
  "fechaFundacion": "1964-01-25"
}
```
### Prendras
```json
{
  "nombrePrenda": "Camiseta Deportiva",
  "marcaId": "1", 
  "talla": "M",
  "color": "Negro",
  "precio": 25.00,
  "stock": 150,
  "categoria": "Deportiva"
}
```
### Ventas
```json
{
  "usuarioId": "305340427",
  "fechaVenta": "2025-06-25",
  "items": [
    {
      "prendaId": "1", 
      "cantidad": 2,
      "precioUnitario": 25.00
    }
  ],
  "totalVenta": 50.00
}
```
## Integrantes del Proyecto
Ignacio Cedeño Martínez

