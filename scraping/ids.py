"""
Get ids from a variety of sources

Functions
----------
get_random_videos:
get_trending_videos:
get_search_videos:

"""

import json
import urllib.request
import string
import random

def get_random_videos(
        count = 50,
        API_KEY = 'your_key',
        debug = True
    ):
    """
    Gets random youtube video

    Parameters
    ----------
    count: number of videos to return
    API_KEY: yout YouTube API KEY
    debug: whether to print out results
    
    Return
    ----------
    returns YouTube videos
    """
    
    rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,rand)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    video_ids = []
    for data in results['items']:
        videoId = (data['id']['videoId'])
        if debug:
            print(videoId)
        video_ids.append(videoId)
    
    return video_ids

def get_trending_videos(
        count:int = 50,
        API_KEY:str = 'your_key',
        debug:bool = True,
        category_ID = True,
        pagetoken = False
    ):
    """
    Get IDs of trending videos

    Parameters
    ----------
    count: number of ids to return, 200 max, 50 min. 
    API_KEY: your api key
    debug: whether or not to run in debug mode
    category_ID: category to scrape
    pagetoken: whether this is a continuation of a previous pull or not
    
    Return
    ----------
    Returns list of ids in string format
    """
    
    apilink = "https://youtube.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxHeight=8192&maxResults="+str(count)+"&key="+API_KEY +("" if pagetoken == "None" else ("&pageToken="+pagetoken))
    if category_ID:
        # FOR CATEGORY SPECIFIC: &videoCategoryId=20
        apilink+="&videoCategoryId="+category_ID
    
    #TODO use api link to get video ids

    return

def get_search_videos(
        count = 50,
        API_KEY = 'your_key',
        debug = True
    ):
    
    #TODO
    
    return