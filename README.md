# Proyecto Final  Tienda Ropa Nacho

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

---

 ### 6. Crear una nueva marca (POST)
 
* **Método:** ´POST´
* **Endpoint:** ´http://127.0.0.1:5000/api/marcas´
* **Descripción:** "Crea una nueva marca"

**Ejemplo de respuesta:**

´´´json
{
    "nombreMarca": "Adidas"
}
´´´
 
---

### 7. Obtener todas las marcas (GET)

* **Método:** ´GET´
* **Endpoint:** ´http://127.0.0.1:5000/api/marcas´
* **Descripción:** "Obtiene todas las marcas"

**Ejemplo de respuesta:**

Envía la solicitud. La respuesta debería ser una lista JSON con todas las marcas en la base de datos.

---

### 8. Obtener una marca específica (GET)

* **Método:** ´GET´
* **ENdpoint:** ´http://127.0.0.1:5000/api/marcas/<marca_id>´
* **Descripción:** "Obtiene el nombre de una marca en especifico por ID"

**Ejemplo de respuesta:**

Reemplaza <marca_id> con el id de una marca que hay creaste. Por ejemplo: http://127.0.0.1:5000/tienda/api/v1/marcas/685b7d5cf3ab5483f94990b4

---

### 9.  Actualizar una marca (PUT)

* **Método:** ´PUT´
* **Endpoint:** ´http://127.0.0.1:5000/api/marcas<marca_id>´
* **Descripción:** "Se actualizan los datos de la marca por medio del ID"


**Ejemplo de respuesta:**

´´´JSON

{
    "nombreMarca": "Adidas Original"
}
´´´
---

### 10. Eliminar una marca (DELETE)

* **Método:** ´DELETE´
* **Endpoint:** ´http://127.0.0.1:5000/api/marcas/<marca_id>´
* **Descripción:** "Se elimina la marca mediante el ID"

---
