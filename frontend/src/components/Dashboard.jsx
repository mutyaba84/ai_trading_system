// frontend/src/components/Dashboard.jsx
import React from "react";
import TradeLog from "./TradeLog";
import EquityCurve from "./EquityCurve";
import AccountInfo from "./AccountInfo";
import Positions from "./Positions";

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-center mb-6">AI Trading Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <AccountInfo />
        <Positions />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <TradeLog />
        <EquityCurve />
      </div>
    </div>
  );
}
