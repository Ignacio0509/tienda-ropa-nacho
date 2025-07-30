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
  "prendaId": "1",
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

##   Endpoints de la API - Tienda

### 1. Obtener todos los libros

* **Metodo:** ´GET´
* **Endpoint:** ´´
* **Descripción:** Obtiene una lista de todas las prendas disponibles en el sistema

´´´http
GET link de la carpeta de las prendas
´´´


**Ejemplo de respuesta:**

´´´json
[
  {
    
  }
]


---

### 2. Obtener una prenda por ID

* **Metodo:** ´Get´
* **Endpoint:** ´´
* **Descripción:** Obtiene la información de una prenda en especifico usando su ID

´´´http
GET
´´´

**Ejemplo de respuesta:**

´´´json
{

}

---

### 3. Insertar una prenda nueva

* **Metodo:** ´Post´
* **Endpoint:** ´´
* **Descripción:** Inserta una prenda nueva en la base de datos

´´´http
Post
´´´

**Cuerpo de la petición (JSON):**

´´´json
{

}

**Ejemplo de respuesta:**

´´´json
{
"mensaje": "Prenda insertada exitosamente"
}
´´´

---


### 4. Actualizar una prenda por ID

* **Metodo:** ´Put´
* **Endpoint:** ´´
* **Descripción:** Actualiza la información de una prenda en especifico

´´´http
PUT
´´´

**Cuerpo de la petición (JSON):**

´´´json
{

}
´´´

**Ejemplo de respuesta**

´´´json
{
  "mensaje": "Prenda actualizada exitosamente"
}
´´´


---


### 5. Eliminar un libro por ID

* **Metodo:** ´Delete´
* **Endpoint:** ´´
* **Descripción:** Elimina una prenda en especifico de la base de datos

´´´http
DELETE
´´´

**Ejemplo de respuesta:**

´´´json
{
  "mensaje": "Prenda eliminada exitosamnete"
}
´´´
