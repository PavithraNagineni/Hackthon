from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pyngrok import ngrok
import uvicorn

# Create FastAPI app
app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    query_text = body['queryResult']['queryText']
    intent = body['queryResult']['intent']['displayName']

    if intent == "Default Welcome Intent":
        reply = "Hello! 👋 How can I help you today?"
    else:
        reply = f"You said: {query_text}"

    return JSONResponse({"fulfillmentText": reply})


if __name__ == "_main_":
    # Start ngrok tunnel
    public_url = ngrok.connect(8000, "http")
    print("✅ Your public HTTPS URL:", public_url)

    # Run FastAPI on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)