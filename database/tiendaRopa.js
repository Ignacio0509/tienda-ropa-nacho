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

