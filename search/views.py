from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import generics
from ytmusicapi import YTMusic

# Create your views here.
from .API import multiSearch


class MultiSearchAPI(generics.RetrieveAPIView):
    '''Get the reviews for a movie'''


    def format_results(results): 
        pass

    def get_queryset(self):
        query = self.request.query_params.get('query')
        page = self.request.query_params.get('page') or 1
        return multiSearch(query=query, page=page)

    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)





@api_view(["GET"])
def search_songs(request):
    query = request.GET.get("q", "")
    if not query:
        return Response({"error": "Query parameter is required"}, status=400)

    try:
        ytmusic = YTMusic()
        results = ytmusic.search(query)

        

        songs = [
            {"video_id": item["videoId"], "title": f'{item["artists"][0]["name"]} - {item["title"]}', "duration": item["duration"], "thumbnail": item["thumbnails"][0]["url"]}
            for item in results
            if item["resultType"] == "song" or (item["resultType"] == "video" and not item["category" ] == "Episodes")
        ]

        return Response(songs)
    except Exception as e:
        return Response({"error": str(e)}, status=500)