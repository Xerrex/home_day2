import requests
def iss_info(lattitude,longitude):
    """
    the function return the passing of the
     International space station at current location as per this cooordinates
    :param lattitude: of curent location
    :param longitude: of current location
    :return: dictionary of iss details as per the passed coordinaates

    nairobi :1.2921° S, 36.8219° E
    mombasa :4.0435° S, 39.6682° E
    kisumu  :0.0917° S, 34.7680° E
    thika   : 1.0388° S, 37.0834° E
    busia   :0.4608° N, 34.1115° E
    kampala :0.3476° N, 32.5825° E
    Dar-es-salam    :6.7924° S, 39.2083° E

    """


    base_url1="http://api.open-notify.org/iss-now.json"
    base_url2="http: // api.open - notify.org/iss - now.json"
def iss_now():
    """
    this function returns details  of the International Space Station
    :return:
    """
    base_url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(base_url)
    data =response.json()

    print(response.json())


iss_now()