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

def eventReport(usage):
    for action in usage:
        print(f"{action}: ")
        for user in usage[action]:
            total = 0
            print(f"\tUser: {user}: ")

            for day in usage[action][user]:
                size = usage[action][user][day]
                total = total + size

                if size < 10 ** 9:
                    print(f"\t\t{day}: {size / 1024 / 1024} MB")
                elif size < 10 ** 12:
                    print(f"\t\t{day}: {size / 1024 / 1024 / 1024} GB")
                elif size < 10 ** 15:
                    print(f"\t\t{day}: {size / 1024 / 1024 / 1024 / 1024} TB")
                else:
                    print(f"\t\t{day}: {size} B")

            if total < 10 ** 9:
                print(f"\t\tTotal: {total / 1024 / 1024} MB\n")
            elif total < 10 ** 12:
                print(f"\t\tTotal: {total / 1024 / 1024 / 1024 } GB\n")
            elif total < 10 ** 15:
                print(f"\t\tTotal: {total / 1024 / 1024 / 1024 / 1024} TB\n")
            elif total < 10 ** 18:
                print(f"\t\tTotal: {total / 1024 / 1024 / 1024 / 1024 / 1024} PB\n")
            else:
                print(f"\t\tTotal: {total} B\n")
            # print(f"\t\tTotal: {total} B\n")
        # print()
