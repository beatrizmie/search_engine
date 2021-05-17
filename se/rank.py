def score_document(terms, doc):
    score = 0
    for word in doc:
        if word in terms:
            score += 1
    return score


def rank_documents(query, docs, index_query):
    terms = query.get_terms()
    ranked_index = []
    for doc_number in index_query:
        doc = docs[doc_number]
        score = score_document(terms, doc)
        ranked_index.append((score, doc_number))
    ranked_index = sorted(ranked_index, key=lambda x: -x[0])
    return [item[1] for item in ranked_index]
