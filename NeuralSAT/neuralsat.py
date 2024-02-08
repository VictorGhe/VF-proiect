import subprocess
from subprocess import TimeoutExpired
import time

combinations = []

all_combinations = [
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift5_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift20_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/if_then_5levels_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/if_then_7levels_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_small_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/if_then_9levels_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta5_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta10_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta20_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta40_epsilon10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift5_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift10_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift20_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/if_then_7levels_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_20.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/if_then_9levels_w20.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta5_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta10_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta20_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_2perturbations_delta40_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta5_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta10_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta20_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_4perturbations_delta40_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta5_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta10_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta20_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_8perturbations_delta40_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta5_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta10_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta20_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/robustness_16perturbations_delta40_epsilon10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift5_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift10_w40.vnnlib"),
	    ("vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/onnx/NN_rul_full_window_40.onnx", "vnncomp2023_benchmarks/benchmarks/collins_rul_cnn/vnnlib/monotonicity_CI_shift20_w40.vnnlib")
	]

combinations.extend(all_combinations)


results = []

with open("results.txt", "w") as result_file:
    for onnx_file, vnnlib_file in combinations:
        command = [
            "python3",
            "main.py",
            "--net",
            onnx_file,
            "--spec",
            vnnlib_file,
        ]

        # Start timer
        start_time = time.time()

        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate(timeout=130)

            if process.returncode == 0:
                result = (command, output.decode(), error.decode())
            else:
                result = (command, f"Process returned non-zero exit code: {process.returncode}", error.decode())
        except TimeoutExpired:
            result = (command, "Timeout: Command exceeded 130 seconds", "")

        results.append(result)

       
        print("\n".join(result[0]))  
        print(result[1])  

        result_file.write(" ".join(result[0]) + "\n")
        result_file.write(result[1] + result[2] + "\n")
