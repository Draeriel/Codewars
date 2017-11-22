def areYouPlayingBanjo(name):
    while name[0] == 'r' or name[0] == 'R':
        return name + ' plays banjo'
        break
    while name[0] != 'r' or name[0] != 'R':
        return name + ' does not play banjo'
        break