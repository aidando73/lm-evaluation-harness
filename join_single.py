import datasets
from datasets import load_dataset
from datasets import Dataset

model_name="Llama-3.2-1B-Instruct"
original_dataset_name = "lighteval/MATH"
meta_dataset_name = f"meta-llama/{model_name}-evals"
meta_data = load_dataset(
    meta_dataset_name,
    name=f"{model_name}-evals__math__details",
    split="latest",
)
math_data = load_dataset(original_dataset_name, split="test")
meta_df = meta_data.to_pandas()
math_df = math_data.to_pandas()
math_df = math_df.rename(columns={"problem": "input_question"})
# join the two datasets on the input_question column
joined = meta_df.join(math_df.set_index("input_question"), on="input_question")
joined = Dataset.from_pandas(joined)
joined = joined.select_columns(
    [
        "input_question",
        "input_correct_responses",
        "input_final_prompts",
        "is_correct",
        "solution",
        "output_prediction_text",
    ]
)
joined = joined.rename_column("is_correct", "previous_is_correct")
joined = joined.rename_column(
    "output_prediction_text", "previous_output_prediction_text"
)

# Filter out so only one row

joined = joined.filter(lambda x: "are the four distinct roots of the equation $x^4+2x^3+2=0$. Determine the unordered set" in x["input_question"])

joined.to_parquet("./joined_math.parquet")