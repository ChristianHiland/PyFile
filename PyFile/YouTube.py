#!/usr/bin/env python
import pytube
from youtube_transcript_api import YouTubeTranscriptApi

def Video(link, lists):
    if lists == True:
        with open("link.txt", "r") as links:
            if links.read() == str("Add a Link"):
                print("User needs to add some links to the link.txt file to continue.")
            else:
                for i in links:
                    yt = pytube.YouTube(i)
                    print("Title:", yt.title)
                    print("Author", yt.author)
                    print("Length:", yt.length)
                    yt.streams.get_highest_resolution().download()
                    print("Video successfullly downloaded from", i + "\n")
                    links.close()
                with open("link.txt", "w") as links:
                    links.write("Add a Link")
    else:
        yt = pytube.YouTube(link)
        print("Title:", yt.title)
        print("Author", yt.author)
        print("Length:", yt.length)
        yt.streams.get_highest_resolution().download()
        print("Video successfullly downloaded from", i + "\n")
        links.close()
        with open("link.txt", "w") as links:
            links.write("Add a Link")
    return

def Subtitles(link, lists):
    if lists == True:
        with open("link.txt", "r") as links:
        for i in links:
            # of dictionaries obtained by the get_transcript() function
            srt = YouTubeTranscriptApi.get_transcript(i)
            yt = pytube.Youtube(i)
            file = str(yt.title() + ".txt")
            with open(file, "w") as sub:
                for t in srt:
                    sub.write("{}\n".format(t))
    elif lists == False:
        srt = YouTubeTranscriptApi.get_transcript(link)
        yt = pytube.Youtube(link)
        file = str(yt.title() + ".txt")
        with open(file, "w") as sub:
            for t in srt:
                sub.write("{}\n".format(t))
    else:
        print("error")
    return

