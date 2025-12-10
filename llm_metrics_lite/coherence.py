import re,math

def coherence_score(text):
    if not text: return 0.0
    s=re.split(r"(?<=[.!?])\s+",text)
    s=[x.strip() for x in s if x.strip()]
    if len(s)<2: return 1.0
    vec=lambda sent: {w:1 for w in re.findall(r"\w+",sent.lower())}
    sims=[]
    for a,b in zip(s,s[1:]):
        v1,v2=vec(a),vec(b)
        dot=sum(v1.get(k,0)*v2.get(k,0) for k in v1.keys()&v2.keys())
        n1=math.sqrt(len(v1));n2=math.sqrt(len(v2))
        sims.append(dot/(n1*n2) if n1 and n2 else 0)
    return max(0,min(1,sum(sims)/len(sims)))
