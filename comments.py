class comment:
    def __init__(self,body,author,timestamp,parent):
        self.body=body
        self.author=author
        self.timestamp=timestamp
        if(parent!="null"):
            self.type="reply"
            self.parent=parent
         else:
             self.type="comment"
             self.parent="null"

    def getBody(self):
        return self.body;
    def getAuthor(self):
        return self.author;
    def getTimestamp(self):
        return self.timestamp;
    def setBody(self,body):
        self.body=body;
    def setAuthor(self,author):
        self.author=author;
    def setTimestamp(self,timestamp):
        self.timestamp=timestamp;
        
        

