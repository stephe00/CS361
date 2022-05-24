import time

def userDisplay():

    while True:
        userAnswer = input("Enter 'yes' to get a link to a video or 'no' to quit: ")

        if userAnswer == "yes":
            grabLink = open('link-service.txt', 'r+')
            grabLink.seek(0)
            grabLink.truncate()
            userSearch = input("Enter your search keywords: ")
            grabLink.write("Keywords: " + userSearch + "\n")
            grabLink.close()

            time.sleep(10)

            grabLink = open('link-service.txt', 'r+')
            ytLink = grabLink.read()
            grabLink.close()

            print(ytLink)

        elif userAnswer == "no":
            return

        else:
            print("unknown option")


if __name__ == '__main__':

    print("UI Program Running...")
    userDisplay()