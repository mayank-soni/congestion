save_local:
	python -c 'from congestion.data.save_local import save_local; save_local()'

save_cloud:
	python -c 'from congestion.data.save_cloud import save_cloud; save_cloud()'

save_cloud_vm:
	/home/mayank-soni/.pyenv/shims/python -c 'from congestion.data.save_cloud import save_cloud; save_cloud()'
