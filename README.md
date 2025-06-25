# Primer Proyecto  tienda-ropa-nacho

## Descripción del Proyecto
Este proyecto implementa una base de datos NoSQL para una tienda de ropa
utilizando MongoDB, gestionando usuarios, marcas, prendas y ventas

## Colecciones y Ejemplos JSON

### 👥 Usuarios
```json
{
  "usuarioId": "305340427",
  "nombre": "Ignacio Cedeño",
  "email": "luis.ignacio.cedeno.martinez@outlook.com",
  "rol": "cliente"
}
```
### Marcas
```json
{
  "marcaId": "1",
  "nombreMarca": "Nike"
}
```
### Categorias
```json
{
  "categoriaId": "1",
  "nombreCategoria": "Deportiva"
},
{
  "categoriaId": "2",
  "nombreCategoria": "Formal"
}
```
### Prendras
```json
{
  ""prendaId": "1",
  "nombrePrenda": "Camiseta Deportiva",
  "marcaId": "1", 
  "talla": "M",
  "color": "Negro",
  "precio": 25.00,
  "stock": 150,
  "categoriaId": "1"
}
```
### 🧾 Ventas
```json
{
  "usuarioId": "305340427",
  "fechaVenta": "2025-06-25",
  "numeroVenta": "1",
  "items": [
    {
      "prendaId": "1", 
      "cantidad": 2
    }
  ],
  "totalVenta": 50.00
}
```
## 👤 Integrantes del Proyecto
Ignacio Cedeño Martínez

