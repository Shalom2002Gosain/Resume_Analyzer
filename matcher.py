from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def calculate_similarity(resume_text, job_text):
    
    documents = [
        resume_text,
        job_text
    ]
    
    # convert text into vector
    
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )
    
    vectors = vectorizer.fit_transform(documents)
    
    
    # calculate similarity
    
    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )
    
    score = similarity[0][0]*100
    return round(score, 2)