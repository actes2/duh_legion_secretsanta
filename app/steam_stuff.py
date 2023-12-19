import requests

def get_profile_url_from_steamid(steam_id):

    start_str = 'target="_blank"id="go2steamcom">'
    end_str = '</a>'
    base_url = f"https://steamid.io/lookup/{steam_id}/"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.request("GET", base_url, headers=headers).text
    
    response = response.replace(" ", "")


    start_index = response.find(start_str) + len(start_str)
    substr = response[start_index:]
    substr = substr[:substr.find(end_str)]
    return substr

