import time
import requests
from secret import CIRCLE_API_KEY
from addresses import ADDRESSES

API_URL = "https://api.circle.com/v1/faucet/drips"
API_KEY = CIRCLE_API_KEY
BLOCKCHAIN = "SOL-DEVNET"


def request_usdc(address: str) -> None:
    if not API_KEY:
        raise RuntimeError("API key not found")

    payload = {
        "address": address,
        "blockchain": BLOCKCHAIN,
        "native": True,
        "usdc": True,
        "eurc": False,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    resp = requests.post(API_URL, json=payload, headers=headers, timeout=30)

    if resp.status_code == 204:
        print(f"[OK] {address}")
    else:
        print(f"[ERR] {address}: {resp.status_code} {resp.text}")


def main():
    for addr in ADDRESSES:
        request_usdc(addr)
        time.sleep(10)


if __name__ == "__main__":
    main()