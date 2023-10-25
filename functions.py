
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

def reportTotals(usage):
    for action in usage:
        print(f"{action}: ")
        for user in usage[action]:
            total = 0
            # print(f"\tUser: {user}: ")
            for item in usage[action][user]:
                total = total + item['Size']

            if total > 10 ** 6 and total < 10 ** 9:
                print(f"\t{user}: {total / 1024 / 1024} GB")
            elif total > 10 ** 9:
                print(f"\t{user}: {total / 1024 / 1024 / 1024} TB")
            else:
                print(f"\t{user}: {total} KB")
        print()

def report(usage):
    for action in usage:
        print(f"{action}: ")
        for user in usage[action]:
            total = 0
            print(f"\tUser: {user}: ")

            for day in usage[action][user]:
                size = usage[action][user][day]
                total = total + size
                if size > 10 ** 6 and size < 10 ** 9:
                    print(f"\t\t{day}: {size / 1024 / 1024} GB")
                elif size > 10 ** 9:
                    print(f"\t\t{day}: {size / 1024 / 1024 / 1024} TB")
                else:
                    print(f"\t\t{day}: {size} KB")

            if total > 10 ** 6 and size < 10 ** 9:
                print(f"\t\tTotal: {total / 1024 / 1024} GB\n")
            elif total > 10 ** 9:
                print(f"\t\tTotal: {total / 1024 / 1024 / 1024} TB\n")
            else:
                print(f"\t\tTotal: {total} KB\n")
        print()
