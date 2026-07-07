import axios from "axios";

const api = axios.create({
  baseURL: "https://stockflow-1-e094.onrender.com/api/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;