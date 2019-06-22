import lyricsgenius as genius
api = genius.Genius('BbtnBP88nVVVisOYwwKCX7YtTLAkdxHODod76yw8HLkwGM-kXPk124_ZlKj_7I1T')
artist = api.search_artist('Racionais-mcs')
lyrics = artist.save_lyrics()

from glob import glob
import json
from pandas.io.json import json_normalize

lyrics = []
for f_name in glob('./*.json'):
    config = json.loads(open(f_name).read())
    lyrics.append(config)

df = pd.DataFrame(lyrics)
df.drop(['tracks','artist','audio_features' ], axis=1, inplace = True)
df = df.dropna()
df['title'] = df['songs'].apply(lambda x : x[0]['title'])
df['album'] = df['songs'].apply(lambda x : x[0]['album'])
df['lyrics'] = df['songs'].apply(lambda x : x[0]['lyrics'].lower())
df.drop(['songs'], axis = 1, inplace = True)
df.head()