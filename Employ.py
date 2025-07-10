class Employ:
    def work(self):
        print("work")
class Manager(Employ):
    def manage(self):
        print("manage")
m=Manager()
m.manage()
m.work()

