//CRUD para la tienda de ropa

//Conexion a la base de datos
use tiendaRopa;

//Crea colección o tabla MARCAS
db.createCollection("Marcas")

//Crea un nuevo documento en la coleccion MARCAS
db.Marcas.insertOne({marcaId:1, nombreMarca:"Adidas"})

//Actualiza un documento en la colección MARCAS
db.Marcas.updateOne(
  { marcaId: 1 }, 
  {
    $set: {                     
      nombreMarca: "Adidas2"
    }
  }
);

//Borra un documento de la coleccion MARCAS
db.Marcas.deleteOne({
  nombreMarca: "Adidas2" 
});

//CREA COLECCION PRENDAS
db.createCollection("Prendas")

//CREA un documento en la colección PRENDAS
db.Prendas.insertOne({prendaId: 1, nombrePrenda:"Camisa",marcaId:1, talla: "M", color: "Azul", precio: 3.99, stock: 8, categoriaId : 1})

//ACTUALIZA documento en la colección PRENDAS
db.Prendas.updateOne(
  { prendaId: 1 }, 
  {
    $set: {                     
      nombrePrenda: "Camisa",
	  marcaId: 2,
	  talla: "S",
	  color: "Verde",
	  precio: 4,
	  stock: 10,
	  categoriaId : 2
    }
  }
);

//BORRA un documento de la coleccion PRENDAS
db.Prendas.deleteOne({
  prendaId: 1 // FILTRO: Elimina el primer documento donde prendaId es 1
});

//Crea colección USUARIOS
db.createCollection("Usuarios")

//CREA un documento en la colección USUARIOS
db.Usuarios.insertOne({usuarioId: 1, nombre:"Luis",rol:"cliente", correo: "luis@correo.com"})

//ACTUALIZA un documento en la colección USUARIOS
db.Usuarios.updateOne(
  { usuarioId: 1 }, 
  {
    $set: {                     
      nombre: "Alberto",
	  rol: "lciente",
	  correo: "alberto@correo.com"
    }
  }
);

//Consultas

//Obtener lacantidad vendida de prendas por fecha y filtrada con una fecha específica
db.Ventas.aggregate([
  {
    $match: { //Filtrar por una fecha específica.
      fechaVenta: "27/07/1975"
    }
  },
  {
    $unwind: "$items" //Descomponer el arreglo items para trabajar con cada prenda vendida individualmente.
  },
  {
    $group: { //Agrupar por la fecha de venta y sumar la cantidad de prendas vendidas.
      _id: "$fechaVenta",
      totalPrendasVendidas: { $sum: "$items.cantidad" }
    }
  }
]);

//Resultado esperado
[
  {
    "_id": "10/06/2025",
    "totalPrendasVendidas": 2
  }
]

//Obtener el listado de todas las marcas que tienen al menos unaventa
db.Ventas.aggregate([
  {
    $unwind: "$items" //Descomponer ($unwind) los items de la venta.
  },
  {
    $lookup: { //Unir ($lookup) cada prenda vendida desde items.prendaId con la colección Prendas.
      from: "Prendas",
      localField: "items.prendaId",
      foreignField: "prendaId",
      as: "prenda"
    }
  },
  {
    $unwind: "$prenda"
  },
  {
    $lookup: { //*Unir ($lookup) con la colección Marcas, usando marcaId desde Prendas.
      from: "Marcas",
      localField: "prenda.marcaId",
      foreignField: "marcaId",
      as: "marca"
    }
  },
  {
    $unwind: "$marca"
  },
  {
    $group: { //Agrupar ($group) por nombreMarca para eliminar duplicados (una marca puede aparecer en múltiples
      _id: "$marca.marcaId",
      nombreMarca: { $first: "$marca.nombreMarca" }
    }
  },
  {
    $project: { //($project) solo muestra el nombre de la marca.
      _id: 0,
      nombreMarca: 1
    }
  }
]);
//Resultñado esperado
[
  {
    "nombreMarca": "Adidas"
  }
]


//Obtener las prendas vendidas y su cantidad restante en stock
db.Ventas.aggregate([
  {
    $unwind: "$items" //Descompone los items para trabajar prenda por prenda.
  },
  {
    $group: { //Agrupa por prendaId y suma las cantidades vendidas.
      _id: "$items.prendaId",
      cantidadVendida: { $sum: "$items.cantidad" }
    }
  },
  {
    $lookup: { //Une con la colección Prendas para traer información adicional, como el nombrePrenda y el stock
      from: "Prendas",
      localField: "_id",
      foreignField: "prendaId",
      as: "prenda"
    }
  },
  {
    $unwind: "$prenda"
  },
  {
    $project: { //Limpia y presenta los campos deseados.
      _id: 0,
      prendaId: "$_id",
      nombrePrenda: "$prenda.nombrePrenda",
      cantidadVendida: 1,
      stock: "$prenda.stock"
    }
  }
]);
//Resultado esperado
[
  {
    "prendaId": 1,
    "nombrePrenda": "Camisa",
    "cantidadVendida": 2,
    "stock": 8
  }
]

//Obtener el listado de las 5 marcas mas vendidas y su cantidad de ventas
db.Ventas.aggregate([
  {
    $unwind: "$items" // para tratar cada prenda vendida individualmente.
  },
  {
    $lookup: { //$lookup a Prendas: para saber a qué prenda corresponde cada prendaId.
      from: "Prendas",
      localField: "items.prendaId",
      foreignField: "prendaId",
      as: "prenda"
    }
  },
  {
    $unwind: "$prenda"
  },
  {
    $lookup: {// $lookup a Marcas: para obtener el nombreMarca desde marcaId.
      from: "Marcas",
      localField: "prenda.marcaId",
      foreignField: "marcaId",
      as: "marca"
    }
  },
  {
    $unwind: "$marca"
  },
  {
    $group: { //$group por nombreMarca: suma de cantidades vendidas por marca.
      _id: "$marca.nombreMarca",
      cantidadVendida: { $sum: "$items.cantidad" }
    }
  },
  {
    $sort: { //$sort + $limit: ordenar descendente y limita a las 5 más vendidas.
      cantidadVendida: -1
    }
  },
  {
    $limit: 5
  },
  {
    $project: { //$project: limpia el resultado y lo deja legible.
      _id: 0,
      nombreMarca: "$_id",
      cantidadVendida: 1
    }
  }
]);
//Resultado esperado

[
  { "nombreMarca": "Adidas", "cantidadVendida": 2 },
  { "nombreMarca": "Nike", "cantidadVendida": 1 },
  ...
]

