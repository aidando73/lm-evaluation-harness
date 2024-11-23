
```bash
source $STORAGE_DIR/lm-evaluation-harness/.venv/bin/activate
```

```bash
pip install lm-eval[vllm]
```

```bash
huggingface-cli login
```

```bash
pip install -e .
```

```bash
run_nohup lm_eval --model vllm \
  --model_args pretrained=meta-llama/Llama-3.2-1B,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.25,data_parallel_size=1,max_model_len=8192,add_bos_token=True,seed=42 \
  --tasks meta_mmlu \
  --batch_size auto \
  --output_path eval_results \
  --seed 42  \
  --log_samples \
  --limit 3
```

```bash
cat $(ls -1 $STORAGE_DIR/lm-evaluation-harness/eval_results/meta-llama__Llama-3.2-1B/samples_meta_mmlu* | tail -n 1) \
  | tail -n 1 \
  | jq

```