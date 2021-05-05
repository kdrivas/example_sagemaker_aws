from sagemaker.serializers import CSVSerializer
from urllib import request

base_url='http://localhost:8080'
csv_serializer = CSVSerializer()
payloads = [
    [4.6, 3.1, 1.5, 0.2], # 0
    [7.7, 2.6, 6.9, 2.3], # 2
    [6.1, 2.8, 4.7, 1.2]  # 1
]

def predict(payload):
    headers = {
        'Content-type': 'text/csv',
        'Accept': 'text/csv'
    }
    
    req = request.Request("%s/invocations" % base_url, data=csv_serializer.serialize(payload).encode('utf-8'), headers=headers)
    resp = request.urlopen(req)
    print("Response code: %d, Prediction: %s\n" % (resp.getcode(), resp.read()))
    for i in resp.headers:
        print(i, resp.headers[i])

for p in payloads:
    predict(p)