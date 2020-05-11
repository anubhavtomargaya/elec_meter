
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.readings = {}


    def add_rd(self, val,date):
        rd = Reading(val, self.user_id, date)
        self.readings[rd.date]=rd.value


class Reading:
    def __init__(self, value, user_id, date):
        self.date = date
        self.value = value
        self.user_id = user_id
        # self.pday = {}


    def add_here(self):
        if self.date not in self.pday:
            self.pday[self.date] = [self.value]
        else:
            self.pday[self.date].append(self.value)
        print(self.pday)


class Group:
    def __init__(self):
        self.all_reading = {}
        self.users = {}
        self.pday = {}

    def add_users(self,id, name):
        usr = User(id, name)
        self.users[usr.user_id] = usr.name

    def addrd(self, id, val, date):
        rd = Reading(val, id, date)
        self.pday.setdefault(rd.date, []).append(rd.value)

    def all_rd(self):

        if isinstance(user, User):
            self.all_reading[user.name] = user.readings
        else:

            print("user not created")
        return True





#
#     def add_reading(self, date, red):
#         for i in red:
#             readings[self.user_id].append(i)
#         for j in date:
#             readings['date'].append(j)
#         return True
#

# one = User(2, 'bud', 34)
# newred = Reading(3, 40, 2)
# one.add_user()
# two = User(4, 'mins', 54)
# two.add_user()
# print(user)

# print(readings['read']['date'])
# readings['read']= 23
# print(readings)
# one =User(12, 'Golu')
# one.add_user(20, 13)
# print(readings)
# readings['']
# one = User(23, 'tom')
# one.add_rd(200, 1)
# one.add_rd(300,2)
# two = User(24, 'dani')
# two.add_rd(505, 1)
# two.add_rd(903, 2)
# print(one.readings)
ram =Group()
ram.add_users(2,'tom')
ram.add_users(3, 'dani')
print(ram.users)
ram.addrd(2,300,1)
ram.addrd(3, 500,1)
print(ram.pday)
# print(one.pday)
# print(ram.all_reading)
