from matplotlib import pyplot as plt
from datetime import  datetime
class User:
    def __init__(self, idd):
        self.idd = idd
        self.reading = []
        self.consumed = [0]

    def add_initial_reading(self, data):
        self.reading.append(data)
        # diff = (data - self.reading[-2])
        # self.consumed.append(diff)
        return True

    def show_consumed(self):
        print(self.consumed)
        return True

    def show_read(self):
        print(self.reading)
        return True



class Society:
    members = {}

    def __init__(self, name):
        self.name = name

    def add_user(self, user, inread):
        if isinstance(user, User):
            user.add_initial_reading(inread)

            self.members[user.idd] = [user.reading, user.consumed]
            return True
        else:
            return False


    def add_reading(self, user, newread):
        if isinstance(user, User) and user.idd in self.members:
            last_read = int(user.reading[-1])
            diffs = (newread - last_read)
            user.reading.append(newread)
            user.consumed.append(diffs)
            self.members[user.idd] = [user.reading, user.consumed]
            return True

        else:
            return False
    def add_read_list(self,user, listred ):
        if isinstance(user, User) and user.idd in self.members:
            for i in listred:
                diff = i - user.reading[-1]
                user.consumed.append(diff)
                user.reading.append(i)
                self.members[user.idd] = [user.reading, user.consumed]
            return True

    def avg_of_soc(self, day):
        all = []
        for value in self.members.values():
            if len(value[1]) > 1:
                all.append(value[1][day])
                x = sum(all)/len(all)
        return x

    def prnt_mem(self):
        print(self.members)
#


A = User('A')
B = User('B')
curr_day = 2

reda = [324,345,456,654,764,875]
redb = [49,94,107,148,302,482]
soc = Society('ram')
soc.add_user(A, 300)
soc.add_user(B, 34)
# soc.add_reading(A, 324)
# soc.add_reading(B,49)
soc.add_read_list(A, reda)
soc.add_read_list(B, redb)
soc.prnt_mem()
y_avgval = [0]
for i in range(len(reda)):
    y_avgval.append(soc.avg_of_soc(i))
yav = y_avgval

x_dates = [0,1,2,3,4,5,6]
y_aval = A.consumed
y_bval = B.consumed

plt.plot(x_dates, y_aval, label='user A')


plt.plot(x_dates, y_bval, label='user B')

plt.plot(x_dates, yav, label='averg')
plt.style.use('seaborn-pastel')
print(plt.style.available)
plt.legend()

plt.show()



