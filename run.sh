# model="meta-llama/Llama-3.2-1B"
model="meta-llama/Llama-3.1-8B"


lm_eval --model hf \
  --model_args pretrained=$model \
  --tasks hellaswag,lambada_openai,arc_easy \
  --device cuda:0 \
  --batch_size 8 \
  2>&1 | tee -a logs

pip install -e .[vllm]

pip install -e . && lm_eval --model vllm \
  --model_args pretrained=meta-llama/Llama-3.2-1B-Instruct,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.25,data_parallel_size=1,max_model_len=8192,add_bos_token=True,seed=42 \
  --tasks meta_gpqa \
  --batch_size auto \
  --output_path eval_results \
  --include_path /home/ubuntu/1xa100-2/llama-recipes/tools/benchmarks/llm_eval_harness/meta_eval/work_dir \
  --seed 42 \
  --limit 1 \
  --log_samples 2>&1 | tee -a log-141-148-201-82