// frontend/src/api/backend.js
import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend
});

export const getPrediction = (symbol) => API.get(`/model/predict?symbol=${symbol}`);
export const autoTrade = (symbol) => API.post(`/auto_trade?symbol=${symbol}`);
export const getTrades = () => API.get(`/trades`);
export const getAccount = () => API.get(`/account`);
export const getPositions = () => API.get(`/account/positions`);
