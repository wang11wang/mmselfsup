config = 'configs/selfsup/mae/mae_vit-base_b4096-coslr-400e_in1k.py'
work_dirs = 'work_dirs/selfsup/mae_imagenet_pretrain_b4096_400e'
job_name = 'mae_4096_400'
srun_args = ''
partition = 'mediaf1'
gpus_per_node = 8
gpus = 32