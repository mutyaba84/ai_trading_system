// frontend/src/components/Positions.jsx
import React, { useEffect, useState } from "react";
import { getPositions } from "../api/backend";

export default function Positions() {
  const [positions, setPositions] = useState([]);

  useEffect(() => {
    const fetchPositions = async () => {
      const res = await getPositions();
      setPositions(res.data);
    };
    fetchPositions();
  }, []);

  return (
    <div className="p-4 border rounded shadow bg-white">
      <h2 className="text-lg font-bold mb-2">Open Positions</h2>
      {positions.length === 0 ? (
        <p>No open positions</p>
      ) : (
        <table className="w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th>Symbol</th>
              <th>Qty</th>
              <th>Side</th>
              <th>Entry Price</th>
              <th>Market Value</th>
              <th>Unrealized P/L</th>
            </tr>
          </thead>
          <tbody>
            {positions.map((p, i) => (
              <tr key={i} className="border-t">
                <td>{p.symbol}</td>
                <td>{p.qty}</td>
                <td>{p.side}</td>
                <td>${p.avg_entry_price}</td>
                <td>${p.market_value}</td>
                <td className={p.unrealized_pl >= 0 ? "text-green-600" : "text-red-600"}>
                  ${p.unrealized_pl}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
