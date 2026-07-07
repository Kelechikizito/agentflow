// Import the library
import xrpl from "xrpl";

// Define the network client
const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
try {
  await client.connect();
  console.log("Connected to Testnet");
  await client.disconnect();
} catch (err) {
  console.error("Failed to connect to Testnet:", err.message);
}
