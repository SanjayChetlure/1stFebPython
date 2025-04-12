
#Example2:  Multi Level Inheritance

class WhatsAppV1:       #Super class
    def sms(self):
        print("SMS")

class WhatsAppV2(WhatsAppV1):       #Super/Sub class
    def ac(self):
        print("Audio Calling")

    # def sms(self):
    #     print("SMS")

class WhatsAppV3(WhatsAppV2):   #sub class
    def vc(self):
        print("Video Calling")

    # def ac(self):
    #     print("Audio Calling")

    # def sms(self):
    #     print("SMS")


v3=WhatsAppV3()
v3.sms()
v3.ac()
v3.vc()