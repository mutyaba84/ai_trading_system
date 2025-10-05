import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [portfolio, setPortfolio] = useState({});
  const [tradeSize, setTradeSize] = useState(1);
  const [stopLoss, setStopLoss] = useState(0.02);
  const [takeProfit, setTakeProfit] = useState(0.04);
  const [trailingStop, setTrailingStop] = useState(0.01);

  useEffect(() => {
    const interval = setInterval(async () => {
      const res = await axios.get("http://localhost:8000/portfolio_status");
      setPortfolio(res.data);
      setTradeSize(res.data.trade_size);
      setStopLoss(res.data.stop_loss);
      setTakeProfit(res.data.take_profit);
      setTrailingStop(res.data.trailing_stop);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  const updateTradeSize = async (val) => {
    setTradeSize(val);
    await axios.post("http://localhost:8000/update_trade_size", { size: val });
  };

  const updateRiskParams = async (sl, tp, ts) => {
    await axios.post("http://localhost:8000/update_risk_params", {
      stop_loss: sl,
      take_profit: tp,
      trailing_stop: ts,
    });
  };

  return (
    <div className="p-4 space-y-4">
      <h2 className="text-xl font-bold">Live Trading Dashboard</h2>

      <div className="p-2 bg-gray-50 rounded border shadow-sm">
        <h3 className="font-semibold">Portfolio</h3>
        <p>Cash: {portfolio.cash?.toFixed(2)}</p>
        <p>PnL: {portfolio.pnl?.toFixed(2)}</p>
        <h4>Positions:</h4>
        {portfolio.positions &&
          Object.entries(portfolio.positions).map(([asset, pos]) => (
            <p key={asset}>
              {asset}: {pos.size} @ {pos.avg_price.toFixed(2)}
            </p>
          ))}
      </div>

      <div className="p-2 bg-blue-50 rounded border shadow-sm">
        <h3 className="font-semibold">Trade Size</h3>
        <input
          type="range"
          min={0.1}
          max={10}
          step={0.1}
          value={tradeSize}
          onChange={(e) => updateTradeSize(parseFloat(e.target.value))}
          className="w-full"
        />
        <p>{tradeSize}</p>
      </div>

      <div className="p-2 bg-green-50 rounded border shadow-sm space-y-2">
        <h3 className="font-semibold">Risk Controls</h3>

        <label>Stop Loss %: {stopLoss}</label>
        <input
          type="range"
          min={0.001}
          max={0.1}
          step={0.001}
          value={stopLoss}
          onChange={(e) => {
            const val = parseFloat(e.target.value);
            setStopLoss(val);
            updateRiskParams(val, takeProfit, trailingStop);
          }}
          className="w-full"
        />

        <label>Take Profit %: {takeProfit}</label>
        <input
          type="range"
          min={0.001}
          max={0.2}
          step={0.001}
          value={takeProfit}
          onChange={(e) => {
            const val = parseFloat(e.target.value);
            setTakeProfit(val);
            updateRiskParams(stopLoss, val, trailingStop);
          }}
          className="w-full"
        />

        <label>Trailing Stop %: {trailingStop}</label>
        <input
          type="range"
          min={0.001}
          max={0.05}
          step={0.001}
          value={trailingStop}
          onChange={(e) => {
            const val = parseFloat(e.target.value);
            setTrailingStop(val);
            updateRiskParams(stopLoss, takeProfit, val);
          }}
          className="w-full"
        />
      </div>
    </div>
  );
}
