import requests


def post_request():
    with requests.Session() as c:
        url = 'https://jsonplaceholder.typicode.com/posts'  # this is url wher server is running
        data = {
            "userId": 1,
            "id": 101,
            "title": "Title is change by post request",
            "body": "minus omnis soluta quia\nqui sed adipisci voluptates illum ipsam voluptatem\neligendi officia ut in\neos soluta similique molestias praesentium blanditiis"
        }  # this is the data we want to change on server
        """
        the below overall_data contain all data receive from get request to specified URL 
        """
        overall_data = c.get(
            url=str(url + "/1"))  # this is the data we receive from server before modificatioin /uploading
        print("Data receive from URL is given below before post request \n" + overall_data.text)

        '''
        The below method will post the data to url in JSON format 
        '''

        updated_data = c.post(url=url,
                              data=data)  # here we will update data by using post request and retun updated data
        print("Data receive from URL is given below after post request \n" + updated_data.text)


if __name__ == "__main__":
    try:
        post_request()
    except ConnectionError:
        print("DVWA service is not running")
    except:
        print("DVWA service is not running")

"""
This method send the post request to Local host with payload of credentials and url is /dvwa/login.php

def post_request():
    with requests.Session() as c:
        token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
        payload['user_token'] = token

        p = c.post('https://127.0.0.1/dvwa/login.php', data=payload)
        r = c.get('http://127.0.0.1/dvwa/vulnerabilities/exec')

"""
