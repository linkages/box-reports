
def reportGB(usage):
    for user in usage:
        asize = usage[user] / 1024 / 1024
        roundedSize = round(asize, 3)
        print(f'{user}: {roundedSize} GB')


def reportTB(usage):
    for user in usage:
        asize = usage[user] / 1024 / 1024 / 1024
        roundedSize = round(asize, 3)
        print(f'{user}: {roundedSize} TB')
