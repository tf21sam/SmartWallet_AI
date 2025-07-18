from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('rag/financial_tips.txt', 'r') as file:
    tips = [line.strip() for line in file.readlines()]
tip_embeddings = model.encode(tips)

def get_financial_advice(query):
    query_embedding = model.encode([query])[0]
    scores = util.cos_sim(query_embedding, tip_embeddings)[0]
    best_tip_index = scores.argmax().item()
    return tips[best_tip_index]
