#!/usr/bin/env python3
import httpx

def coin_price(p, coin="bitcoin"):
    # bitcoin price
    api_call= httpx.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    coinprice = api_call.json()[coin]["usd"]
    p.text(f"{coin} price: ")
    p.set(bold=True, underline=True)
    p.textln(f"${coinprice}")
    p.set_with_default()

