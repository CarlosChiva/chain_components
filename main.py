# this is only a example code of how call chain(variable who contain all configuration about database and llm) not use if not execute chain_composition before.
import chain
from question import Question

# Define the question input
question_text = "What is the latest research on large language models?"
question = Question(__root__=question_text)

# Execute the chain and get the output
result = chain(question)
print(result)