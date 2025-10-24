unconfirmed_users = ['Alice', 'Bob', 'Cici']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('confirming unconfirmed users:' + current_users)

    confirmed_users.append(current_users)

for confirmed_user in confirmed_users:
    print(confirmed_user)