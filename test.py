import GueseTool as gt
import numpy as np

X = [1,4,2,4,6,3,2,21,4,5]

print "MW: ",gt.mean(X),np.mean(X)
print "Median: ",gt.median(X),np.median(X)
print "Variance: ",gt.var(X), np.var(X)
print "Standartabw: ",gt.std(X),np.std(X)

gt.circle([50,60],["Gelesen","Kommend"],"Deine Mudda")
