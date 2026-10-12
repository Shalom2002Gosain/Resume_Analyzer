import re

SKILLS = [
     # Programming Languages
    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "typescript",
    "sql",
    "r",
    "go",
    "rust",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "genai",
    "llm",
    "large language models",
    "transformers",
    "bert",
    "gpt",

    # Frameworks
    "tensorflow",
    "pytorch",
    "keras",
    "scikit-learn",
    "sklearn",
    "opencv",
    "spacy",
    "nltk",
    "pandas",
    "numpy",

    # GenAI
    "langchain",
    "langgraph",
    "rag",
    "retrieval augmented generation",
    "vector database",
    "faiss",
    "chroma",
    "pinecone",
    "prompt engineering",
    "ai agents",
    "agentic ai",

    # Web / APIs
    "fastapi",
    "flask",
    "django",
    "rest api",
    "api",

    # Cloud
    "aws",
    "azure",
    "google cloud",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",
    "git",
    "github",
    "ci/cd",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "redis",

    # Data
    "data science",
    "data analysis",
    "statistics",
    "power bi",
    "tableau"
]


def extract_skills(text):
    
    text = text.lower()
    
    found_skills = []
    
    for skill in SKILLS:

        # Check if skill exists
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills