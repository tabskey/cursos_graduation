from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB

# Treinos de dados_treino [altura,peso, numeração de sapato]
dados_treino = [[191, 90, 43], [182, 70, 43], [152, 60, 34], [154, 84, 37], [166, 65, 40], [190, 90, 45], [175, 64, 39],[177, 70, 40], [157, 43,33], [176, 75, 41], [183, 85, 43],[177, 70, 37],[182, 82, 39]]

generos_treino = ['Masculino', 'Masculino', 'Feminino', 'Feminino', 'Masculino', 'Masculino', 'Feminino', 'Feminino', 'Feminino', 'Masculino', 'Masculino', 'Feminino', 'Feminino']

#Classificadores escolhidos
clf = tree.DecisionTreeClassifier()
clf1 = svm.SVC()
clf2 = neighbors.KNeighborsClassifier()
clf3 = GaussianNB()

#Modelo de Treinamento
clf = clf.fit(dados_treino,generos_treino)
clf1 = clf1.fit(dados_treino,generos_treino)
clf2 = clf2.fit(dados_treino,generos_treino)
clf3 = clf3.fit(dados_treino,generos_treino)

dados = [[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[192,80,42],[180,92,43], [172, 92, 38]]
generos = ['Masculino','Masculino','Masculino','Feminino','Feminino','Feminino','Masculino','Masculino', 'Feminino']

#Previsões feitas
previsao = clf.predict(dados)
previsao1 = clf1.predict(dados)
previsao2 = clf2.predict(dados)
previsao3 = clf3.predict(dados)

#Resultado 
r1 = accuracy_score(generos,previsao1) * 100
r2 = accuracy_score(generos,previsao2) * 100
r3 = accuracy_score(generos,previsao3) * 100

#print best result
if r1 > r2 and r1 > r3:
	print("O melhor modelo é SVM com ", r1)
elif r2 > r3 and r2 > r1:
	print("O melhor modelo é KNeighborsClassifier com ", r2)
else :
	print("O melhor modelo é Naive com ",r3)


