from fastapi import APIRouter, status


podcast_router = APIRouter()




@podcast_router.post(path="/api/v1/list", summary="Podcast list", response_model="", status_code=status.HTTP_200_OK)
async def podcast_list():
    pass



@podcast_router.post(path="/api/v1/episodes", summary="Podcast episode list", response_model="", status_code=status.HTTP_200_OK)
async def podcast_episode_list():
    pass



@podcast_router.post(path="/api/v1/liked", summary="Liked Podcasts list", response_model="", status_code=status.HTTP_200_OK)
async def liked_podcast_list():
    pass



@podcast_router.post(path="/api/v1/bookmarked", summary="Bookearked Podcast list", response_model="", status_code=status.HTTP_200_OK)
async def bookmarked_podcast_list():
    pass



@podcast_router.post(path="/api/v1/subscribed", summary="Subscribed Podcast list", response_model="", status_code=status.HTTP_200_OK)
async def subscribed_podcast_list():
    pass



@podcast_router.post(path="/api/v1/comments", summary="Comments list", response_model="", status_code=status.HTTP_200_OK)
async def comments_list():
    pass