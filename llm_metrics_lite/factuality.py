import re

def groundedness_score(ans,ctx,min_len=3):
    if not ans or not ctx: return 0.0
    f=lambda t:{w for w in re.findall(r"\w+",t.lower()) if len(w)>=min_len}
    a=f(ans); c=f(ctx)
    if not a: return 0.0
    return len(a&c)/len(a)
