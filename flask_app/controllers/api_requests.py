import http.client
import json
from flask_app.controllers.rand_zips import get_random_zip


headers = {
        'X-RapidAPI-Key': "119aab99ecmsh1807def65680d70p14a4aajsn91d6ccee1503",
        'X-RapidAPI-Host': "realty-in-us.p.rapidapi.com"
    }
conn = http.client.HTTPSConnection("realty-in-us.p.rapidapi.com")


def get_featured_homes():
    zip = get_random_zip()
    conn.request("GET", "/properties/list-for-sale?state_code=_&city=_&offset=0&limit=20&postal_code=" + str(zip) +"&sort=relevance&radius=50", headers=headers)
    res = conn.getresponse()
    data = res.read()
    parse_json = json.loads(data)
    featured_homes = parse_json['listings']
    return featured_homes

# print ("***********GET FEATURED HOMES*************", get_featured_homes())


