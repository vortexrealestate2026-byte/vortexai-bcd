import requests

def fetch_redfin(zipcode="90210"):
    url = f"https://www.redfin.com/stingray/api/gis-csv?al=1&market=usa&num_homes=350&region_id={zipcode}&region_type=6"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.text.split("\n")  # CSV rows
    except Exception as e:
        print("[Redfin] Error:", e)

    return []
