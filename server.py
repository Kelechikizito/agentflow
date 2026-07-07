import os
from dotenv import load_dotenv
from fastapi import FastAPI
from x402_xrpl.server import require_payment

load_dotenv()

app = FastAPI()

# Protect the /hello endpoint with the x402 payment middleware.
# Requests that do not include a valid payment receipt receive a 402 response
# containing the payment requirements.
#
# extra={"sourceTag": ...} stamps every on-chain Payment that pays this
# endpoint with the given SourceTag, so you can filter and measure usage via
# any XRPL data API or block explorer.
# See /docs/agents/track-agent-behavior/ for more.
app.middleware("http")(
    require_payment(
        path="/hello",
        price=os.getenv("XRPL_PRICE_DROPS", "1000"),
        pay_to_address=os.getenv("XRPL_PAY_TO"),
        facilitator_url=os.getenv("XRPL_FACILITATOR_URL"),
        network="xrpl:1",  # xrpl:1 = Testnet, xrpl:0 = Mainnet
        asset="XRP",
        description="A paid hello world endpoint",
        extra={"sourceTag": int(os.getenv("XRPL_SOURCE_TAG", "20260601"))},
    )
)


@app.get("/hello")
async def hello():
    """Protected endpoint — requires payment."""
    return {"message": "Hello World! Thanks for the payment."}


@app.get("/health")
async def health():
    """Free endpoint — no payment required."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
