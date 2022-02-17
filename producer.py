from confluent_kafka import Producer
import json

def startpy():

    data = {
        "apple":"an day",
        "doctor":"away",
        "docker":"greata"
    }

    serialized_data = json.dumps(data)

    p = Producer({'bootstrap.servers': 'localhost:9091'})

    p.produce('fruit-vendor', key='prash', value=serialized_data)

    print("sent")

    p.flush(30)

if __name__ == '__main__':
    startpy()