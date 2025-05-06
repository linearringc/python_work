def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)
    return profile

build_profile('bob', 'Hoffmann', location = 'hamburg', age = '71')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(build_profile('bob', 'Hoffmann', location = 'hamburg', age = '71'))