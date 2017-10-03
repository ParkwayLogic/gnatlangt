from google.cloud import language

def language_analysis(text):
	client = language.Client()
	document = client.document_from_text(text)
	sent_analysis = document.analyze_sentiment()
	# print(dir(sent_analysis))
	sentiment = sent_analysis.sentiment  # direction and magnitude
	ent_analysis = document.analyze_entities()
	entities = ent_analysis.entities  # entity and salience
	return sentiment, entities

example_text = """
Hemingway read John Donne: "Ask not for whom the bell 
tolls, for it tolls for thee."
"""

sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)

for e in entities:
	print('entity:', e.name, e.entity_type, e.metadata, e.salience)
	