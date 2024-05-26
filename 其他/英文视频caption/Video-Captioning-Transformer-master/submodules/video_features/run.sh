python main.py --feature_type i3d --flow_type raft --output_direct --device_ids 0 1 2 3 \
--on_extraction save_numpy \
--video_dir /data3/lzh_3/video-captioning-swin-transformer/data/msvd_trainval \
--output_path /data3/lzh_3/video-captioning-swin-transformer/data/msvd_I3D_feats

python --feature_type CLIP-ViT-B/32 --output_direct --device_ids 0 1 2 3 \
--on_extraction save_numpy \
--extraction_fps 2 \
--video_dir /data3/lzh_3/video-captioning-swin-transformer/data/msvd_trainval \
--output_path /data3/lzh_3/video-captioning-swin-transformer/data/msvd_CLIP_fps2_feats

python --feature_type CLIP-ViT-B/32 --output_direct --cpu \
--on_extraction save_numpy \
--extract uni_12 \
--video_paths ./sample/v_ZNVhz7ctTq0.mp4 \
--output_path ./sample


python main.py --feature_type CLIP-ViT-B/32 --output_direct --cpu --on_extraction save_numpy --extract_method uni_12 --video_paths ./sample/v_ZNVhz7ctTq0.mp4 --output_path ./sample

python main.py --feature_type CLIP4CLIP-ViT-B-32 --output_direct --cpu --on_extraction save_numpy --extract_method uni_12 --video_paths ./sample/v_GGSY1Qvo990.mp4 --output_path ./sample

