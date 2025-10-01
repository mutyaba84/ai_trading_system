import useRealtime from "../hooks/useRealtime";
import { getAccount } from "../api/backend";

export default function AccountInfo() {
  const info = useRealtime(getAccount, 5000); // every 5 seconds

  if (!info) return <p>Loading account info...</p>;

  return (
    <div className="p-4 border rounded shadow bg-white">
      <h2 className="text-lg font-bold mb-2">Account Overview</h2>
      <p><b>Cash:</b> ${info.cash.toFixed(2)}</p>
      <p><b>Equity:</b> ${info.equity.toFixed(2)}</p>
      <p><b>Portfolio Value:</b> ${info.portfolio_value.toFixed(2)}</p>
      <p><b>Buying Power:</b> ${info.buying_power.toFixed(2)}</p>
      <p><b>Status:</b> {info.status}</p>
    </div>
  );
}
