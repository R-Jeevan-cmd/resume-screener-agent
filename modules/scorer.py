from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(jd_text: str, resume_text: str) -> float:
    """
    Returns semantic similarity score between 0 and 100.
    """

    jd_embedding = model.encode([jd_text])
    resume_embedding = model.encode([resume_text])

    similarity = cosine_similarity(
        jd_embedding,
        resume_embedding
    )[0][0]

    return round(similarity * 100, 2)


def compute_final_score(
    skill_score,
    experience_score,
    semantic_score
):
    """
    Weighted score.

    Skill        : 50%
    Experience   : 30%
    Semantic NLP : 20%
    """

    final = (
        (0.50 * skill_score)
        + (0.30 * experience_score)
        + (0.20 * semantic_score)
    )

    return round(final, 1)