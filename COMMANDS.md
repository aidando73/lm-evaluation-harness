
```bash

# model="meta-llama/Llama-3.2-1B"
model="meta-llama/Llama-3.1-8B"

source $STORAGE_DIR/lm-evaluation-harness/.venv/bin/activate

huggingface-cli login

lm_eval --model hf \
  --model_args pretrained=$model \
  --tasks hellaswag,lambada_openai,arc_easy \
  --device cuda:0 \
  --batch_size 8 \
  2>&1 | tee -a logs

python join.py

pip install lm-eval[math,ifeval,sentencepiece,vllm]==0.4.3

pip install -e . && lm_eval --model vllm \
  --model_args pretrained=meta-llama/Llama-3.2-1B-Instruct,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.25,data_parallel_size=1,max_model_len=8192,add_bos_token=True,seed=42 \
  --tasks meta_math \
  --batch_size auto \
  --output_path eval_results \
  --seed 42 \
  --limit 100 \
  --log_samples 2>&1 | tee -a log-$(hostname)


pip install -e . && lm_eval --model vllm \
  --model_args pretrained=meta-llama/Llama-3.2-1B-Instruct,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.25,data_parallel_size=1,max_model_len=8192,add_bos_token=True,seed=42 \
  --tasks meta_math \
  --batch_size auto \
  --output_path eval_results \
  --seed 42 \
  --log_samples 2>&1 | tee -a log-$(hostname)
```