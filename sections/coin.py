import httpx

from sections import Section

class CoinPriceSection(Section):
    apiurl: str = "https://api.coingecko.com/api/v3/simple/price"
    args: dict[str, str]

    def get_data(self):
        api_call = httpx.get(urlencode(apiUrl, args))
        coinprices = api_call.json()
        return coinprices

