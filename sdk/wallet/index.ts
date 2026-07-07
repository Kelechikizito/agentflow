// this is to test the connection to the testnet and make sure it is working properly
import * as xrpl from "xrpl";
import { Wallet } from "xrpl";
import * as dotenv from "dotenv";

dotenv.config();

// XRPL SEED
const XRPL_SEED = process.env.XRPL_SEED;

// Define the network client
const TESTNET_URL = "wss://s.altnet.rippletest.net:51233";
const client = new xrpl.Client(TESTNET_URL);
await client.connect();
console.log("Connected to Testnet");

console.log("\nYour agentic wallet and Testnet XRP...");
const agenticWallet = Wallet.fromSeed(XRPL_SEED || "");
const agenticWalletAddress = agenticWallet.address;
console.log("Agentic Wallet Address:", agenticWalletAddress);

// Get the balance
const balance = await client.getXrpBalance(agenticWalletAddress);
console.log("Balance:", balance, "XRP");
await client.disconnect();
