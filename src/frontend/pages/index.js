import { useState, useEffect } from "react";

export default function RiskControlPanel() {
  const [stopLoss, setStopLoss] = useState(0.02);
  const [takeProfit, setTakeProfit] = useState(0.04);
  const [trailingStop, setTrailingStop] = useState(0.015);

  // Fetch current risk settings from backend
  const fetchRisk = async () => {
    const res = await fetch("http://localhost:5000/api/get_risk");
    const data = await res.json();
    setStopLoss(data.stop_loss_pct);
    setTakeProfit(data.take_profit_pct);
    setTrailingStop(data.trailing_stop_pct);
  };

  useEffect(() => {
    fetchRisk();
    const interval = setInterval(fetchRisk, 5000); // auto-refresh every 5s
    return () => clearInterval(interval);
  }, []);

  const updateRisk = async () => {
    await fetch("http://localhost:5000/api/update_risk", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        stop_loss_pct: stopLoss,
        take_profit_pct: takeProfit,
        trailing_stop_pct: trailingStop
      })
    });
    fetchRisk();
    alert("✅ Risk parameters updated!");
  };

  return (
    <div className="p-4 bg-gray-100 rounded-lg shadow-md space-y-3">
      <h2 className="font-bold text-lg">⚖️ Risk Control Panel</h2>

      <div>
        <label>Stop Loss %</label>
        <input
          type="number"
          step="0.001"
          value={stopLoss}
          onChange={(e) => setStopLoss(parseFloat(e.target.value))}
          className="ml-2 p-1 border rounded"
        />
      </div>

      <div>
        <label>Take Profit %</label>
        <input
          type="number"
          step="0.001"
          value={takeProfit}
          onChange={(e) => setTakeProfit(parseFloat(e.target.value))}
          className="ml-2 p-1 border rounded"
        />
      </div>

      <div>
        <label>Trailing Stop %</label>
        <input
          type="number"
          step="0.001"
          value={trailingStop}
          onChange={(e) => setTrailingStop(parseFloat(e.target.value))}
          className="ml-2 p-1 border rounded"
        />
      </div>

      <button
        onClick={updateRisk}
        className="mt-3 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Update Risk Settings
      </button>

      <div className="mt-4 p-2 bg-white rounded border shadow-sm">
        <h3 className="font-semibold">📊 Current Settings</h3>
        <p>Stop Loss: {stopLoss * 100}%</p>
        <p>Take Profit: {takeProfit * 100}%</p>
        <p>Trailing Stop: {trailingStop * 100}%</p>
      </div>
    </div>
  );
}

