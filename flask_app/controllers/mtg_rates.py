import http.client
import requests
import json
import random 


headers = {
        'X-RapidAPI-Key': "119aab99ecmsh1807def65680d70p14a4aajsn91d6ccee1503",
        'X-RapidAPI-Host': "realty-in-us.p.rapidapi.com"
    }
conn = http.client.HTTPSConnection("realty-in-us.p.rapidapi.com")
conn.request("GET", "/mortgage/v2/check-rates?postal_code=94538", headers=headers)




url = "https://realty-in-us.p.rapidapi.com/mortgage/v2/check-rates"
querystring = {"postal_code":"90004"}

response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.post(url=url, data=response, headers={'Connection':'close'})

res = conn.getresponse()
rates_data = res.read()


parse_json_rates = json.loads(rates_data)
avg_rate = parse_json_rates['data']['loan_analysis']['market']['mortgage_data']['average_rates'][0]['rate']


zip_codes =  [64036, 42349, 80046, 28138, 30260, 46312, 99124, 43219, 27909, 47865, 57752, 45672, 23412, 89705, 94538, 37229, 12584, 79401, 90039, 80206, 12257, 
42762, 81046, 98837, 33981, 55110, 23952, 48381, 53003, 33127, 75372, 40618, 95894, 67762, 58779, 20233, 16410, 11715, 59074, 28105, 15676, 95836, 28166, 41093,
28232, 30306, 93950, 41001, 72583, 58735, 27377, 87323, 40285, 98577, 34293, 38066, 43333, 24993, 30276, 15865, 57629, 73301, 94938, 84656, 27106, 14683, 76856, 
19074, 92376, 38391, 49017, 10011, 37219, 72031, 58278, 97914, 20011, 72802, 56340, 97042, 43347, 12967, 90012, 73045, 94945, 66416, 58795, 62035, 40160, 97731, 
76028, 65250, 60974, 38668, 36135, 32607, 21201, 44809, 30439, 96121]

def get_random_zip():
    rndm_zip = random.choice(zip_codes)
    return rndm_zip




url = "https://realty-in-us.p.rapidapi.com/properties/list-for-sale"

querystring = {"state_code":"WA","city":"Seattle City","offset":"0","limit":"200","sort":"relevance"}

response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.post(url=url, data=res, headers={'Connection':'close'})

def get_featured_homes():
    zip = get_random_zip()
    conn.request("GET", "/properties/list-for-sale?state_code=_&city=_&offset=0&limit=24&postal_code=" + str(zip) +"&sort=relevance&radius=50", headers=headers)
    res = conn.getresponse()
    data = res.read()
    parse_json = json.loads(data)
    featured_homes = parse_json['listings']
    return featured_homes



