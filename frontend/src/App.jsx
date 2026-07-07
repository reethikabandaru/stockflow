import { useEffect, useState } from "react";
import api from "./services/api";

function App() {
  const [dashboard, setDashboard] = useState({});
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get("dashboard/")
      .then((res) => {
        setDashboard(res.data);
      })
      .catch((err) => console.log(err));

    api.get("products/")
      .then((res) => {
        setProducts(res.data.results);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div style={{padding:"20px"}}>
      <h1>📦 StockFlow Dashboard</h1>

      <h3>Total Products: {dashboard.total_products}</h3>
      <h3>Total Quantity: {dashboard.total_quantity}</h3>
      <h3>Low Stock Items: {dashboard.low_stock_count || 0}</h3>

      <h2>Products</h2>

      {products.map((item) => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <p>SKU: {item.sku}</p>
          <p>Quantity: {item.quantity}</p>
          <p>Price: ₹{item.selling_price}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;
 