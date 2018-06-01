
class operations():
    users = []
    comments =[]
    #Edit Commenti
    def edit_comment(self,user,comment):
        if "admin"==user.role:
            i=0
            for com in comments:
                if com['id'] == comment['id']:
                    comments[i]=comment
                    return "You have Succesfully edited the comment."
                else:
                    return "The comment you selected doesnt Exist"
        else:
            return "You are not authorized to edit this comment"

    #Delete Comment
    def delete_comment(self,user,comment):
        if "admin"==user.role or "moderator"==user.role:
            i=0
            for com in comments:
                if com['id'] == comment['id']:
                    del comments[i]
                    return "You have Succesfully deleted the comment."
                else:
                    return "The comment you selected doesnt Exist"
        else:
            return "You are not authorized to edit this comment"

    #Create Comment
    def create_comment(self,comment):
        comments.append(comment)

    def get_comment_by_id(self,id):
        i=0
        for com in comments:
            if com['id'] == comment['id']:
                return comments[i]
        return None

