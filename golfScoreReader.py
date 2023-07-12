def main():
    golf_file = open("GolfRecord.txt","r")


    name = golf_file.readline()


    while name != '':
        score = golf_file.readline()

        name = name.rstrip('\n')
        score = score.rstrip('\n')

        print(f"Name: {name}")
        print(f"Score: {score}")
        print()

        name = golf_file.readline()

    golf_file.close()


main()