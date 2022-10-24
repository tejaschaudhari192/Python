class Account:
    def __init__(self, uname, folls, follg):
        self.uname = uname
        self.followers = folls
        self.following = follg

    def follow(self, user):
        user.followers += 1
        self.following += 1


p1 = Account('person 1', 90, 78)
p2 = Account('person 2', 50, 36)

print('Before follows')
print('Following of person 1 :', p1.followers)
print('Followers of person 1 :', p1.following)

print('Followers of person 2 :', p2.followers)
print('Following of person 2 :', p2.following)
p1.follow(p2)
print('After follows')


print('Following of person 1 :', p1.followers)
print('Followers of person 1 :', p1.following)

print('Followers of person 2 :', p2.followers)
print('Following of person 2 :', p2.following)
