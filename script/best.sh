
source activate /home/wangzihan/condaenv/llm
cd /home/wangzihan/MCPrecommand
CUDA_VISIBLE_DEVICES=3 python best.py --tool time  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool markdown  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool fetch  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool hotnews  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool installer  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool search  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool weather  &
CUDA_VISIBLE_DEVICES=3 python best.py --tool cryto  &


