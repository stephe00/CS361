import googleapiclient.discovery
import googleapiclient.errors

def main():

    while True:

        videoFunction = open('link-service.txt', 'r+')
        input = videoFunction.readline()
        verify = input[0:10]
        keywords = input[11: len(input) - 1]
        videoFunction.close()

        if verify == "Keywords: ":

            print("Keywords found...")

            api_service_name = "youtube"
            api_version = "v3"
            api_key = "AIzaSyBIiBqvVNia6aUYOhWb9wkvrI5H36UzQNw"
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=api_key)

            request = youtube.search().list(
                part="snippet",
                q=keywords,
                maxResults=5
            )
            response = request.execute()
            video = response['items'][0]
            videoID = video['id']['videoId']

            ytLink = "https://www.youtube.com/watch?v=" + videoID

            videoFunction = open('link-service.txt', 'r+')
            videoFunction.seek(0)
            videoFunction.truncate()
            videoFunction.write(ytLink + "\n")
            videoFunction.close()

if __name__ == "__main__":

    print("YouTube Linker running...")
    main()