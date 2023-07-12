def main():
    num_rec = int(input("How many records do you want to make? "))
    golf_file = open("GolfRecord.txt", "w")

    for count in range(1, num_rec+1):
        print(f"Enter data for golfer #{count}")
        name = input("Name: ")
        golf_score = input("Golf score: ")

        golf_file.write(f'{name}\n')
        golf_file.write(f'{golf_score}\n')
        print()

    golf_file.close()
    print("Golf scores recorded in GolfRecord.txt")

main()

