// frontend/src/components/TradeLog.jsx
import React, { useEffect, useState } from "react";
import { getTrades } from "../api/backend";

export default function TradeLog() {
  const [trades, setTrades] = useState([]);

  useEffect(() => {
    const fetchTrades = async () => {
      const res = await getTrades();
      setTrades(res.data);
    };
    fetchTrades();
  }, []);

  return (
    <div className="p-4 border rounded shadow bg-white">
      <h2 className="text-lg font-bold mb-2">Trade Log</h2>
      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th>Symbol</th>
            <th>Side</th>
            <th>Qty</th>
            <th>Price</th>
            <th>Status</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {trades.map((t, i) => (
            <tr key={i} className="border-t">
              <td>{t.symbol}</td>
              <td>{t.side}</td>
              <td>{t.qty}</td>
              <td>{t.price}</td>
              <td>{t.status}</td>
              <td>{t.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
