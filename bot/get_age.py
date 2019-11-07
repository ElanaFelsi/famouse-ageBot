import requests


def get_age(name: str):
    try:
        url = "https://en.wikipedia.org/wiki/" + name
        r = requests.get(url)
        if(r==200)
        age = r.text.split("age&#160;")[1].split(")")[0]
    except:
        return 


    return age


#get_age("Donald_Trump")