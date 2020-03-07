import json
from urllib.request import urlopen
from math import pi, sin, cos, atan2, sqrt, asin, acos

R = 6371.0 # Earth's radius

def getTransmitter():
    """ Download and parse list of DAPNET transmitters. """
    try:
        return json.loads(urlopen("http://www.hampager.de:8080/transmitters").read())
    except Exception:
        return None

def vecProd(x,y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]);

def vecScaleTo(x, r=1.0):
    n = sqrt(x[0]**2 + x[1]**2 + x[2]**2)
    return (r*x[0]/n, r*x[1]/n, r*x[2]/n)

def deg2car(x, r):
    lon, lat = x
    st = sin(pi*(90-lat)/180)
    ct = cos(pi*(90-lat)/180)
    sp = sin(pi*lon/180)
    cp = cos(pi*lon/180)
    return (r*st*cp, r*st*sp, r*ct)

def car2deg(x):
    r = sqrt(x[0]**2 + x[1]**2 + x[2]**2)
    lat = acos(x[2]/r)
    lon = atan2(x[1],x[0])
    return (180*lon/pi, 90-180*lat/pi)

def greatCircleDist(a,b, r):
    pa = pi*(90-a[1])/180; pb = pi*(90-b[1])/180
    dp = pi*(a[1]-b[1])/180; dl = pi*(a[0]-b[0])/180
    return 2*r*asin(sqrt(sin(dp/2)**2 + cos(pa)*cos(pb)*(sin(dl/2)**2)))

def distanceLineSegmentPoint(a, b, p):
    A = deg2car(a, R); B = deg2car(b, R); P = deg2car(p, R)
    G = vecProd(A,B);
    F = vecProd(P,G);
    T = vecProd(G,F);
    T = vecScaleTo(T, R)
    t = car2deg(T)
    return greatCircleDist(p, t, R);

def distancePolyPoint(polygon, point):
    d = greatCircleDist(point, polygon[0], R)
    for i in range(1, len(polygon)):
        tmp = greatCircleDist(polygon[i], point, R)
        if tmp < d: d = tmp
    return d

def pointInPoly(polygon, point):
    return False;

def transmitterNearPoly(polygon, transmitter, max_dist=50):
    point = (float(transmitter["longitude"]), float(transmitter["latitude"]))
    return (distancePolyPoint(polygon, point) < max_dist) or (pointInPoly(polygon, point))

def isWideRange(transmitter):
    return "WIDERANGE" == transmitter["usage"]

def filterTransmitterForMessage(message, transmiters, max_dist=50):
    txs = list()
    for info in message["info"]:
        for area in info["area"]:
            if not "polygon" in area:
                continue;
            for poly in area["polygon"]:
                points = poly.split(" ");
                poly = list(map(lambda p: tuple(map(float, p.split(","))), points))
                txs += filter(isWideRange, filter(lambda t: transmitterNearPoly(poly, t, max_dist), transmiters))
    return txs

if __name__== "__main__":
    # transmitters = getTransmitter()
    transmitters = json.load(open("transmitters", "r"))
    messages     = json.load(open("../test.json", "r"))
    for message in messages:
        txs = filterTransmitterForMessage(message, transmitters)
        print("Sent {0} ({1}) to".format(message["identifier"], message["sender"]))
        for tx in txs:
            print(" => {0} at {1}, {2}".format(tx["name"], tx["longitude"], tx["latitude"]))
