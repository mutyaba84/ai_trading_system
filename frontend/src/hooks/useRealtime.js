// frontend/src/hooks/useRealtime.js
import { useEffect, useState } from "react";

export default function useRealtime(fetchFunction, interval = 5000) {
  const [data, setData] = useState(null);

  useEffect(() => {
    let mounted = true;

    const fetchData = async () => {
      const result = await fetchFunction();
      if (mounted) setData(result);
    };

    fetchData();
    const id = setInterval(fetchData, interval);

    return () => {
      mounted = false;
      clearInterval(id);
    };
  }, [fetchFunction, interval]);

  return data;
}
