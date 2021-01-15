def profile_(volume, origin, **properties):
    profile = {'volume': volume, 'origin': origin}
    for key, value in properties.items():
        profile[key] = value
    print(profile)
    return profile

js_1 = profile_(10,'Apple',priece = '23 UAN',state = 'pure')