class Features:
    def __init__(self):
        self.sender_email = ""
        self.reciever_email =""
        self.sender_org = ""
        self.reciever_org = ""
        self.body = ""
        self.date = ""
        self.message_id=""
        self.summarisedBody = ""

    def __str__(self):
        return f"{self.date}\n,{self.body}\n,{self.reciever_org}\n,{self.sender_org}\n,{self.reciever_email}\n,{self.sender_email}\n"
