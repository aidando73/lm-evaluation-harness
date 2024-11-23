import datasets
from pprint import pprint


dataset="meta-llama/llama-3.2-1B-evals"

dataset = datasets.load_dataset(dataset, name="Llama-3.2-1B-evals__mmlu__details")

input_question = "There are 230 calories in 4 ounces of a type of ice cream. How many calories are in 6 ounces of that ice cream?"

row = dataset.filter(lambda x: x["input_question"] == input_question)

# pprint(row['latest'][0])
print(row['latest'][0]['input_final_prompts'][0])