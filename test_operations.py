import unittest
from operations import Operations
from allusers import User
from comments import Comment
class TestOperation(unittest.TestCase):

    def setup(self):
        self.user=User("wolves@gmail.com","password","admin")
        self.comment =Comment("that is amazing","wolves@gmail.com","2-06-2018","2")
        self.comment1 =Comment("You are cool!","wolves@gmail.com","2-06-2018","2")
        self.operation =Operations("self.user","self.comment")

    def test_create_comment_works(self):
        
        res = self.operation.create_comment(self.user,self.comment)
        self.assertEqual(res,"True")
        
    def test_delete_acomment(self):
        self.operation.create_comment(self.user,self.comment)
        result =self.operation.delete(self.user,self.comment)
        self.assertEqual(result,True)

    def test_edit_comment(self):
        self.operation.create_comment(self.user,self.comment)
        res = self.operation.edit(self.coment,self.comment1)
    def test_reply(self):
        res = self.reply(self.user,self.comment)
