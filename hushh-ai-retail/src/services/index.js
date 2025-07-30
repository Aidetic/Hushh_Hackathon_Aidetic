import axios from 'axios';

const BASE_URL = import.meta.env.VITE_APP_BACKEND_URL;

console.log(BASE_URL, "9999");

// export const getDeals = async (payload) => {
//     const response = await axios.post(`${BASE_URL}/get_deals`, payload);
//     if (response.status === 200 && response.data?.mall_resp) {
//       return { data: response.data, error: null };
//     } else {
//       return { data: null, error: "Failed to fetch results" };
//     }
// };

export const getDeals = async (payload, onStreamMessage, onFinalReport) => {
  const response = await fetch(`${BASE_URL}/run_agent`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.body) {
    throw new Error("No response body returned.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");
  let fullText = "";
  let done = false;

  while (!done) {
    const { value, done: doneReading } = await reader.read();
    done = doneReading;

    const chunk = decoder.decode(value || new Uint8Array(), { stream: true });
    fullText += chunk;

    const lines = chunk.split("\n").filter(Boolean);
    for (const line of lines) {
      try {
        const parsed = JSON.parse(JSON.parse(line)) ;
        if (parsed.title === "logs") {
          onStreamMessage(parsed.content);
        } else if (parsed.title === "report") {
          onFinalReport(parsed.content);
        }
          // onStreamMessage(line);
      } catch (err) {
        console.warn(err);
      }
    }


  }
};
