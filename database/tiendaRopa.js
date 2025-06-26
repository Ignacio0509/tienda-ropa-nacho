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

///Cantidad vendida de prendas por fecha específica
db.Ventas.aggregate([
  {
    $match: {
      fechaVenta: {
        $eq: new Date("2025-06-25") 
      }
    }
  },
  {
    $group: {
      _id: "$fechaVenta",
      total_prendas_vendidas: { $sum: "$totalVenta" }
    }
  }
]);

//Lista de todas las prendas que tienen al menos una venta
db.Ventas.aggregate([
  {
    $lookup: {
      from: "Marcas",
      localField: "Marcas.marcaId",
      foreignField: "nombreMarca",
      as: "info_marcas"
    }
  },
  { $unwind: "$info_marcas" },
  {
    $group: {
      _id: {
        marcaId: "$info_marcas.nombreMarca",
      }
    }
  }
]);

//Prendas vendidas y su cantidad restante en stock
//Cantidad vendida de prendas por fecha y fíltrala con una fecha especifica
