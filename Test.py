import requests

# Replace the URL with the actual endpoint of the REST service you want to consume
#url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
#url = "https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=36"
url = "https://appfeeds.moneycontrol.com/jsonapi/market/indices&format=json&t_device=iphone&t_app=MC&t_version=48&ind_id=23"

# If the API requires authentication, you can pass credentials using the auth parameter
# Example: auth = ("username", "password")
headers = {
    "Cookie": "MC_PPID_LOGIC=normaluser20093237737077148mcids; _gcl_au=1.1.1534690776.1703762540; _cb=Dzuv30DhU_hMDvjIW2; _chartbeat2=.1703762539813.1703762539813.1.CQ1IO7Blhu_vatBO5DxQ1rVMKVG-.1; _sharedID=b24ed0ad-c2c6-4300-aaff-97a105926fc4; WZRK_G=78b2497c35384fcfae15f4b0ede71206; _cc_id=7579dc38773491d0bdfb56efaa516b1b; __gads=ID=ddd232d9e794b8d7:T=1703762544:RT=1703762544:S=ALNI_MZDdNXMsuwcCkc3uxNREEhkXondPA; __gpi=UID=00000cc889e5618d:T=1703762544:RT=1703762544:S=ALNI_Mb1mm16k7NATUDa5mUoCL8LMO4CTw; _au_1d=AU1D-0100-001703762548-JBTA4LKZ-PABO; _au_last_seen_pixels=eyJhcG4iOjE3MDM3NjI1NDgsInR0ZCI6MTcwMzc2MjU0OCwicHViIjoxNzAzNzYyNTQ4LCJydWIiOjE3MDM3NjI1NDgsInRhcGFkIjoxNzAzNzYyNTQ4LCJhZHgiOjE3MDM3NjI1NDgsImdvbyI6MTcwMzc2MjU0OCwic21hcnQiOjE3MDM3NjI1NDgsImFkbyI6MTcwMzc2MjU0OCwidGFib29sYSI6MTcwMzc2MjU0OH0%3D; _ga=GA1.2.878778803.1703762534; FCNEC=%5B%5B%22AKsRol9WBSDgqUHkpxMLw4LDS3mcazykARvFGenKvNgrjxzJxSdRukX83DVEM98IWdNSohfkeZR4VS7aWYeLxetlVzsRlBjxXKF1GwNvaKeQUTwra_Ihkecp3qq4MTuH3Gmmnl9TClZqj2ZAhLg4Bq00JRHR1BO2Bg%3D%3D%22%5D%5D; _ga_4S48PBY299=GS1.1.1703762542.1.1.1703762565.0.0.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# Make a GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # The response content (usually in JSON format for REST APIs) can be accessed using response.json()
    data = response.json()
    #for item in data:
     #   print("Item:", item)
    print("Data from the API:", data["indices"]["lastprice"])
else:
    print("Error:", response.status_code, response.text)
