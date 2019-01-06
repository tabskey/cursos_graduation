import tweetpy
import textblob 
#Procurei suporte para a linguagem portuguesa/brasileira mas até dado momento de acordo com o site oficial, não tinha atualizações sobre o assunto.



# Autenticação padrão
consumer_key= 'ULo8IJhnndyNQ0Ns1BegIt3ro '
consumer_secret= 'gWyVXCvEUJrEQsv14f1J45sYrx92SWy0MtMkchj5atsdIrcMU0 '

access_token='ULo8IJhnndyNQ0Ns1BegIt3ro '
access_token_secret='gWyVXCvEUJrEQsv14f1J45sYrx92SWy0MtMkchj5atsdIrcMU0 '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Adiciona a devida target e salva 
start_date = '2019-01-01'
end_date = '2019-01-05'

tweets = api.search('Anime', count = 150, since= start_date, until= end_date)

with open(caminho, 'wb') as arquivoCSV:
    for tweet in tweets:
       analysis = TextBlob(tweet.text)
       linha = tweet.text + get_label(analysis)
       arquivoCSV.write(linha.encode('utf-8'))       


