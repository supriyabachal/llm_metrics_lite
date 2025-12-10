from dataclasses import dataclass
from .coherence import coherence_score
from .perplexity import ngram_perplexity
from .factuality import groundedness_score
from .tokens import count_words,count_characters,approximate_token_count

@dataclass
class LLMEvaluationResult:
    coherence:float=None; perplexity:float=None; groundedness:float=None
    word_count:int=None; char_count:int=None; approx_token_count:int=None

def evaluate_output(output_text,context_text=None,perplexity_model=None,perplexity_n=3):
    r=LLMEvaluationResult()
    r.coherence=coherence_score(output_text)
    if perplexity_model: r.perplexity=ngram_perplexity(output_text,perplexity_model,perplexity_n)
    if context_text: r.groundedness=groundedness_score(output_text,context_text)
    r.word_count=count_words(output_text)
    r.char_count=count_characters(output_text)
    r.approx_token_count=approximate_token_count(output_text)
    return r
