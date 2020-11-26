import requests

"""
    This method send post request to url 
    https://jsonplaceholder.typicode.com/comments?postId=
    and get specified post data enter by user.
    
"""


def download_data(id):
    with requests.Session() as c:
        url = "https://jsonplaceholder.typicode.com/comments?postId=" + id  # at this url we have multiple posts we just enter post o and the data of that post is downloaded and store in file
        downloaded_data = c.get(url=url)  # this line send the get requset to specified url
        data = str(downloaded_data.text)
        filename = "DownloadedData/dataofpostno" + id + ".txt"
        with open(filename, 'w') as f:
            f.write(data)
            print("Data successfully downloaded and store on file " + filename + " :)")


if __name__ == "__main__":
    id = int(input("Enter the postID between 0-499 you want to download : "))
    download_data(str(id))
