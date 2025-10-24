current_users = ['Chenyi', 'Nayina', 'Wanyanhuide', 'Laoba', 'Captin']
new_users = ['Bob', 'Chenyi', 'nayina', 'Andy', 'Laoba']

current_users_lower = [current_user.lower() for current_user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print('please print another user name')
	else:
		print('welcome!')