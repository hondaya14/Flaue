
python_path_root="$(pwd)"
python_path_src="$(pwd)/src"
python_path_lib="$(pwd)/src/lib"
python_path_config="$(pwd)/src/config"
export "PYTHONPATH=$python_path_root:$python_path_src:$python_path_lib:$python_path_config"
python src/laue.py /Users/honda/Desktop/cor_intensity/ch3_20_oh_280/intensity_potential_gt.txt
