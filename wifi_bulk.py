import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

docs = []

# for i in range(1,21):
for i in range(1, 2):
    iStart = (i - 1) * 1000 + 1
    iEnd = i * 1000
    url = (
        "http://openapi.seoul.go.kr:8088/5a6e69665a64646f353578416e4359/xml/TbPublicWifiInfo/"
        + str(iStart)
        + "/"
        + str(iEnd)
        + "/"
    )

    response = urllib.request.urlopen(url)
    xml_str = response.read().decode("utf-8")
    tree = ElementTree(fromstring(xml_str))
    root = tree.getroot()

    for row in root.iter("row"):
        gu_nm = row.find("X_SWIFI_WRDOFC").text
        place_nm = row.find("X_SWIFI_MAIN_NM").text
        place_x = float(row.find("LAT").text)
        place_y = float(row.find("LNT").text)
        doc = {
            "_index": "seoul_wifi2",
            "_source": {
                "gu_nm": gu_nm,
                "place_nm": place_nm,
                "instl_xy": {
                    "_type": "geo_point",
                    "lat": float(row.find("LAT").text),
                    "lot": float(row.find("LNT").text),
                },
            },
        }
    docs.append(doc)
    print("END", iStart, "~", iEnd)
    print(docs)
# print("END", iStart, "~", iEnd)
res = helpers.bulk(es, docs)
print("END")
