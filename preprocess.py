import os, json
import pandas as pd
import re
import os


def execute():
    lyrics = readJsonLyrics()
    saveLyricsText(lyrics)


def proccesLyrics(lyric):
    return re.sub(r'\[.*\]', '', lyric.lower())


def readJsonLyrics():
    path_to_json = 'dataset/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    lyrics = []
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            lyrics.append(proccesLyrics(json_text['songs'][0]['lyrics']))

    return lyrics


def saveLyricsText(lyrics):
    with open('lyricsText.txt', 'w', encoding="utf-8") as filehandle:
        for listitem in lyrics:
            filehandle.write('%s\n' % listitem)


execute()