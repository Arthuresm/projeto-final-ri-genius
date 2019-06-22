import matplotlib.pyplot as plt
import nltk

from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud

stops = stopwords.words('portuguese')
mapa_cores = ListedColormap(['orange', 'red', 'magenta'])
nuvem = WordCloud(background_color = 'white',
                    colormap = mapa_cores,
                    stopwords = stops,
                    max_words = 100)

nuvem.generate("vale das virtudes é nós no pente já era boyzão cê sabe como é o bagulho tá doido cê tem um qualquer mãe e irmão, irmã e sobrinho se o dinheiro constar eu não gasto sozinho ei camarada a cara é correr a quebrada é sofrida, eu também fazer o que dinheiro no bolso deus no coração família unida champanhe pros irmão amor pela mãe, ocupa o meu tempo um coração puro quanto mundo enfermo não há nada na vida que o amor não supere o mundão desandou, ei você não se entrege olha ao seu redor a expansão do terror apocalipse já que o profeta pregou")
nuvem.to_file("first_review.png")
plt.imshow(nuvem)