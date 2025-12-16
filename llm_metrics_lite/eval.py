from dataclasses import dataclass
from .coherence import coherence_score
from .perplexity import ngram_perplexity
from .factuality import groundedness_score
from .tokens import count_words,count_characters,approximate_token_count
from .readability import flesch_reading_ease
from .lexical import lexical_diversity
from .repetition import repetition_ratio
from .uncertinity import uncertainty_score
from .numeric import numeric_density
from .quality import quality_index
from .cost import estimated_cost

@dataclass
class LLMEvaluationResult:
    coherence: float = None
    perplexity: float = None
    groundedness: float = None

    readability: float = None
    lexical_diversity: float = None
    repetition: float = None
    uncertainty: float = None
    numeric_density: float = None

    quality_index: float = None
    estimated_cost: float = None

    word_count: int = None
    char_count: int = None
    approx_token_count: int = None

def evaluate_output(
    output_text,
    context_text=None,
    perplexity_model=None,
    perplexity_n=3,
    price_per_1k_tokens=0.002,
):
    r = LLMEvaluationResult()

    # --- Core quality ---
    r.coherence = coherence_score(output_text)

    if perplexity_model:
        r.perplexity = ngram_perplexity(
            output_text, perplexity_model, perplexity_n
        )

    if context_text:
        r.groundedness = groundedness_score(output_text, context_text)

    # --- Text statistics ---
    r.word_count = count_words(output_text)
    r.char_count = count_characters(output_text)
    r.approx_token_count = approximate_token_count(output_text)

    # --- Added metrics ---
    r.readability = flesch_reading_ease(output_text)
    r.lexical_diversity = lexical_diversity(output_text)
    r.repetition = repetition_ratio(output_text)
    r.uncertainty = uncertainty_score(output_text)
    r.numeric_density = numeric_density(output_text)

    # --- Composite quality index ---
    r.quality_index = quality_index(
        coherence=r.coherence or 0,
        repetition=r.repetition or 0,
        groundedness=r.groundedness or 0,
        readability=r.readability or 0,
    )

    # --- Cost estimation ---
    r.estimated_cost = estimated_cost(
        r.approx_token_count, price_per_1k_tokens
    )

    return r

