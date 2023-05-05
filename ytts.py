# IMPORTS


# OUR UTILITIES

# Scraping
from scraping.ids import get_random_videos, get_search_videos, get_trending_videos 
from scraping.thumbnails import get_thumbnails

# Utilities
from utilities.formatting import remove_bars, detect_type, convert
from utilities.loading import key

if __name__ == "__main__":
    
    # Print out API key for the world to see
    print(key('api.key'))
