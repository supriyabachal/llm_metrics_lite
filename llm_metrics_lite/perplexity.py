from collections import defaultdict
import math

def train_char_ngram_model(texts,n=3):
    m=defaultdict(lambda:defaultdict(int))
    for t in texts:
        if len(t)<n: continue
        for i in range(len(t)-n+1):
            p=t[i:i+n-1]; c=t[i+n-1]
            m[p][c]+=1
    return m

def ngram_perplexity(text,model,n=3,smoothing=1.0):
    if len(text)<n: return float("inf")
    lp=0; ct=0
    for i in range(len(text)-n+1):
        p=text[i:i+n-1]; c=text[i+n-1]
        if p not in model: continue
        counts=model[p]; total=sum(counts.values())
        prob=(counts.get(c,0)+smoothing)/(total+smoothing*len(counts))
        lp+=math.log(prob); ct+=1
    if not ct: return float("inf")
    return math.exp(-lp/ct)
