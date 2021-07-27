import Adafruit_DHT


class DHT22:
    def __init__(self):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 4

    def set_formater(self, formater):
        self.formater = formater

    def get_dht(self):
        return Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)

