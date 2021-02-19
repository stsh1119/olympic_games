def convert_medal(medal):
    if medal == 'Gold':
        medal = 1
    elif medal == 'Silver':
        medal = 2
    elif medal == 'Bronze':
        medal = 3
    else:
        medal = 0

    return medal
