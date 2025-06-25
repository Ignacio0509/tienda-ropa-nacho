//CRUD para la tienda de ropa

//Conexion a la base de datos
use tiendaRopa;

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

//Lista de todaslas prendas que tienen al menos una venta
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
