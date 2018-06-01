import store

class operations(store):

    #Edit Comment
    def edit_comment(self,user,comment):
        if "admin"==user.role:
            for int i=0;i<len(comments;i++):
                if comments[i]['id'] = comment['id']:
                    comment[i]=comment
                    print "You have Succesfully edited the comment."
                else:
                    print "The comment you selected doesnt Exist"
        else:
            print "You are not authorized to edit this comment"

    #Delete Comment
    def delete_comment(self,user,comment):
        if "admin"==user.role or "moderator"==user.role:
            for int i=0;i<len(comments;i++):
                if comments[i]['id'] = comment['id']:
                    del comments[i]
                    print "You have Succesfully deleted the comment."
                else:
                    print "The comment you selected doesnt Exist"
        else:
            print "You are not authorized to edit this comment"

    #Create Comment
    def create_comment(self,comment):
        comments.append(comment)

    def get_comment_by_id(self,id):
        for int i=0;i<len(comments;i++):
            if comments[i]['id'] = comment['id']:
                return comment[i]
        print "The comment you selected doesnt Exist"
            return None

