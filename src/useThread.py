# thread class for calling network  asnyc fucntion
class async_Thread(TD.Thread):
    def __init__(self, message):
        TD.Thread.__init__(self)
        self.message = message

    def run(self):
        asyncio.run(self.message)




#this thread subclass fetch unverified student information
#run on the background
class dameon_Trhead(TD.Thread):

    def __init__(self, message=None,controller=None):
        TD.Thread.__init__(self)
        self.message = message
        self.controller=controller

    def run(self) -> None:
        if self.message:
            time.sleep(1)
            asyncio.run(self.message)
