// frontend/src/components/EquityCurve.jsx
import React, { useEffect, useState } from "react";
import { getTrades } from "../api/backend";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function EquityCurve() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchTrades = async () => {
      const res = await getTrades();
      let equity = 10000; // starting balance
      const curve = res.data
        .reverse()
        .map((t, i) => {
          const pnl = t.side === "buy" ? -t.price * t.qty : t.price * t.qty;
          equity += pnl * 0.01;
          return { name: i, equity: parseFloat(equity.toFixed(2)) };
        });
      setData(curve);
    };
    fetchTrades();
  }, []);

  return (
    <div className="p-4 border rounded shadow bg-white">
      <h2 className="text-lg font-bold mb-2">Equity Curve</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="equity" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
