import { useEffect, useState } from "react";
import api from "./services/api";

function App() {
  const [dashboard, setDashboard] = useState(null);

  useEffect(() => {
    api
      .get("dashboard/")
      .then((response) => {
        setDashboard(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  if (!dashboard) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>📦 StockFlow Dashboard</h1>

      <hr />

      <h2>Total Products: {dashboard.total_products}</h2>

      <h2>Total Quantity: {dashboard.total_quantity}</h2>

      <h2>Low Stock Items: {dashboard.low_stock_count}</h2>
    </div>
  );
}

export default App;