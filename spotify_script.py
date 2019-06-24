import pandas as pd 
import re 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import json
import lyricsgenius as genius
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud


#Documentacao utilizada
# https://spotipy.readthedocs.io/en/latest/#installation
# https://github.com/johnwmillr/LyricsGenius/tree/master/lyricsgenius



def proccesLyrics(lyric):
    return re.sub(r'\[.*\]', '', lyric.lower())

def create_cloud(first_artist, idioma):
    gen = genius.Genius('__your_api_key__')

    #Client ID contido no dashboard
    cid ="__your_client_id__" 
    #Client Secret contido no dashboard
    secret = "__your_client_secret__" 

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

    results = sp.search("artist: " + first_artist)
    artist_id = results['tracks']['items'][0]['artists'][0]['uri']
    print('Id do artista = ' + artist_id)
    results = sp.artist_top_tracks(artist_id)

    total_lyrics = []
    
    max_musics = 10
    count = 0
    for track in results['tracks']:
        track_name = track['name']
        # print ('track    : ' + track_name)

        #Esse if e necessario pois algumas musicas tem ' - Remastered', ' - Film Version', entao retirei esse trecho
        if ' -' in track_name: 
            track_name = track_name.split(' -')
            track_name = track_name[0]
        
        # print('after processing    :' + track_name)
        music = gen.search_song(track_name, artist=first_artist, get_full_info= True)
        
        if music != None:
            music = music.to_dict()
            music = music['lyrics']
            processed_music = proccesLyrics(music)
            total_lyrics.append(processed_music)
            max_musics -= 1

        else:
            count += 1
            # print('Musica nao encontrada - Aumentando indice')
        print ('\n')
        if(max_musics == 0):
            break;

    
    print('Seriam buscadas ' + str(count + 10))
    
    stops = stopwords.words(idioma)
    mapa_cores = ListedColormap(['orange', 'red', 'magenta', 'yellow', 'blue'])
    nuvem = WordCloud(background_color = 'white',
                        max_font_size=150,
                        colormap = mapa_cores,
                        stopwords = stops,
                        max_words = 1000)

    all_lyrics = ''
    for lyric in total_lyrics: 
        all_lyrics = lyric + '\n'

    nuvem.generate(all_lyrics)
    nuvem.to_file(first_artist + ".png")
    plt.imshow(nuvem)



#Pesquisas realizadas no cifra club 23-06-2019

# MELHORES provavelmente sao as mais acessadas ao longo da historia
# nao as mais populares atualmente

#Melhores do Rock Internacional
create_cloud('The Beatles', 'english')
create_cloud('Queen', 'english')

#Melhores do Rock Nacional
create_cloud('Legião Urbana', 'portuguese')
create_cloud('Charlie Brown Jr.', 'portuguese')

#Melhores do Sertanejo
create_cloud('Bruno e Marrone', 'portuguese')
create_cloud('Gusttavo Lima', 'portuguese')

#Melhores do Pop Internacional
create_cloud('Lady Gaga', 'english')
create_cloud('Ed Sheeran', 'english')