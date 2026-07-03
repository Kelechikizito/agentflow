For developers or new users who want to try out the features of XRPL without investing their own funds, there are two developer environments, Testnet and Devnet. Users can create an account funded with 1,000 (fake) XRP and connect to either environment to interact with the XRPL.[https://xrpl.org/docs/introduction/what-is-the-xrp-ledger]

### Sample XRP TX

Here is a sample transaction in JSON format. This transaction transfers 1 XRP from account rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn to destination account ra5nK24KXen9AHvsdFTKHSANinZseWnPcX.

```json
{
  "TransactionType": "Payment",
  "Account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
  "Amount": "1000000",
  "Destination": "ra5nK24KXen9AHvsdFTKHSANinZseWnPcX"
}
```

You send the transaction to the ledger as a command from JavaScript, Python, the command line, or any compatible service. The xrpld servers propose transactions to the XRPL.

When 80% of the validators approve a current set of proposed transactions, they are recorded as part of the permanent ledger. The xrpld server returns the results of the transaction you sent.

### XRP Requests

Requests are used to get information from the ledger, but they do not make changes to the ledger (similar to pure and view solidity functions, lol). The information is freely available to anyone to view, so there is no need to sign in with your account information.

When you submit your request, it might be processed by an xrpld server or by a Clio server, a server that is dedicated to responding to requests. Clio servers take some of the load off the other xrpld servers on the XRPL to improve processing speed and reliability.

This is a sample request in JSON format. This request gets the current account information for the account number you provide.

```json
{
  "command": "account_info",
  "account": "rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn"
}
```

The request returns a wealth of information. Here is an example response for an account information request in JSON format.

```json
{
    "result": {
        "account_data": {
            "Account": "rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn",
            "Balance": "999999999960",
            "Flags": 8388608,
            "LedgerEntryType": "AccountRoot",
            "OwnerCount": 0,
            "PreviousTxnID": "4294BEBE5B569A18C0A2702387C9B1E7146DC3A5850C1E87204951C6FDAA4C42",
            "PreviousTxnLgrSeq": 3,
            "Sequence": 6,
            "index": "92FA6A9FC8EA6018D5D16532D7795C91BFB0831355BDFDA177E86C8BF997985F"
        },
        "ledger_current_index": 4,
        "queue_data": {
            "auth_change_queued": true,
            "highest_sequence": 10,
            "lowest_sequence": 6,
            "max_spend_drops_total": "500",
            "transactions": [
                {
                    "auth_change": false,
                    "fee": "100",
                    "fee_level": "2560",
                    "max_spend_drops": "100",
                    "seq": 6
                },
                ... (trimmed for length) ...
                {
                    "LastLedgerSequence": 10,
                    "auth_change": true,
                    "fee": "100",
                    "fee_level": "2560",
                    "max_spend_drops": "100",
                    "seq": 10
                }
            ],
            "txn_count": 5
        },
        "status": "success",
        "validated": false
    }
```

### Middleware

Middleware services are programs that consume the XRP Ledger APIs on one side and provide their own APIs on the other side.

Unlike client libraries, which are instantiated fresh and shut down with the program that imports them, middleware services typically stay running indefinitely, and may have their own databases (relational SQL databases or otherwise) and configuration files. Some are available as cloud services with various pricing or usage limitations.

### Apps and Services

Atop the stack is where the truly exciting things happen. Apps and services provide a way for users and devices to connect to the XRP Ledger. Services like private exchanges, token issuers, marketplaces, interfaces to the decentralized exchange, and wallets provide user interfaces for buying, selling, and trading various assets including XRP and tokens of all kinds. Many other possibilities exist, including additional services layered even higher.

### XRPL Smart Contracts

Smart contracts on the XRP Ledger work through conditionally held escrows.
