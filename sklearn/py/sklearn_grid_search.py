from sklearn.model_selection import GridSearchCV

# selecionar os parametros
parameters = {'kernel':['poly', 'rbf'],'C':[0.1, 1, 10]}

# criar um pontuador
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score scorer = make_scorer(f1_score)

# Criar um objeto GridSearch com os parâmetros e o pontuador
grid_obj = GridSearchCV(clf, parameters, scoring = scorer)

# Faça o ajuste dos dados
grid_fit = grid_obj.fit(X, y)

# Obter o melhor estimador
best_clf = grid_fit.best_estimator_
