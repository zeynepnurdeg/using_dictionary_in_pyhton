def groups_per_user(group_dictionary):
	user_groups = {}
	for group_name, users in group_dictionary.items():
		for user in users:
			if user in user_groups:
				user_groups[user].append(group_name)
			else:
				user_groups[user] = [group_name]
				
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
