import os
import googleapiclient.discovery
from dotenv import dotenv_values

config = dotenv_values(".env")


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = config['api_key']

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId="6YZvp2GwT0A",
        maxResults=100
    )
    response = request.execute()

    for cle, valeur in response.items():
        print(f'{cle} : {valeur}')

    youtube.close()


if __name__ == "__main__":
    main()
