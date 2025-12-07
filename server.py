from fastapi import FastAPI

app = FastAPI()

# Temporary: hardcoded valid codes (for testing)
VALID_CODES = {"TEST123", "PAID999", "GOON777"}

@app.get("/validate")
def validate(code: str):
    if code in VALID_CODES:
        return {"status": "valid"}
    else:
        return {"status": "invalid"}
