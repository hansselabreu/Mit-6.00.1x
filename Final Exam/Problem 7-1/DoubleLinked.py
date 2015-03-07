class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name



def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    def isEmpty(node):
        return node.getBefore() == None and node.getAfter() == None

    if isEmpty(atMe):
        if atMe.myName() < newFrob.myName():
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
    else:
        if atMe.myName() < newFrob.myName():
            current = atMe
            while current.myName() < newFrob.myName():
                if current.getAfter() == None:
                    break
                so = current.getAfter()
                if so.myName() > newFrob.myName():
                    break
                current = current.getAfter()
                
            if current.getAfter() == None:
                current.setAfter(newFrob)
                newFrob.setBefore(current)
            else:
                temp = current.getAfter()
                current.setAfter(newFrob)
                newFrob.setBefore(current)
                newFrob.setAfter(temp)
                temp.setBefore(newFrob)
        else:
            current = atMe
            while current.myName() > newFrob.myName():
                if current.getBefore() == None:
                    break
                so = current.getBefore()
                if so.myName() < newFrob.myName():
                    break
                current = current.getBefore()
            if current.getBefore() == None:
                current.setBefore(newFrob)
                newFrob.setAfter(current)
            else:
                temp = current.getBefore()
                current.setBefore(newFrob)
                newFrob.setAfter(current)
                newFrob.setBefore(temp)
                temp.setAfter(newFrob)




eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
