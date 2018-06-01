class Comment:
    def __init__(self,body,author,timestamp,parentId,c_id):
        self.body=body
        self.c_id=c_id
        self.author=author
        self.timestamp=timestamp
        if(parent!="null"):
            self.type="reply"
            self.parent=parent
         else:
             self.type="comment"
             self.parentId="null"

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
        
    def setParent(self,parentId):
        self.parentId=parentId;
    def getParent(self):
        return parentId;
    def setId(self,c_id):
        self.c_id=c_id;
    def getParent(self):
        return c_id;
