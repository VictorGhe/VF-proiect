Last login: Wed Jan 31 12:08:31 on ttys000
victorg@victors-air build % ls
CMakeCache.txt		Makefile		lp_feasible_1.mps	src
CMakeFiles		cmake_install.cmake	lp_infeasible_1.mps	tests
CTestTestfile.cmake	input_parsers		regress			tools
victorg@victors-air build % cd ~
victorg@victors-air ~ % ls
Applications			Movies				Virtual Machines.localized
Applications (Parallels)	Music				VirtualKey.db
Cisco Packet Tracer 8.2.1	Parallels			cadical
Desktop				Pictures			eclipse
Documents			Postman				eclipse-workspace
Downloads			Public				find.txt.gz
Library				README				pvmd
Marabou				Soulseek Chat Logs		v
MirrorTo.ini			Soulseek Downloads		vnncomp2023_benchmarks
victorg@victors-air ~ % cd Marabou 
victorg@victors-air Marabou % ls
AUTHORS		COPYING		THANKS		maraboupy	resources	tools
CHANGELOG.md	MANIFEST.in	build		pyproject.toml	setup.py
CMakeLists.txt	README.md	deps		regress		src
victorg@victors-air Marabou % ctest
*********************************
No test configuration file found!
*********************************
Usage

  ctest [options]

victorg@victors-air Marabou % ctest -L unit
Test project /Users/victorg/Marabou
No tests were found!!!
victorg@victors-air Marabou % cd ~
victorg@victors-air ~ % ls
Applications			Movies				Virtual Machines.localized
Applications (Parallels)	Music				VirtualKey.db
Cisco Packet Tracer 8.2.1	Parallels			cadical
Desktop				Pictures			eclipse
Documents			Postman				eclipse-workspace
Downloads			Public				find.txt.gz
Library				README				pvmd
Marabou				Soulseek Chat Logs		v
MirrorTo.ini			Soulseek Downloads		vnncomp2023_benchmarks
victorg@victors-air ~ % cd vnncomp2023_benchmarks 
victorg@victors-air vnncomp2023_benchmarks % ls
README.md		benchmarks		run_all_categories.sh	run_single_instance.sh	setup.sh
victorg@victors-air vnncomp2023_benchmarks % ls
README.md		benchmarks		run_all_categories.sh	run_single_instance.sh	setup.sh
victorg@victors-air vnncomp2023_benchmarks % 
victorg@victors-air vnncomp2023_benchmarks % cd ~
victorg@victors-air ~ % cd Marabou 
victorg@victors-air Marabou % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

zsh: no such file or directory: ./build/Marabou
victorg@victors-air Marabou % ls
AUTHORS		COPYING		THANKS		deps		regress		src
CHANGELOG.md	MANIFEST.in	Testing		maraboupy	resources	tools
CMakeLists.txt	README.md	build		pyproject.toml	setup.py
victorg@victors-air Marabou % cd build
victorg@victors-air build % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

zsh: no such file or directory: ./build/Marabou
victorg@victors-air build % cd build
cd: no such file or directory: build
victorg@victors-air build % /build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt 


zsh: no such file or directory: /build/Marabou
victorg@victors-air build % cd ~
victorg@victors-air ~ % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

zsh: no such file or directory: ./build/Marabou
victorg@victors-air ~ % cd Marabou
victorg@victors-air Marabou % ls
AUTHORS		COPYING		THANKS		deps		regress		src
CHANGELOG.md	MANIFEST.in	Testing		maraboupy	resources	tools
CMakeLists.txt	README.md	build		pyproject.toml	setup.py
victorg@victors-air Marabou % cd build
victorg@victors-air build % cd ..
victorg@victors-air Marabou % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

zsh: no such file or directory: ./build/Marabou
victorg@victors-air Marabou % ls
AUTHORS		COPYING		THANKS		deps		regress		src
CHANGELOG.md	MANIFEST.in	Testing		maraboupy	resources	tools
CMakeLists.txt	README.md	build		pyproject.toml	setup.py
victorg@victors-air Marabou % cd build
victorg@victors-air build % ls
CMakeCache.txt		Makefile		lp_feasible_1.mps	src
CMakeFiles		cmake_install.cmake	lp_infeasible_1.mps	tests
CTestTestfile.cmake	input_parsers		regress			tools
victorg@victors-air build % ls -l
total 592
-rw-r--r--   1 victorg  staff   26952 Jan 31 15:25 CMakeCache.txt
drwxr-xr-x  20 victorg  staff     640 Jan 31 15:25 CMakeFiles
-rw-r--r--   1 victorg  staff     347 Jan 31 15:25 CTestTestfile.cmake
-rw-r--r--   1 victorg  staff  257407 Jan 31 15:25 Makefile
-rw-r--r--   1 victorg  staff    2191 Jan 31 15:25 cmake_install.cmake
drwxr-xr-x   2 victorg  staff      64 Jan 31 15:25 input_parsers
-rw-r--r--   1 victorg  staff     512 Jan 31 14:41 lp_feasible_1.mps
-rw-r--r--   1 victorg  staff     713 Jan 31 14:41 lp_infeasible_1.mps
drwxr-xr-x  12 victorg  staff     384 Jan 31 15:25 regress
drwxr-xr-x  15 victorg  staff     480 Jan 31 15:25 src
drwxr-xr-x  10 victorg  staff     320 Jan 31 15:25 tests
drwxr-xr-x   8 victorg  staff     256 Jan 31 15:25 tools
victorg@victors-air build % ls -l Marabou
ls: Marabou: No such file or directory
victorg@victors-air build % cmake --build .
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/tools/onnx-1.12.0/onnx.proto3.pb.cc.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/deps/CVC4/context/context.cpp.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/deps/CVC4/context/context_mm.cpp.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/deps/CVC4/base/check.cpp.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/deps/CVC4/base/exception.cpp.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/deps/CVC4/base/output.cpp.o
[  0%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/real/CommonReal.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/real/Errno.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/real/FileFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/real/CostFunctionManagerFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/real/RowBoundTightenerFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/real/TableauFactory.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/configuration/GlobalConfiguration.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/configuration/OptionParser.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/configuration/Options.cpp.o
[  1%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/AbsoluteValueConstraint.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/BlandsRule.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/BoundManager.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/CDSmtCore.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/ConstraintMatrixAnalyzer.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/CostFunctionManager.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DantzigsRule.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DegradationChecker.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DisjunctionConstraint.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DnCManager.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DnCMarabou.cpp.o
[  2%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/DnCWorker.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Engine.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/EngineState.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/EntrySelectionStrategy.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Equation.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/InputQuery.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/LargestIntervalDivider.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/MILPEncoder.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Marabou.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/MarabouMain.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/MaxConstraint.cpp.o
[  3%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PLConstraintScoreTracker.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PiecewiseLinearCaseSplit.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PiecewiseLinearConstraint.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PolarityBasedDivider.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PrecisionRestorer.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Preprocessor.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/ProjectedSteepestEdge.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/PseudoImpactTracker.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/QueryDivider.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/ReluConstraint.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/RowBoundTightener.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/SigmoidConstraint.cpp.o
[  4%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/SignConstraint.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Simulator.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/SmtCore.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/SumOfInfeasibilitiesManager.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/Tableau.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/TableauRow.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/TableauState.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/TranscendentalConstraint.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/engine/main.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/BasisFactorizationFactory.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/CSRMatrix.cpp.o
[  5%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/EtaMatrix.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/ForrestTomlinFactorization.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/GaussianEliminator.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/LPElement.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/LUFactorization.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/LUFactors.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/PermutationMatrix.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseColumnsOfBasis.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseEtaMatrix.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseFTFactorization.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseGaussianEliminator.cpp.o
[  6%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseLUFactorization.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseLUFactors.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseUnsortedArray.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseUnsortedArrays.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseUnsortedList.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/basis_factorization/SparseUnsortedLists.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/ConstSimpleData.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/Error.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/File.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/FloatUtils.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/GurobiWrapper.cpp.o
[  7%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/HeapData.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/IFile.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/LinearExpression.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/MString.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/MatrixMultiplication.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/SignalHandler.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/Statistics.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/common/TimeUtils.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/AcasNeuralNetwork.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/AcasNnet.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/AcasParser.cpp.o
[  8%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/BerkeleyNeuralNetwork.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/BerkeleyParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/MpsParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/NetworkParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/OnnxParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/PropertyParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/TensorUtils.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/input_parsers/VnnLibParser.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/query_loader/QueryLoader.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyAbsoluteValueElement.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyAnalysis.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyElement.cpp.o
[  9%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyInputElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyMaxPoolElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyReLUElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolySigmoidElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolySignElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/DeepPolyWeightedSumElement.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/IterativePropagator.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/LPFormulator.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/Layer.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/MILPFormulator.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/NetworkLevelReasoner.cpp.o
[ 10%] Building CXX object CMakeFiles/MarabouHelper.dir/src/nlr/ParallelSolver.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/BoundExplainer.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/Checker.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/Contradiction.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/JsonWriter.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/PlcLemma.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/SmtLibWriter.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/UnsatCertificateNode.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelper.dir/src/proofs/UnsatCertificateUtils.cpp.o
[ 11%] Linking CXX static library libMarabouHelper.a
[ 11%] Built target MarabouHelper
[ 11%] Building CXX object CMakeFiles/Marabou.dir/src/engine/main.cpp.o
[ 11%] Linking CXX executable Marabou
[ 11%] Built target Marabou
[ 11%] Building CXX object CMakeFiles/MarabouCore.dir/maraboupy/MarabouCore.cpp.o
[ 11%] Linking CXX shared module /Users/victorg/Marabou/maraboupy/MarabouCore.cpython-311-darwin.so
[ 11%] Built target MarabouCore
[ 11%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/configuration/GlobalConfiguration.cpp.o
[ 11%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/configuration/OptionParser.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/configuration/Options.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/AbsoluteValueConstraint.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/BlandsRule.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/BoundManager.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/CDSmtCore.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/ConstraintMatrixAnalyzer.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/CostFunctionManager.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DantzigsRule.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DegradationChecker.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DisjunctionConstraint.cpp.o
[ 12%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DnCManager.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DnCMarabou.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/DnCWorker.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Engine.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/EngineState.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/EntrySelectionStrategy.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Equation.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/InputQuery.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/LargestIntervalDivider.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/MILPEncoder.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Marabou.cpp.o
[ 13%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/MarabouMain.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/MaxConstraint.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PLConstraintScoreTracker.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PiecewiseLinearCaseSplit.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PiecewiseLinearConstraint.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PolarityBasedDivider.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PrecisionRestorer.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Preprocessor.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/ProjectedSteepestEdge.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/PseudoImpactTracker.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/QueryDivider.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/ReluConstraint.cpp.o
[ 14%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/RowBoundTightener.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/SigmoidConstraint.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/SignConstraint.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Simulator.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/SmtCore.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/SumOfInfeasibilitiesManager.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/Tableau.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/TableauRow.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/TableauState.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/TranscendentalConstraint.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/engine/main.cpp.o
[ 15%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/BasisFactorizationFactory.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/CSRMatrix.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/EtaMatrix.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/ForrestTomlinFactorization.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/GaussianEliminator.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/LPElement.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/LUFactorization.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/LUFactors.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/PermutationMatrix.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseColumnsOfBasis.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseEtaMatrix.cpp.o
[ 16%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseFTFactorization.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseGaussianEliminator.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseLUFactorization.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseLUFactors.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseUnsortedArray.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseUnsortedArrays.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseUnsortedList.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/basis_factorization/SparseUnsortedLists.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/ConstSimpleData.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/Error.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/File.cpp.o
[ 17%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/FloatUtils.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/GurobiWrapper.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/HeapData.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/IFile.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/LinearExpression.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/MString.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/MatrixMultiplication.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/SignalHandler.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/Statistics.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/common/TimeUtils.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/AcasNeuralNetwork.cpp.o
[ 18%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/AcasNnet.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/AcasParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/BerkeleyNeuralNetwork.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/BerkeleyParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/MpsParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/NetworkParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/OnnxParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/PropertyParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/TensorUtils.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/input_parsers/VnnLibParser.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/query_loader/QueryLoader.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyAbsoluteValueElement.cpp.o
[ 19%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyAnalysis.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyInputElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyMaxPoolElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyReLUElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolySigmoidElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolySignElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/DeepPolyWeightedSumElement.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/IterativePropagator.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/LPFormulator.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/Layer.cpp.o
[ 20%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/MILPFormulator.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/NetworkLevelReasoner.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/nlr/ParallelSolver.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/BoundExplainer.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/Checker.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/Contradiction.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/JsonWriter.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/PlcLemma.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/SmtLibWriter.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/UnsatCertificateNode.cpp.o
[ 21%] Building CXX object CMakeFiles/MarabouHelperTest.dir/src/proofs/UnsatCertificateUtils.cpp.o
[ 21%] Linking CXX static library libMarabouHelperTest.a
[ 21%] Built target MarabouHelperTest
[ 21%] Generating Test_UnsatCertificateUtils.cc
[ 21%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/Test_UnsatCertificateUtils.cc.o
[ 21%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/common/real/CommonReal.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/common/real/Errno.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/common/real/FileFactory.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 22%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateUtils.dir/__/engine/real/TableauFactory.cpp.o
[ 22%] Linking CXX executable Test_UnsatCertificateUtils
[ 22%] Built target Test_UnsatCertificateUtils
[ 22%] Built target build-unit-tests
[ 23%] Generating Test_AbsoluteValueConstraint.cc
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/Test_AbsoluteValueConstraint.cc.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/__/common/mock/Errno.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 23%] Building CXX object src/engine/CMakeFiles/Test_AbsoluteValueConstraint.dir/mock/TableauFactory.cpp.o
[ 23%] Linking CXX executable Test_AbsoluteValueConstraint
[ 23%] Built target Test_AbsoluteValueConstraint
[ 23%] Generating Test_BlandsRule.cc
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/Test_BlandsRule.cc.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/__/common/mock/CommonMock.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/__/common/mock/Errno.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/__/common/mock/FileFactory.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/mock/CostFunctionManagerFactory.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/mock/RowBoundTightenerFactory.cpp.o
[ 24%] Building CXX object src/engine/CMakeFiles/Test_BlandsRule.dir/mock/TableauFactory.cpp.o
[ 24%] Linking CXX executable Test_BlandsRule
[ 24%] Built target Test_BlandsRule
[ 24%] Generating Test_BoundManager.cc
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/Test_BoundManager.cc.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/__/common/mock/CommonMock.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/__/common/mock/Errno.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/__/common/mock/FileFactory.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/mock/CostFunctionManagerFactory.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/mock/RowBoundTightenerFactory.cpp.o
[ 25%] Building CXX object src/engine/CMakeFiles/Test_BoundManager.dir/mock/TableauFactory.cpp.o
[ 25%] Linking CXX executable Test_BoundManager
[ 25%] Built target Test_BoundManager
[ 25%] Generating Test_ConstraintMatrixAnalyzer.cc
[ 25%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/Test_ConstraintMatrixAnalyzer.cc.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/__/common/mock/CommonMock.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/__/common/mock/Errno.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/__/common/mock/FileFactory.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/mock/CostFunctionManagerFactory.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/mock/RowBoundTightenerFactory.cpp.o
[ 26%] Building CXX object src/engine/CMakeFiles/Test_ConstraintMatrixAnalyzer.dir/mock/TableauFactory.cpp.o
[ 26%] Linking CXX executable Test_ConstraintMatrixAnalyzer
[ 26%] Built target Test_ConstraintMatrixAnalyzer
[ 26%] Generating Test_CostFunctionManager.cc
[ 26%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/Test_CostFunctionManager.cc.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/__/common/mock/CommonMock.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/__/common/mock/Errno.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/__/common/mock/FileFactory.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/mock/CostFunctionManagerFactory.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/mock/RowBoundTightenerFactory.cpp.o
[ 27%] Building CXX object src/engine/CMakeFiles/Test_CostFunctionManager.dir/mock/TableauFactory.cpp.o
[ 27%] Linking CXX executable Test_CostFunctionManager
[ 27%] Built target Test_CostFunctionManager
[ 27%] Generating Test_DantzigsRule.cc
[ 27%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/Test_DantzigsRule.cc.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/__/common/mock/CommonMock.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/__/common/mock/Errno.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/__/common/mock/FileFactory.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/mock/CostFunctionManagerFactory.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/mock/RowBoundTightenerFactory.cpp.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DantzigsRule.dir/mock/TableauFactory.cpp.o
[ 28%] Linking CXX executable Test_DantzigsRule
[ 28%] Built target Test_DantzigsRule
[ 28%] Generating Test_DegradationChecker.cc
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/Test_DegradationChecker.cc.o
[ 28%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/__/common/mock/CommonMock.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/__/common/mock/Errno.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/__/common/mock/FileFactory.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/mock/CostFunctionManagerFactory.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/mock/RowBoundTightenerFactory.cpp.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DegradationChecker.dir/mock/TableauFactory.cpp.o
[ 29%] Linking CXX executable Test_DegradationChecker
[ 29%] Built target Test_DegradationChecker
[ 29%] Generating Test_DisjunctionConstraint.cc
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/Test_DisjunctionConstraint.cc.o
[ 29%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/__/common/mock/Errno.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DisjunctionConstraint.dir/mock/TableauFactory.cpp.o
[ 30%] Linking CXX executable Test_DisjunctionConstraint
[ 30%] Built target Test_DisjunctionConstraint
[ 30%] Generating Test_DnCWorker.cc
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/Test_DnCWorker.cc.o
[ 30%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/__/common/mock/CommonMock.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/__/common/mock/Errno.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/__/common/mock/FileFactory.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/mock/CostFunctionManagerFactory.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/mock/RowBoundTightenerFactory.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_DnCWorker.dir/mock/TableauFactory.cpp.o
[ 31%] Linking CXX executable Test_DnCWorker
[ 31%] Built target Test_DnCWorker
[ 31%] Generating Test_Engine.cc
[ 31%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/Test_Engine.cc.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/__/common/mock/CommonMock.cpp.o
[ 31%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/__/common/mock/Errno.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/__/common/mock/FileFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/mock/CostFunctionManagerFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/mock/RowBoundTightenerFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_Engine.dir/mock/TableauFactory.cpp.o
[ 32%] Linking CXX executable Test_Engine
[ 32%] Built target Test_Engine
[ 32%] Generating Test_InputQuery.cc
[ 32%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/Test_InputQuery.cc.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/__/common/mock/CommonMock.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/__/common/mock/Errno.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/__/common/mock/FileFactory.cpp.o
[ 32%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/mock/CostFunctionManagerFactory.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/mock/RowBoundTightenerFactory.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_InputQuery.dir/mock/TableauFactory.cpp.o
[ 33%] Linking CXX executable Test_InputQuery
[ 33%] Built target Test_InputQuery
[ 33%] Generating Test_LargestIntervalDivider.cc
[ 33%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/Test_LargestIntervalDivider.cc.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/__/common/mock/CommonMock.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/__/common/mock/Errno.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/__/common/mock/FileFactory.cpp.o
[ 33%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/mock/CostFunctionManagerFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/mock/RowBoundTightenerFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_LargestIntervalDivider.dir/mock/TableauFactory.cpp.o
[ 34%] Linking CXX executable Test_LargestIntervalDivider
[ 34%] Built target Test_LargestIntervalDivider
[ 34%] Generating Test_MaxConstraint.cc
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/Test_MaxConstraint.cc.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/__/common/mock/Errno.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 34%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MaxConstraint.dir/mock/TableauFactory.cpp.o
[ 35%] Linking CXX executable Test_MaxConstraint
[ 35%] Built target Test_MaxConstraint
[ 35%] Generating Test_MILPEncoder.cc
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/Test_MILPEncoder.cc.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/__/common/mock/CommonMock.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/__/common/mock/Errno.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/__/common/mock/FileFactory.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 35%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/mock/CostFunctionManagerFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/mock/RowBoundTightenerFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_MILPEncoder.dir/mock/TableauFactory.cpp.o
[ 36%] Linking CXX executable Test_MILPEncoder
[ 36%] Built target Test_MILPEncoder
[ 36%] Generating Test_PolarityBasedDivider.cc
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/Test_PolarityBasedDivider.cc.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/__/common/mock/CommonMock.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/__/common/mock/Errno.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/__/common/mock/FileFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/mock/CostFunctionManagerFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 36%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/mock/RowBoundTightenerFactory.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_PolarityBasedDivider.dir/mock/TableauFactory.cpp.o
[ 37%] Linking CXX executable Test_PolarityBasedDivider
[ 37%] Built target Test_PolarityBasedDivider
[ 37%] Generating Test_Preprocessor.cc
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/Test_Preprocessor.cc.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/__/common/mock/CommonMock.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/__/common/mock/Errno.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/__/common/mock/FileFactory.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/mock/CostFunctionManagerFactory.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 37%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/mock/RowBoundTightenerFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_Preprocessor.dir/mock/TableauFactory.cpp.o
[ 38%] Linking CXX executable Test_Preprocessor
[ 38%] Built target Test_Preprocessor
[ 38%] Generating Test_ProjectedSteepestEdge.cc
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/Test_ProjectedSteepestEdge.cc.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/__/common/mock/CommonMock.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/__/common/mock/Errno.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/__/common/mock/FileFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/mock/CostFunctionManagerFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/mock/RowBoundTightenerFactory.cpp.o
[ 38%] Building CXX object src/engine/CMakeFiles/Test_ProjectedSteepestEdge.dir/mock/TableauFactory.cpp.o
[ 39%] Linking CXX executable Test_ProjectedSteepestEdge
[ 39%] Built target Test_ProjectedSteepestEdge
[ 39%] Generating Test_PseudoImpactTracker.cc
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/Test_PseudoImpactTracker.cc.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/__/common/mock/CommonMock.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/__/common/mock/Errno.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/__/common/mock/FileFactory.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/mock/CostFunctionManagerFactory.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/mock/RowBoundTightenerFactory.cpp.o
[ 39%] Building CXX object src/engine/CMakeFiles/Test_PseudoImpactTracker.dir/mock/TableauFactory.cpp.o
[ 40%] Linking CXX executable Test_PseudoImpactTracker
[ 40%] Built target Test_PseudoImpactTracker
[ 40%] Generating Test_ReluConstraint.cc
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/Test_ReluConstraint.cc.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/__/common/mock/Errno.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 40%] Building CXX object src/engine/CMakeFiles/Test_ReluConstraint.dir/mock/TableauFactory.cpp.o
[ 41%] Linking CXX executable Test_ReluConstraint
[ 41%] Built target Test_ReluConstraint
[ 41%] Generating Test_RowBoundTightener.cc
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/Test_RowBoundTightener.cc.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/__/common/mock/CommonMock.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/__/common/mock/Errno.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/__/common/mock/FileFactory.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/mock/CostFunctionManagerFactory.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/mock/RowBoundTightenerFactory.cpp.o
[ 41%] Building CXX object src/engine/CMakeFiles/Test_RowBoundTightener.dir/mock/TableauFactory.cpp.o
[ 41%] Linking CXX executable Test_RowBoundTightener
[ 41%] Built target Test_RowBoundTightener
[ 42%] Generating Test_SignConstraint.cc
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/Test_SignConstraint.cc.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/__/common/mock/Errno.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 42%] Building CXX object src/engine/CMakeFiles/Test_SignConstraint.dir/mock/TableauFactory.cpp.o
[ 42%] Linking CXX executable Test_SignConstraint
[ 42%] Built target Test_SignConstraint
[ 43%] Generating Test_SigmoidConstraint.cc
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/Test_SigmoidConstraint.cc.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/__/common/mock/CommonMock.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/__/common/mock/Errno.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/__/common/mock/FileFactory.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/mock/CostFunctionManagerFactory.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/mock/RowBoundTightenerFactory.cpp.o
[ 43%] Building CXX object src/engine/CMakeFiles/Test_SigmoidConstraint.dir/mock/TableauFactory.cpp.o
[ 43%] Linking CXX executable Test_SigmoidConstraint
[ 43%] Built target Test_SigmoidConstraint
[ 44%] Generating Test_SmtCore.cc
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/Test_SmtCore.cc.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/__/common/mock/CommonMock.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/__/common/mock/Errno.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/__/common/mock/FileFactory.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/mock/CostFunctionManagerFactory.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/mock/RowBoundTightenerFactory.cpp.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SmtCore.dir/mock/TableauFactory.cpp.o
[ 44%] Linking CXX executable Test_SmtCore
[ 44%] Built target Test_SmtCore
[ 44%] Generating Test_SumOfInfeasibilitiesManager.cc
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/Test_SumOfInfeasibilitiesManager.cc.o
[ 44%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/__/common/mock/CommonMock.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/__/common/mock/Errno.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/__/common/mock/FileFactory.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/mock/CostFunctionManagerFactory.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/mock/RowBoundTightenerFactory.cpp.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_SumOfInfeasibilitiesManager.dir/mock/TableauFactory.cpp.o
[ 45%] Linking CXX executable Test_SumOfInfeasibilitiesManager
[ 45%] Built target Test_SumOfInfeasibilitiesManager
[ 45%] Generating Test_Tableau.cc
[ 45%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/Test_Tableau.cc.o
[ 45%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/__/common/mock/CommonMock.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/__/common/mock/Errno.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/__/common/mock/FileFactory.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/mock/CostFunctionManagerFactory.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/mock/RowBoundTightenerFactory.cpp.o
[ 46%] Building CXX object src/engine/CMakeFiles/Test_Tableau.dir/mock/TableauFactory.cpp.o
[ 46%] Linking CXX executable Test_Tableau
[ 46%] Built target Test_Tableau
[ 46%] Generating Test_CSRMatrix.cc
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/Test_CSRMatrix.cc.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/common/real/CommonReal.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/common/real/Errno.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/common/real/FileFactory.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CSRMatrix.dir/__/engine/real/TableauFactory.cpp.o
[ 47%] Linking CXX executable Test_CSRMatrix
[ 47%] Built target Test_CSRMatrix
[ 47%] Generating Test_CompareFactorizations.cc
[ 47%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/Test_CompareFactorizations.cc.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/common/real/CommonReal.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/common/real/Errno.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/common/real/FileFactory.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_CompareFactorizations.dir/__/engine/real/TableauFactory.cpp.o
[ 48%] Linking CXX executable Test_CompareFactorizations
[ 48%] Built target Test_CompareFactorizations
[ 48%] Generating Test_ForrestTomlinFactorization.cc
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/Test_ForrestTomlinFactorization.cc.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/common/real/CommonReal.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/common/real/Errno.cpp.o
[ 48%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/common/real/FileFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_ForrestTomlinFactorization.dir/__/engine/real/TableauFactory.cpp.o
[ 49%] Linking CXX executable Test_ForrestTomlinFactorization
[ 49%] Built target Test_ForrestTomlinFactorization
[ 49%] Generating Test_LUFactorization.cc
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/Test_LUFactorization.cc.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/common/real/CommonReal.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/common/real/Errno.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/common/real/FileFactory.cpp.o
[ 49%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactorization.dir/__/engine/real/TableauFactory.cpp.o
[ 50%] Linking CXX executable Test_LUFactorization
[ 50%] Built target Test_LUFactorization
[ 50%] Generating Test_LUFactors.cc
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/Test_LUFactors.cc.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/common/real/CommonReal.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/common/real/Errno.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/common/real/FileFactory.cpp.o
[ 50%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_LUFactors.dir/__/engine/real/TableauFactory.cpp.o
[ 51%] Linking CXX executable Test_LUFactors
[ 51%] Built target Test_LUFactors
[ 51%] Generating Test_PermutationMatrix.cc
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/Test_PermutationMatrix.cc.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/common/real/CommonReal.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/common/real/Errno.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/common/real/FileFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 51%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 52%] Building CXX object src/basis_factorization/CMakeFiles/Test_PermutationMatrix.dir/__/engine/real/TableauFactory.cpp.o
[ 52%] Linking CXX executable Test_PermutationMatrix
[ 52%] Built target Test_PermutationMatrix
[ 52%] Generating Test_SparseFTFactorization.cc
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/Test_SparseFTFactorization.cc.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/common/real/CommonReal.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/common/real/Errno.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/common/real/FileFactory.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 53%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseFTFactorization.dir/__/engine/real/TableauFactory.cpp.o
[ 53%] Linking CXX executable Test_SparseFTFactorization
[ 53%] Built target Test_SparseFTFactorization
[ 53%] Generating Test_SparseGaussianEliminator.cc
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/Test_SparseGaussianEliminator.cc.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/common/real/CommonReal.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/common/real/Errno.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/common/real/FileFactory.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 54%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseGaussianEliminator.dir/__/engine/real/TableauFactory.cpp.o
[ 54%] Linking CXX executable Test_SparseGaussianEliminator
[ 54%] Built target Test_SparseGaussianEliminator
[ 54%] Generating Test_SparseLUFactorization.cc
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/Test_SparseLUFactorization.cc.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/common/real/CommonReal.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/common/real/Errno.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/common/real/FileFactory.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 55%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactorization.dir/__/engine/real/TableauFactory.cpp.o
[ 55%] Linking CXX executable Test_SparseLUFactorization
[ 55%] Built target Test_SparseLUFactorization
[ 55%] Generating Test_SparseLUFactors.cc
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/Test_SparseLUFactors.cc.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/common/real/CommonReal.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/common/real/Errno.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/common/real/FileFactory.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseLUFactors.dir/__/engine/real/TableauFactory.cpp.o
[ 56%] Linking CXX executable Test_SparseLUFactors
[ 56%] Built target Test_SparseLUFactors
[ 56%] Generating Test_SparseUnsortedArray.cc
[ 56%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/Test_SparseUnsortedArray.cc.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/common/real/CommonReal.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/common/real/Errno.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/common/real/FileFactory.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArray.dir/__/engine/real/TableauFactory.cpp.o
[ 57%] Linking CXX executable Test_SparseUnsortedArray
[ 57%] Built target Test_SparseUnsortedArray
[ 57%] Generating Test_SparseUnsortedArrays.cc
[ 57%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/Test_SparseUnsortedArrays.cc.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/common/real/CommonReal.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/common/real/Errno.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/common/real/FileFactory.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedArrays.dir/__/engine/real/TableauFactory.cpp.o
[ 58%] Linking CXX executable Test_SparseUnsortedArrays
[ 58%] Built target Test_SparseUnsortedArrays
[ 58%] Generating Test_SparseUnsortedList.cc
[ 58%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/Test_SparseUnsortedList.cc.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/common/real/CommonReal.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/common/real/Errno.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/common/real/FileFactory.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedList.dir/__/engine/real/TableauFactory.cpp.o
[ 59%] Linking CXX executable Test_SparseUnsortedList
[ 59%] Built target Test_SparseUnsortedList
[ 59%] Generating Test_SparseUnsortedLists.cc
[ 59%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/Test_SparseUnsortedLists.cc.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/common/real/CommonReal.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/common/real/Errno.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/common/real/FileFactory.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 60%] Building CXX object src/basis_factorization/CMakeFiles/Test_SparseUnsortedLists.dir/__/engine/real/TableauFactory.cpp.o
[ 60%] Linking CXX executable Test_SparseUnsortedLists
[ 60%] Built target Test_SparseUnsortedLists
[ 60%] Generating Test_ConstSimpleData.cc
[ 60%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/Test_ConstSimpleData.cc.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/mock/CommonMock.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/mock/Errno.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/mock/FileFactory.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_ConstSimpleData.dir/__/engine/real/TableauFactory.cpp.o
[ 61%] Linking CXX executable Test_ConstSimpleData
[ 61%] Built target Test_ConstSimpleData
[ 61%] Generating Test_Error.cc
[ 61%] Building CXX object src/common/CMakeFiles/Test_Error.dir/Test_Error.cc.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_Error.dir/mock/CommonMock.cpp.o
[ 61%] Building CXX object src/common/CMakeFiles/Test_Error.dir/mock/Errno.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/mock/FileFactory.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_Error.dir/__/engine/real/TableauFactory.cpp.o
[ 62%] Linking CXX executable Test_Error
[ 62%] Built target Test_Error
[ 62%] Generating Test_File.cc
[ 62%] Building CXX object src/common/CMakeFiles/Test_File.dir/Test_File.cc.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_File.dir/mock/CommonMock.cpp.o
[ 62%] Building CXX object src/common/CMakeFiles/Test_File.dir/mock/Errno.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/mock/FileFactory.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_File.dir/__/engine/real/TableauFactory.cpp.o
[ 63%] Linking CXX executable Test_File
[ 63%] Built target Test_File
[ 63%] Generating Test_FloatUtils.cc
[ 63%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/Test_FloatUtils.cc.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/mock/CommonMock.cpp.o
[ 63%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/mock/Errno.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/mock/FileFactory.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_FloatUtils.dir/__/engine/real/TableauFactory.cpp.o
[ 64%] Linking CXX executable Test_FloatUtils
[ 64%] Built target Test_FloatUtils
[ 64%] Generating Test_GurobiWrapper.cc
[ 64%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/Test_GurobiWrapper.cc.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/mock/CommonMock.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/mock/Errno.cpp.o
[ 64%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/mock/FileFactory.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_GurobiWrapper.dir/__/engine/real/TableauFactory.cpp.o
[ 65%] Linking CXX executable Test_GurobiWrapper
[ 65%] Built target Test_GurobiWrapper
[ 65%] Generating Test_HashMap.cc
[ 65%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/Test_HashMap.cc.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/mock/CommonMock.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/mock/Errno.cpp.o
[ 65%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/mock/FileFactory.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashMap.dir/__/engine/real/TableauFactory.cpp.o
[ 66%] Linking CXX executable Test_HashMap
[ 66%] Built target Test_HashMap
[ 66%] Generating Test_HashSet.cc
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/Test_HashSet.cc.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/mock/CommonMock.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/mock/Errno.cpp.o
[ 66%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/mock/FileFactory.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HashSet.dir/__/engine/real/TableauFactory.cpp.o
[ 67%] Linking CXX executable Test_HashSet
[ 67%] Built target Test_HashSet
[ 67%] Generating Test_HeapData.cc
[ 67%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/Test_HeapData.cc.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/mock/CommonMock.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/mock/Errno.cpp.o
[ 67%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/mock/FileFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_HeapData.dir/__/engine/real/TableauFactory.cpp.o
[ 68%] Linking CXX executable Test_HeapData
[ 68%] Built target Test_HeapData
[ 68%] Generating Test_LinearExpression.cc
[ 68%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/Test_LinearExpression.cc.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/mock/CommonMock.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/mock/Errno.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/mock/FileFactory.cpp.o
[ 68%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_LinearExpression.dir/__/engine/real/TableauFactory.cpp.o
[ 69%] Linking CXX executable Test_LinearExpression
[ 69%] Built target Test_LinearExpression
[ 69%] Generating Test_List.cc
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/Test_List.cc.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/mock/CommonMock.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/mock/Errno.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/mock/FileFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 69%] Building CXX object src/common/CMakeFiles/Test_List.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_List.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_List.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_List.dir/__/engine/real/TableauFactory.cpp.o
[ 70%] Linking CXX executable Test_List
[ 70%] Built target Test_List
[ 70%] Generating Test_MString.cc
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/Test_MString.cc.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/mock/CommonMock.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/mock/Errno.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/mock/FileFactory.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 70%] Building CXX object src/common/CMakeFiles/Test_MString.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MString.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MString.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MString.dir/__/engine/real/TableauFactory.cpp.o
[ 71%] Linking CXX executable Test_MString
[ 71%] Built target Test_MString
[ 71%] Generating Test_MStringf.cc
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/Test_MStringf.cc.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/mock/CommonMock.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/mock/Errno.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/mock/FileFactory.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 71%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_MStringf.dir/__/engine/real/TableauFactory.cpp.o
[ 72%] Linking CXX executable Test_MStringf
[ 72%] Built target Test_MStringf
[ 72%] Generating Test_Map.cc
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/Test_Map.cc.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/mock/CommonMock.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/mock/Errno.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/mock/FileFactory.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 72%] Building CXX object src/common/CMakeFiles/Test_Map.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Map.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Map.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Map.dir/__/engine/real/TableauFactory.cpp.o
[ 73%] Linking CXX executable Test_Map
[ 73%] Built target Test_Map
[ 73%] Generating Test_Pair.cc
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/Test_Pair.cc.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/mock/CommonMock.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/mock/Errno.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/mock/FileFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 73%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Pair.dir/__/engine/real/TableauFactory.cpp.o
[ 74%] Linking CXX executable Test_Pair
[ 74%] Built target Test_Pair
[ 74%] Generating Test_Queue.cc
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/Test_Queue.cc.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/mock/CommonMock.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/mock/Errno.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/mock/FileFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 74%] Building CXX object src/common/CMakeFiles/Test_Queue.dir/__/engine/real/TableauFactory.cpp.o
[ 75%] Linking CXX executable Test_Queue
[ 75%] Built target Test_Queue
[ 76%] Generating Test_Set.cc
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/Test_Set.cc.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/mock/CommonMock.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/mock/Errno.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/mock/FileFactory.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 76%] Building CXX object src/common/CMakeFiles/Test_Set.dir/__/engine/real/TableauFactory.cpp.o
[ 76%] Linking CXX executable Test_Set
[ 76%] Built target Test_Set
[ 76%] Generating Test_Stack.cc
[ 76%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/Test_Stack.cc.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/mock/CommonMock.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/mock/Errno.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/mock/FileFactory.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Stack.dir/__/engine/real/TableauFactory.cpp.o
[ 77%] Linking CXX executable Test_Stack
[ 77%] Built target Test_Stack
[ 77%] Generating Test_Vector.cc
[ 77%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/Test_Vector.cc.o
[ 77%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/mock/CommonMock.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/mock/Errno.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/mock/FileFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_Vector.dir/__/engine/real/TableauFactory.cpp.o
[ 78%] Linking CXX executable Test_Vector
[ 78%] Built target Test_Vector
[ 78%] Generating Test_MatrixMultiplication.cc
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/Test_MatrixMultiplication.cc.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/mock/CommonMock.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/mock/Errno.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/mock/FileFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 78%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 79%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 79%] Building CXX object src/common/CMakeFiles/Test_MatrixMultiplication.dir/__/engine/real/TableauFactory.cpp.o
[ 79%] Linking CXX executable Test_MatrixMultiplication
[ 79%] Built target Test_MatrixMultiplication
[ 79%] Generating Test_acas.cc
[ 79%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/Test_acas.cc.o
[ 79%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/common/real/CommonReal.cpp.o
[ 79%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/common/real/Errno.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/common/real/FileFactory.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_acas.dir/__/engine/real/TableauFactory.cpp.o
[ 80%] Linking CXX executable Test_acas
[ 80%] Built target Test_acas
[ 80%] Generating Test_lp.cc
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/Test_lp.cc.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/common/real/CommonReal.cpp.o
[ 80%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/common/real/Errno.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/common/real/FileFactory.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_lp.dir/__/engine/real/TableauFactory.cpp.o
[ 81%] Linking CXX executable Test_lp
[ 81%] Built target Test_lp
[ 81%] Generating Test_max.cc
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/Test_max.cc.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/common/real/CommonReal.cpp.o
[ 81%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/common/real/Errno.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/common/real/FileFactory.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_max.dir/__/engine/real/TableauFactory.cpp.o
[ 82%] Linking CXX executable Test_max
[ 82%] Built target Test_max
[ 82%] Generating Test_mps.cc
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/Test_mps.cc.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/common/real/CommonReal.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/common/real/Errno.cpp.o
[ 82%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/common/real/FileFactory.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_mps.dir/__/engine/real/TableauFactory.cpp.o
[ 83%] Linking CXX executable Test_mps
[ 83%] Built target Test_mps
[ 83%] Generating Test_relu.cc
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/Test_relu.cc.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/common/real/CommonReal.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/common/real/Errno.cpp.o
[ 83%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/common/real/FileFactory.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_relu.dir/__/engine/real/TableauFactory.cpp.o
[ 84%] Linking CXX executable Test_relu
[ 84%] Built target Test_relu
[ 84%] Generating Test_sign.cc
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/Test_sign.cc.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/common/real/CommonReal.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/common/real/Errno.cpp.o
[ 84%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/common/real/FileFactory.cpp.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_sign.dir/__/engine/real/TableauFactory.cpp.o
[ 85%] Linking CXX executable Test_sign
[ 85%] Built target Test_sign
[ 85%] Generating Test_Disjunction.cc
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/Test_Disjunction.cc.o
[ 85%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/common/real/CommonReal.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/common/real/Errno.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/common/real/FileFactory.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 86%] Building CXX object src/system_tests/CMakeFiles/Test_Disjunction.dir/__/engine/real/TableauFactory.cpp.o
[ 86%] Linking CXX executable Test_Disjunction
[ 86%] Built target Test_Disjunction
[ 87%] Generating Test_AbsoluteValue.cc
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/Test_AbsoluteValue.cc.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/common/real/CommonReal.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/common/real/Errno.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/common/real/FileFactory.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_AbsoluteValue.dir/__/engine/real/TableauFactory.cpp.o
[ 87%] Linking CXX executable Test_AbsoluteValue
[ 87%] Built target Test_AbsoluteValue
[ 87%] Generating Test_wsElimination.cc
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/Test_wsElimination.cc.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/common/real/CommonReal.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/common/real/Errno.cpp.o
[ 87%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/common/real/FileFactory.cpp.o
[ 88%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 88%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 88%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 88%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 88%] Building CXX object src/system_tests/CMakeFiles/Test_wsElimination.dir/__/engine/real/TableauFactory.cpp.o
[ 88%] Linking CXX executable Test_wsElimination
[ 88%] Built target Test_wsElimination
[ 88%] Generating Test_OnnxParser.cc
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/Test_OnnxParser.cc.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/common/real/CommonReal.cpp.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/common/real/Errno.cpp.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/common/real/FileFactory.cpp.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 88%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 89%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 89%] Building CXX object src/input_parsers/CMakeFiles/Test_OnnxParser.dir/__/engine/real/TableauFactory.cpp.o
[ 89%] Linking CXX executable Test_OnnxParser
[ 89%] Built target Test_OnnxParser
[ 89%] Generating Test_VnnLibParser.cc
[ 89%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/Test_VnnLibParser.cc.o
[ 89%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/common/real/CommonReal.cpp.o
[ 89%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/common/real/Errno.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/common/real/FileFactory.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 90%] Building CXX object src/input_parsers/CMakeFiles/Test_VnnLibParser.dir/__/engine/real/TableauFactory.cpp.o
[ 90%] Linking CXX executable Test_VnnLibParser
[ 90%] Built target Test_VnnLibParser
[ 90%] Generating Test_QueryLoader.cc
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/Test_QueryLoader.cc.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/common/mock/CommonMock.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/common/mock/Errno.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/common/mock/FileFactory.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/engine/mock/ConstraintMatrixAnalyzerFactory.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/engine/mock/CostFunctionManagerFactory.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/engine/mock/ProjectedSteepestEdgeFactory.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/engine/mock/RowBoundTightenerFactory.cpp.o
[ 90%] Building CXX object src/query_loader/CMakeFiles/Test_QueryLoader.dir/__/engine/mock/TableauFactory.cpp.o
[ 91%] Linking CXX executable Test_QueryLoader
[ 91%] Built target Test_QueryLoader
[ 91%] Generating Test_DeepPolyAnalysis.cc
[ 91%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/Test_DeepPolyAnalysis.cc.o
[ 91%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/common/real/CommonReal.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/common/real/Errno.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/common/real/FileFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_DeepPolyAnalysis.dir/__/engine/real/TableauFactory.cpp.o
[ 92%] Linking CXX executable Test_DeepPolyAnalysis
[ 92%] Built target Test_DeepPolyAnalysis
[ 92%] Generating Test_NetworkLevelReasoner.cc
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/Test_NetworkLevelReasoner.cc.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/common/real/CommonReal.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/common/real/Errno.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/common/real/FileFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 92%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 93%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 93%] Building CXX object src/nlr/CMakeFiles/Test_NetworkLevelReasoner.dir/__/engine/real/TableauFactory.cpp.o
[ 93%] Linking CXX executable Test_NetworkLevelReasoner
[ 93%] Built target Test_NetworkLevelReasoner
[ 93%] Generating Test_WsLayerElimination.cc
[ 93%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/Test_WsLayerElimination.cc.o
[ 93%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/common/real/CommonReal.cpp.o
[ 93%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/common/real/Errno.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/common/real/FileFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_WsLayerElimination.dir/__/engine/real/TableauFactory.cpp.o
[ 94%] Linking CXX executable Test_WsLayerElimination
[ 94%] Built target Test_WsLayerElimination
[ 94%] Generating Test_ParallelSolver.cc
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/Test_ParallelSolver.cc.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/common/real/CommonReal.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/common/real/Errno.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/common/real/FileFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 94%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 95%] Building CXX object src/nlr/CMakeFiles/Test_ParallelSolver.dir/__/engine/real/TableauFactory.cpp.o
[ 95%] Linking CXX executable Test_ParallelSolver
[ 95%] Built target Test_ParallelSolver
[ 95%] Generating Test_BoundExplainer.cc
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/Test_BoundExplainer.cc.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/common/real/CommonReal.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/common/real/Errno.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/common/real/FileFactory.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 96%] Building CXX object src/proofs/CMakeFiles/Test_BoundExplainer.dir/__/engine/real/TableauFactory.cpp.o
[ 96%] Linking CXX executable Test_BoundExplainer
[ 96%] Built target Test_BoundExplainer
[ 96%] Generating Test_Checker.cc
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/Test_Checker.cc.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/common/real/CommonReal.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/common/real/Errno.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/common/real/FileFactory.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 97%] Building CXX object src/proofs/CMakeFiles/Test_Checker.dir/__/engine/real/TableauFactory.cpp.o
[ 97%] Linking CXX executable Test_Checker
[ 97%] Built target Test_Checker
[ 98%] Generating Test_SmtLibWriter.cc
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/Test_SmtLibWriter.cc.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/common/real/CommonReal.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/common/real/Errno.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/common/real/FileFactory.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_SmtLibWriter.dir/__/engine/real/TableauFactory.cpp.o
[ 98%] Linking CXX executable Test_SmtLibWriter
[ 98%] Built target Test_SmtLibWriter
[ 98%] Generating Test_UnsatCertificateNode.cc
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/Test_UnsatCertificateNode.cc.o
[ 98%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/common/real/CommonReal.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/common/real/Errno.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/common/real/FileFactory.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/engine/real/ConstraintMatrixAnalyzerFactory.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/engine/real/CostFunctionManagerFactory.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/engine/real/ProjectedSteepestEdgeFactory.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/engine/real/RowBoundTightenerFactory.cpp.o
[ 99%] Building CXX object src/proofs/CMakeFiles/Test_UnsatCertificateNode.dir/__/engine/real/TableauFactory.cpp.o
[ 99%] Linking CXX executable Test_UnsatCertificateNode
[ 99%] Built target Test_UnsatCertificateNode
Test project /Users/victorg/Marabou/build
      Start  1: Test_AbsoluteValueConstraint
      Start  2: Test_BlandsRule
      Start  3: Test_BoundManager
      Start  4: Test_ConstraintMatrixAnalyzer
      Start  5: Test_CostFunctionManager
      Start  6: Test_DantzigsRule
      Start  7: Test_DegradationChecker
      Start  8: Test_DisjunctionConstraint
 1/70 Test  #2: Test_BlandsRule ....................   Passed    2.34 sec
      Start  9: Test_DnCWorker
 2/70 Test  #6: Test_DantzigsRule ..................   Passed    2.34 sec
      Start 10: Test_Engine
 3/70 Test  #4: Test_ConstraintMatrixAnalyzer ......   Passed    2.34 sec
      Start 11: Test_InputQuery
 4/70 Test  #7: Test_DegradationChecker ............   Passed    2.34 sec
      Start 12: Test_LargestIntervalDivider
 5/70 Test  #3: Test_BoundManager ..................   Passed    2.35 sec
      Start 13: Test_MaxConstraint
 6/70 Test  #5: Test_CostFunctionManager ...........   Passed    2.36 sec
      Start 14: Test_MILPEncoder
 7/70 Test  #1: Test_AbsoluteValueConstraint .......   Passed    2.36 sec
      Start 15: Test_PolarityBasedDivider
 8/70 Test  #8: Test_DisjunctionConstraint .........   Passed    2.36 sec
      Start 16: Test_Preprocessor
 9/70 Test #10: Test_Engine ........................   Passed    0.29 sec
      Start 17: Test_ProjectedSteepestEdge
10/70 Test  #9: Test_DnCWorker .....................   Passed    0.43 sec
      Start 18: Test_PseudoImpactTracker
11/70 Test #11: Test_InputQuery ....................   Passed    0.61 sec
      Start 19: Test_ReluConstraint
12/70 Test #12: Test_LargestIntervalDivider ........   Passed    0.76 sec
      Start 20: Test_RowBoundTightener
13/70 Test #13: Test_MaxConstraint .................   Passed    0.96 sec
      Start 21: Test_SignConstraint
14/70 Test #14: Test_MILPEncoder ...................   Passed    1.33 sec
      Start 22: Test_SigmoidConstraint
15/70 Test #15: Test_PolarityBasedDivider ..........   Passed    1.46 sec
      Start 23: Test_SmtCore
16/70 Test #16: Test_Preprocessor ..................   Passed    1.65 sec
      Start 24: Test_SumOfInfeasibilitiesManager
17/70 Test #17: Test_ProjectedSteepestEdge .........   Passed    1.52 sec
      Start 25: Test_Tableau
18/70 Test #18: Test_PseudoImpactTracker ...........   Passed    1.55 sec
      Start 26: Test_CSRMatrix
19/70 Test #19: Test_ReluConstraint ................   Passed    1.53 sec
      Start 27: Test_CompareFactorizations
20/70 Test #20: Test_RowBoundTightener .............   Passed    1.66 sec
      Start 28: Test_ForrestTomlinFactorization
21/70 Test #21: Test_SignConstraint ................   Passed    1.58 sec
      Start 29: Test_LUFactorization
22/70 Test #22: Test_SigmoidConstraint .............   Passed    1.37 sec
      Start 30: Test_LUFactors
23/70 Test #23: Test_SmtCore .......................   Passed    1.38 sec
      Start 31: Test_PermutationMatrix
24/70 Test #24: Test_SumOfInfeasibilitiesManager ...***Failed    1.35 sec
Running 8 tests...
In SumOfInfeasibilitiesManagerTestSuite::test_propose_phase_pattern_update_randomly:
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:341: Error: Expected (*soiManager-> getConstraintsUpdatedInLastProposal().begin() == plConstraints[1]), found ({ C0 2A 80 12 01 00 00 00  } != { 00 2C 80 12 01 00 00 00  })
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:343: Error: Expected (cost1 == soiManager->getCurrentSoIPhasePattern()), found ({ 50 AD A0 03 01 00 00 00 ... } != { D0 AB A0 03 01 00 00 00 ... })
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:347: Error: Expected (mock->randWasCalled == 3u), found (2 != 3)
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:368: Error: Expected (cost2 == soiManager->getCurrentSoIPhasePattern()), found ({ 10 C1 A0 03 01 00 00 00 ... } != { 50 BF A0 03 01 00 00 00 ... })
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:374: Error: Expected (*soiManager-> getConstraintsUpdatedInLastProposal().begin() == plConstraints[3]), found ({ 40 2D 80 12 01 00 00 00  } != { 40 6C 78 03 01 00 00 00  })
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:378: Error: Expected (cost2 == soiManager->getLastAcceptedSoIPhasePattern()), found ({ 50 D6 A0 03 01 00 00 00 ... } != { 90 D4 A0 03 01 00 00 00 ... })
/Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:379: Error: Expected (cost2 == soiManager->getCurrentSoIPhasePattern()), found ({ 90 CC A0 03 01 00 00 00 ... } != { D0 CA A0 03 01 00 00 00 ... })
....
Failed 1 of 8 tests
Success rate: 87%

      Start 32: Test_SparseFTFactorization
25/70 Test #25: Test_Tableau .......................   Passed    1.37 sec
      Start 33: Test_SparseGaussianEliminator
26/70 Test #26: Test_CSRMatrix .....................   Passed    1.52 sec
      Start 34: Test_SparseLUFactorization
27/70 Test #27: Test_CompareFactorizations .........   Passed    1.54 sec
      Start 35: Test_SparseLUFactors
28/70 Test #28: Test_ForrestTomlinFactorization ....   Passed    1.41 sec
      Start 36: Test_SparseUnsortedArray
29/70 Test #29: Test_LUFactorization ...............   Passed    1.43 sec
      Start 37: Test_SparseUnsortedArrays
30/70 Test #30: Test_LUFactors .....................   Passed    1.43 sec
      Start 38: Test_SparseUnsortedList
31/70 Test #31: Test_PermutationMatrix .............   Passed    1.64 sec
      Start 39: Test_SparseUnsortedLists
32/70 Test #32: Test_SparseFTFactorization .........   Passed    1.62 sec
      Start 40: Test_ConstSimpleData
33/70 Test #33: Test_SparseGaussianEliminator ......   Passed    1.61 sec
      Start 41: Test_Error
34/70 Test #34: Test_SparseLUFactorization .........   Passed    1.44 sec
      Start 42: Test_File
35/70 Test #35: Test_SparseLUFactors ...............   Passed    1.43 sec
      Start 43: Test_FloatUtils
36/70 Test #36: Test_SparseUnsortedArray ...........   Passed    1.42 sec
      Start 44: Test_GurobiWrapper
37/70 Test #37: Test_SparseUnsortedArrays ..........   Passed    1.55 sec
      Start 45: Test_HashMap
38/70 Test #38: Test_SparseUnsortedList ............   Passed    1.55 sec
      Start 46: Test_HashSet
39/70 Test #39: Test_SparseUnsortedLists ...........   Passed    1.35 sec
      Start 47: Test_HeapData
40/70 Test #40: Test_ConstSimpleData ...............   Passed    1.37 sec
      Start 48: Test_LinearExpression
41/70 Test #41: Test_Error .........................   Passed    1.36 sec
      Start 49: Test_List
42/70 Test #42: Test_File ..........................   Passed    1.36 sec
      Start 50: Test_MString
43/70 Test #43: Test_FloatUtils ....................   Passed    1.48 sec
      Start 51: Test_MStringf
44/70 Test #44: Test_GurobiWrapper .................   Passed    1.46 sec
      Start 52: Test_Map
45/70 Test #45: Test_HashMap .......................   Passed    1.36 sec
      Start 53: Test_Pair
46/70 Test #46: Test_HashSet .......................   Passed    1.35 sec
      Start 54: Test_Queue
47/70 Test #47: Test_HeapData ......................   Passed    1.35 sec
      Start 55: Test_Set
48/70 Test #48: Test_LinearExpression ..............   Passed    1.36 sec
      Start 56: Test_Stack
49/70 Test #49: Test_List ..........................   Passed    1.36 sec
      Start 57: Test_Vector
50/70 Test #50: Test_MString .......................   Passed    1.46 sec
      Start 58: Test_MatrixMultiplication
51/70 Test #51: Test_MStringf ......................   Passed    1.41 sec
      Start 68: Test_OnnxParser
52/70 Test #52: Test_Map ...........................   Passed    1.41 sec
      Start 69: Test_VnnLibParser
53/70 Test #53: Test_Pair ..........................   Passed    1.39 sec
      Start 70: Test_QueryLoader
54/70 Test #54: Test_Queue .........................   Passed    1.38 sec
      Start 71: Test_DeepPolyAnalysis
55/70 Test #55: Test_Set ...........................   Passed    1.47 sec
      Start 72: Test_NetworkLevelReasoner
56/70 Test #56: Test_Stack .........................   Passed    1.49 sec
      Start 73: Test_WsLayerElimination
57/70 Test #57: Test_Vector ........................   Passed    1.49 sec
      Start 74: Test_ParallelSolver
58/70 Test #58: Test_MatrixMultiplication ..........   Passed    1.39 sec
      Start 75: Test_BoundExplainer
59/70 Test #68: Test_OnnxParser ....................   Passed    1.33 sec
      Start 76: Test_Checker
60/70 Test #70: Test_QueryLoader ...................   Passed    1.56 sec
      Start 77: Test_SmtLibWriter
61/70 Test #71: Test_DeepPolyAnalysis ..............   Passed    1.45 sec
      Start 78: Test_UnsatCertificateNode
62/70 Test #72: Test_NetworkLevelReasoner ..........   Passed    1.37 sec
      Start 79: Test_UnsatCertificateUtils
63/70 Test #73: Test_WsLayerElimination ............   Passed    1.34 sec
64/70 Test #74: Test_ParallelSolver ................   Passed    1.33 sec
65/70 Test #75: Test_BoundExplainer ................   Passed    1.33 sec
66/70 Test #69: Test_VnnLibParser ..................   Passed    2.43 sec
67/70 Test #76: Test_Checker .......................   Passed    1.32 sec
68/70 Test #77: Test_SmtLibWriter ..................   Passed    1.00 sec
69/70 Test #78: Test_UnsatCertificateNode ..........   Passed    1.13 sec
70/70 Test #79: Test_UnsatCertificateUtils .........   Passed    1.17 sec

99% tests passed, 1 tests failed out of 70

Label Time Summary:
basis_factorization unit       =  20.94 sec*proc (14 tests)
common unit                    =  26.71 sec*proc (19 tests)
engine unit                    =  39.62 sec*proc (25 tests)
network_level_reasoner unit    =   5.49 sec*proc (4 tests)
parser unit                    =   3.76 sec*proc (2 tests)
proofs unit                    =   5.95 sec*proc (5 tests)
query_loader unit              =   1.56 sec*proc (1 test)

Total Test time (real) =  13.57 sec

The following tests FAILED:
	 24 - Test_SumOfInfeasibilitiesManager (Failed)
Errors while running CTest
make[2]: *** [build-tests] Error 8
make[1]: *** [CMakeFiles/build-tests.dir/all] Error 2
make: *** [all] Error 2
victorg@victors-air build % ctest -V -R Test_SumOfInfeasibilitiesManager
UpdateCTestConfiguration  from :/Users/victorg/Marabou/build/DartConfiguration.tcl
UpdateCTestConfiguration  from :/Users/victorg/Marabou/build/DartConfiguration.tcl
Test project /Users/victorg/Marabou/build
Constructing a list of tests
Done constructing a list of tests
Updating test list for fixtures
Added 0 tests to meet fixture requirements
Checking test dependency graph...
Checking test dependency graph end
test 24
    Start 24: Test_SumOfInfeasibilitiesManager

24: Test command: /Users/victorg/Marabou/build/tests/engine/Test_SumOfInfeasibilitiesManager
24: Working Directory: /Users/victorg/Marabou/build/src/engine
24: Test timeout computed to be: 10000000
24: Running 8 tests...
24: In SumOfInfeasibilitiesManagerTestSuite::test_propose_phase_pattern_update_randomly:
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:341: Error: Expected (*soiManager-> getConstraintsUpdatedInLastProposal().begin() == plConstraints[1]), found ({ C0 2A A0 14 01 00 00 00  } != { 00 2C A0 14 01 00 00 00  })
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:343: Error: Expected (cost1 == soiManager->getCurrentSoIPhasePattern()), found ({ 50 AD E0 05 01 00 00 00 ... } != { D0 AB E0 05 01 00 00 00 ... })
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:347: Error: Expected (mock->randWasCalled == 3u), found (2 != 3)
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:368: Error: Expected (cost2 == soiManager->getCurrentSoIPhasePattern()), found ({ 10 C1 E0 05 01 00 00 00 ... } != { 50 BF E0 05 01 00 00 00 ... })
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:374: Error: Expected (*soiManager-> getConstraintsUpdatedInLastProposal().begin() == plConstraints[3]), found ({ 40 2D A0 14 01 00 00 00  } != { 40 6C B8 05 01 00 00 00  })
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:378: Error: Expected (cost2 == soiManager->getLastAcceptedSoIPhasePattern()), found ({ 50 D6 E0 05 01 00 00 00 ... } != { 90 D4 E0 05 01 00 00 00 ... })
24: /Users/victorg/Marabou/src/engine/tests/Test_SumOfInfeasibilitiesManager.h:379: Error: Expected (cost2 == soiManager->getCurrentSoIPhasePattern()), found ({ 90 CC E0 05 01 00 00 00 ... } != { D0 CA E0 05 01 00 00 00 ... })
24: ....
24: Failed 1 of 8 tests
24: Success rate: 87%
1/1 Test #24: Test_SumOfInfeasibilitiesManager ...***Failed    0.06 sec

0% tests passed, 1 tests failed out of 1

Label Time Summary:
engine unit    =   0.06 sec*proc (1 test)

Total Test time (real) =   0.09 sec

The following tests FAILED:
	 24 - Test_SumOfInfeasibilitiesManager (Failed)
Errors while running CTest
Output from these tests are in: /Users/victorg/Marabou/build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
victorg@victors-air build % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

zsh: no such file or directory: ./build/Marabou
victorg@victors-air build % ls
CMakeCache.txt		Marabou			input_parsers		lp_infeasible_1.mps	tools
CMakeFiles		Testing			libMarabouHelper.a	regress
CTestTestfile.cmake	bin			libMarabouHelperTest.a	src
Makefile		cmake_install.cmake	lp_feasible_1.mps	tests
victorg@victors-air build % cd Marabou
cd: not a directory: Marabou
victorg@victors-air build % ls -l
total 228272
-rw-r--r--   1 victorg  staff      26952 Jan 31 15:25 CMakeCache.txt
drwxr-xr-x  21 victorg  staff        672 Jan 31 17:34 CMakeFiles
-rw-r--r--   1 victorg  staff        347 Jan 31 15:25 CTestTestfile.cmake
-rw-r--r--   1 victorg  staff     257407 Jan 31 15:25 Makefile
-rwxr-xr-x   1 victorg  staff    3388360 Jan 31 17:35 Marabou
drwxr-xr-x   3 victorg  staff         96 Jan 31 17:40 Testing
drwxr-xr-x   3 victorg  staff         96 Jan 31 17:35 bin
-rw-r--r--   1 victorg  staff       2191 Jan 31 15:25 cmake_install.cmake
drwxr-xr-x   2 victorg  staff         64 Jan 31 15:25 input_parsers
-rw-r--r--   1 victorg  staff    3590312 Jan 31 17:35 libMarabouHelper.a
-rw-r--r--   1 victorg  staff  109584856 Jan 31 17:36 libMarabouHelperTest.a
-rw-r--r--   1 victorg  staff        512 Jan 31 14:41 lp_feasible_1.mps
-rw-r--r--   1 victorg  staff        713 Jan 31 14:41 lp_infeasible_1.mps
drwxr-xr-x  12 victorg  staff        384 Jan 31 15:25 regress
drwxr-xr-x  15 victorg  staff        480 Jan 31 15:25 src
drwxr-xr-x  10 victorg  staff        320 Jan 31 15:25 tests
drwxr-xr-x   8 victorg  staff        256 Jan 31 15:25 tools
victorg@victors-air build % cd ..
victorg@victors-air Marabou % ./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt

Network: resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet
Number of layers: 8. Input layer size: 5. Output layer size: 5. Number of ReLUs: 300
Total number of variables: 610
Property: resources/properties/acas_property_3.txt

Engine::processInputQuery: Input query (before preprocessing): 309 equations, 610 variables
Engine::processInputQuery: Input query (after preprocessing): 609 equations, 838 variables

Input bounds:
	x0: [ -0.3035,  -0.2986] 
	x1: [ -0.0095,   0.0095] 
	x2: [  0.4934,   0.5000] 
	x3: [  0.3000,   0.5000] 
	x4: [  0.3000,   0.5000] 

Branching heuristics set to LargestInterval
unsat
victorg@victors-air Marabou % ./resources/runMarabou.py resources/nnet/mnist/mnist10x10.nnet resources/properties/mnist/image3_target6_epsilon0.05.txt --num-workers=4
/Users/victorg/Marabou/resources/../maraboupy/Marabou.py:27: UserWarning: Tensorflow parser is unavailable because tensorflow package is not installed
  warnings.warn("Tensorflow parser is unavailable because tensorflow package is not installed")
/Users/victorg/Marabou/resources/../maraboupy/Marabou.py:31: UserWarning: ONNX parser is unavailable because onnx or onnxruntime packages are not installed
  warnings.warn("ONNX parser is unavailable because onnx or onnxruntime packages are not installed")
Property: resources/properties/mnist/image3_target6_epsilon0.05.txt
Number of variables: 994
Number of lower bounds: 884
Number of upper bounds: 784
Number of equations: 119
Number of non-linear constraints: 100
Running Marabou with the following arguments:  ['--num-workers=4']
InputQuery: /tmp/tmpnqsr7fdd
Engine::processInputQuery: Input query (before preprocessing): 119 equations, 994 variables
Engine::processInputQuery: Input query (after preprocessing): 219 equations, 1102 variables

Input bounds:
	x0: [  0.0000,   0.0500] 
	x1: [  0.0000,   0.0500] 
	x2: [  0.0000,   0.0500] 
	x3: [  0.0000,   0.0500] 
	x4: [  0.0000,   0.0500] 
	x5: [  0.0000,   0.0500] 
	x6: [  0.0000,   0.0500] 
	x7: [  0.0000,   0.0500] 
	x8: [  0.0000,   0.0500] 
	x9: [  0.0000,   0.0500] 
	x10: [  0.0000,   0.0500] 
	x11: [  0.0000,   0.0500] 
	x12: [  0.0000,   0.0500] 
	x13: [  0.0000,   0.0500] 
	x14: [  0.0000,   0.0500] 
	x15: [  0.0000,   0.0500] 
	x16: [  0.0000,   0.0500] 
	x17: [  0.0000,   0.0500] 
	x18: [  0.0000,   0.0500] 
	x19: [  0.0000,   0.0500] 
	x20: [  0.0000,   0.0500] 
	x21: [  0.0000,   0.0500] 
	x22: [  0.0000,   0.0500] 
	x23: [  0.0000,   0.0500] 
	x24: [  0.0000,   0.0500] 
	x25: [  0.0000,   0.0500] 
	x26: [  0.0000,   0.0500] 
	x27: [  0.0000,   0.0500] 
	x28: [  0.0000,   0.0500] 
	x29: [  0.0000,   0.0500] 
	x30: [  0.0000,   0.0500] 
	x31: [  0.0000,   0.0500] 
	x32: [  0.0000,   0.0500] 
	x33: [  0.0000,   0.0500] 
	x34: [  0.0000,   0.0500] 
	x35: [  0.0000,   0.0500] 
	x36: [  0.0000,   0.0500] 
	x37: [  0.0000,   0.0500] 
	x38: [  0.0000,   0.0500] 
	x39: [  0.0000,   0.0500] 
	x40: [  0.0000,   0.0500] 
	x41: [  0.0000,   0.0500] 
	x42: [  0.0000,   0.0500] 
	x43: [  0.0000,   0.0500] 
	x44: [  0.0000,   0.0500] 
	x45: [  0.0000,   0.0500] 
	x46: [  0.0000,   0.0500] 
	x47: [  0.0000,   0.0500] 
	x48: [  0.0000,   0.0500] 
	x49: [  0.0000,   0.0500] 
	x50: [  0.0000,   0.0500] 
	x51: [  0.0000,   0.0500] 
	x52: [  0.0000,   0.0500] 
	x53: [  0.0000,   0.0500] 
	x54: [  0.0000,   0.0500] 
	x55: [  0.0000,   0.0500] 
	x56: [  0.0000,   0.0500] 
	x57: [  0.0000,   0.0500] 
	x58: [  0.0000,   0.0500] 
	x59: [  0.0000,   0.0500] 
	x60: [  0.0000,   0.0500] 
	x61: [  0.0000,   0.0500] 
	x62: [  0.0000,   0.0500] 
	x63: [  0.0000,   0.0500] 
	x64: [  0.0000,   0.0500] 
	x65: [  0.0000,   0.0500] 
	x66: [  0.0000,   0.0500] 
	x67: [  0.0000,   0.0500] 
	x68: [  0.0000,   0.0500] 
	x69: [  0.0000,   0.0500] 
	x70: [  0.0000,   0.0500] 
	x71: [  0.0000,   0.0500] 
	x72: [  0.0000,   0.0500] 
	x73: [  0.0000,   0.0500] 
	x74: [  0.0000,   0.0500] 
	x75: [  0.0000,   0.0500] 
	x76: [  0.0000,   0.0500] 
	x77: [  0.0000,   0.0500] 
	x78: [  0.0000,   0.0500] 
	x79: [  0.0000,   0.0500] 
	x80: [  0.0000,   0.0500] 
	x81: [  0.0000,   0.0500] 
	x82: [  0.0000,   0.0500] 
	x83: [  0.0000,   0.0500] 
	x84: [  0.0000,   0.0500] 
	x85: [  0.0000,   0.0500] 
	x86: [  0.0000,   0.0500] 
	x87: [  0.0000,   0.0500] 
	x88: [  0.0000,   0.0500] 
	x89: [  0.0000,   0.0500] 
	x90: [  0.0000,   0.0500] 
	x91: [  0.0000,   0.0500] 
	x92: [  0.0000,   0.0500] 
	x93: [  0.0000,   0.0500] 
	x94: [  0.0000,   0.0500] 
	x95: [  0.0000,   0.0500] 
	x96: [  0.0000,   0.0500] 
	x97: [  0.0000,   0.0500] 
	x98: [  0.0000,   0.0500] 
	x99: [  0.0000,   0.0500] 
	x100: [  0.0000,   0.0500] 
	x101: [  0.0000,   0.0500] 
	x102: [  0.0000,   0.0500] 
	x103: [  0.0000,   0.0500] 
	x104: [  0.0000,   0.0500] 
	x105: [  0.0000,   0.0500] 
	x106: [  0.0000,   0.0500] 
	x107: [  0.0000,   0.0500] 
	x108: [  0.0000,   0.0500] 
	x109: [  0.0000,   0.0500] 
	x110: [  0.0000,   0.0500] 
	x111: [  0.0000,   0.0500] 
	x112: [  0.0000,   0.0500] 
	x113: [  0.0000,   0.0500] 
	x114: [  0.0000,   0.0500] 
	x115: [  0.0000,   0.0500] 
	x116: [  0.0000,   0.0500] 
	x117: [  0.0000,   0.0500] 
	x118: [  0.0000,   0.0500] 
	x119: [  0.0000,   0.0500] 
	x120: [  0.0000,   0.0500] 
	x121: [  0.0000,   0.0500] 
	x122: [  0.0000,   0.0500] 
	x123: [  0.0000,   0.0500] 
	x124: [  0.0000,   0.0500] 
	x125: [  0.0000,   0.0500] 
	x126: [  0.0000,   0.0500] 
	x127: [  0.0000,   0.0500] 
	x128: [  0.0000,   0.0500] 
	x129: [  0.0000,   0.0500] 
	x130: [  0.0000,   0.0500] 
	x131: [  0.0000,   0.0500] 
	x132: [  0.0000,   0.0500] 
	x133: [  0.0000,   0.0500] 
	x134: [  0.0000,   0.0500] 
	x135: [  0.0000,   0.0500] 
	x136: [  0.0000,   0.0500] 
	x137: [  0.0000,   0.0500] 
	x138: [  0.0000,   0.0500] 
	x139: [  0.0000,   0.0500] 
	x140: [  0.0000,   0.0500] 
	x141: [  0.0000,   0.0500] 
	x142: [  0.0000,   0.0500] 
	x143: [  0.0000,   0.0500] 
	x144: [  0.0000,   0.0500] 
	x145: [  0.0000,   0.0500] 
	x146: [  0.0000,   0.0500] 
	x147: [  0.0000,   0.0500] 
	x148: [  0.0000,   0.0500] 
	x149: [  0.0000,   0.0500] 
	x150: [  0.0000,   0.0500] 
	x151: [  0.0000,   0.0500] 
	x152: [  0.0000,   0.0500] 
	x153: [  0.0000,   0.0500] 
	x154: [  0.0000,   0.0500] 
	x155: [  0.0000,   0.0500] 
	x156: [  0.0000,   0.0500] 
	x157: [  0.0000,   0.0500] 
	x158: [  0.4363,   0.5363] 
	x159: [  0.9422,   1.0000] 
	x160: [  0.9500,   1.0000] 
	x161: [  0.1971,   0.2971] 
	x162: [  0.0000,   0.0500] 
	x163: [  0.0000,   0.0500] 
	x164: [  0.0000,   0.0500] 
	x165: [  0.0000,   0.0500] 
	x166: [  0.0000,   0.0500] 
	x167: [  0.0000,   0.0500] 
	x168: [  0.0000,   0.0500] 
	x169: [  0.0000,   0.0500] 
	x170: [  0.0000,   0.0500] 
	x171: [  0.0000,   0.0500] 
	x172: [  0.0000,   0.0500] 
	x173: [  0.0000,   0.0500] 
	x174: [  0.0000,   0.0500] 
	x175: [  0.0000,   0.0500] 
	x176: [  0.0000,   0.0500] 
	x177: [  0.0000,   0.0500] 
	x178: [  0.0000,   0.0500] 
	x179: [  0.0000,   0.0500] 
	x180: [  0.0000,   0.0500] 
	x181: [  0.0000,   0.0500] 
	x182: [  0.0000,   0.0500] 
	x183: [  0.0000,   0.0500] 
	x184: [  0.0000,   0.0500] 
	x185: [  0.3265,   0.4265] 
	x186: [  0.9069,   1.0000] 
	x187: [  0.9343,   1.0000] 
	x188: [  0.9422,   1.0000] 
	x189: [  0.1931,   0.2931] 
	x190: [  0.0000,   0.0500] 
	x191: [  0.0000,   0.0500] 
	x192: [  0.0000,   0.0500] 
	x193: [  0.0000,   0.0500] 
	x194: [  0.0000,   0.0500] 
	x195: [  0.0000,   0.0500] 
	x196: [  0.0000,   0.0500] 
	x197: [  0.0000,   0.0500] 
	x198: [  0.0000,   0.0500] 
	x199: [  0.0000,   0.0500] 
	x200: [  0.0000,   0.0500] 
	x201: [  0.0000,   0.0500] 
	x202: [  0.0000,   0.0500] 
	x203: [  0.0000,   0.0500] 
	x204: [  0.0000,   0.0500] 
	x205: [  0.0000,   0.0500] 
	x206: [  0.0000,   0.0500] 
	x207: [  0.0000,   0.0500] 
	x208: [  0.0000,   0.0500] 
	x209: [  0.0000,   0.0500] 
	x210: [  0.0000,   0.0500] 
	x211: [  0.0000,   0.0500] 
	x212: [  0.0000,   0.0500] 
	x213: [  0.4480,   0.5480] 
	x214: [  0.9343,   1.0000] 
	x215: [  0.9343,   1.0000] 
	x216: [  0.9422,   1.0000] 
	x217: [  0.1931,   0.2931] 
	x218: [  0.0000,   0.0500] 
	x219: [  0.0000,   0.0500] 
	x220: [  0.0000,   0.0500] 
	x221: [  0.0000,   0.0500] 
	x222: [  0.0000,   0.0500] 
	x223: [  0.0000,   0.0500] 
	x224: [  0.0000,   0.0500] 
	x225: [  0.0000,   0.0500] 
	x226: [  0.0000,   0.0500] 
	x227: [  0.0000,   0.0500] 
	x228: [  0.0000,   0.0500] 
	x229: [  0.0000,   0.0500] 
	x230: [  0.0000,   0.0500] 
	x231: [  0.0000,   0.0500] 
	x232: [  0.0000,   0.0500] 
	x233: [  0.0000,   0.0500] 
	x234: [  0.0000,   0.0500] 
	x235: [  0.0000,   0.0500] 
	x236: [  0.0000,   0.0500] 
	x237: [  0.0000,   0.0500] 
	x238: [  0.0000,   0.0500] 
	x239: [  0.0000,   0.0500] 
	x240: [  0.2167,   0.3167] 
	x241: [  0.8755,   0.9755] 
	x242: [  0.9343,   1.0000] 
	x243: [  0.7775,   0.8775] 
	x244: [  0.0716,   0.1716] 
	x245: [  0.0000,   0.0814] 
	x246: [  0.0000,   0.0500] 
	x247: [  0.0000,   0.0500] 
	x248: [  0.0000,   0.0500] 
	x249: [  0.0000,   0.0500] 
	x250: [  0.0000,   0.0500] 
	x251: [  0.0000,   0.0500] 
	x252: [  0.0000,   0.0500] 
	x253: [  0.0000,   0.0500] 
	x254: [  0.0000,   0.0500] 
	x255: [  0.0000,   0.0500] 
	x256: [  0.0000,   0.0500] 
	x257: [  0.0000,   0.0500] 
	x258: [  0.0000,   0.0500] 
	x259: [  0.0000,   0.0500] 
	x260: [  0.0000,   0.0500] 
	x261: [  0.0000,   0.0500] 
	x262: [  0.0000,   0.0500] 
	x263: [  0.0000,   0.0500] 
	x264: [  0.0000,   0.0500] 
	x265: [  0.0000,   0.0500] 
	x266: [  0.0000,   0.0500] 
	x267: [  0.1853,   0.2853] 
	x268: [  0.8441,   0.9441] 
	x269: [  0.9343,   1.0000] 
	x270: [  0.9343,   1.0000] 
	x271: [  0.3186,   0.4186] 
	x272: [  0.0000,   0.0500] 
	x273: [  0.0000,   0.0500] 
	x274: [  0.0000,   0.0500] 
	x275: [  0.0000,   0.0500] 
	x276: [  0.0000,   0.0500] 
	x277: [  0.0000,   0.0500] 
	x278: [  0.0000,   0.0500] 
	x279: [  0.0000,   0.0500] 
	x280: [  0.0000,   0.0500] 
	x281: [  0.0000,   0.0500] 
	x282: [  0.0000,   0.0500] 
	x283: [  0.0000,   0.0500] 
	x284: [  0.0000,   0.0500] 
	x285: [  0.0000,   0.0500] 
	x286: [  0.0000,   0.0500] 
	x287: [  0.0000,   0.0500] 
	x288: [  0.0000,   0.0500] 
	x289: [  0.0000,   0.0500] 
	x290: [  0.0000,   0.0500] 
	x291: [  0.0000,   0.0500] 
	x292: [  0.0000,   0.0500] 
	x293: [  0.0000,   0.0500] 
	x294: [  0.0000,   0.0500] 
	x295: [  0.5578,   0.6578] 
	x296: [  0.9422,   1.0000] 
	x297: [  0.9422,   1.0000] 
	x298: [  0.6912,   0.7912] 
	x299: [  0.0000,   0.0500] 
	x300: [  0.0000,   0.0500] 
	x301: [  0.0000,   0.0500] 
	x302: [  0.0000,   0.0500] 
	x303: [  0.0000,   0.0500] 
	x304: [  0.0000,   0.0500] 
	x305: [  0.0000,   0.0500] 
	x306: [  0.0000,   0.0500] 
	x307: [  0.0000,   0.0500] 
	x308: [  0.0000,   0.0500] 
	x309: [  0.0000,   0.0500] 
	x310: [  0.0000,   0.0500] 
	x311: [  0.0000,   0.0500] 
	x312: [  0.0000,   0.0500] 
	x313: [  0.0000,   0.0500] 
	x314: [  0.0000,   0.0500] 
	x315: [  0.0000,   0.0500] 
	x316: [  0.0000,   0.0500] 
	x317: [  0.0000,   0.0500] 
	x318: [  0.0000,   0.0500] 
	x319: [  0.0000,   0.0500] 
	x320: [  0.0000,   0.0500] 
	x321: [  0.0000,   0.0500] 
	x322: [  0.0284,   0.1284] 
	x323: [  0.9422,   1.0000] 
	x324: [  0.9343,   1.0000] 
	x325: [  0.8716,   0.9716] 
	x326: [  0.2088,   0.3088] 
	x327: [  0.0000,   0.0500] 
	x328: [  0.0000,   0.0500] 
	x329: [  0.0000,   0.0500] 
	x330: [  0.0000,   0.0500] 
	x331: [  0.0000,   0.0500] 
	x332: [  0.0000,   0.0500] 
	x333: [  0.0000,   0.0500] 
	x334: [  0.0000,   0.0500] 
	x335: [  0.0000,   0.0500] 
	x336: [  0.0000,   0.0500] 
	x337: [  0.0000,   0.0500] 
	x338: [  0.0000,   0.0500] 
	x339: [  0.0000,   0.0500] 
	x340: [  0.0000,   0.0500] 
	x341: [  0.0000,   0.0500] 
	x342: [  0.0000,   0.0500] 
	x343: [  0.0000,   0.0500] 
	x344: [  0.0000,   0.0500] 
	x345: [  0.0000,   0.0500] 
	x346: [  0.0000,   0.0500] 
	x347: [  0.0000,   0.0500] 
	x348: [  0.0000,   0.0500] 
	x349: [  0.0755,   0.1755] 
	x350: [  0.7539,   0.8539] 
	x351: [  0.9422,   1.0000] 
	x352: [  0.9343,   1.0000] 
	x353: [  0.4441,   0.5441] 
	x354: [  0.0000,   0.0500] 
	x355: [  0.0000,   0.0500] 
	x356: [  0.0000,   0.0500] 
	x357: [  0.0000,   0.0500] 
	x358: [  0.0000,   0.0500] 
	x359: [  0.0000,   0.0500] 
	x360: [  0.0000,   0.0500] 
	x361: [  0.0000,   0.0500] 
	x362: [  0.0000,   0.0500] 
	x363: [  0.0000,   0.0500] 
	x364: [  0.0000,   0.0500] 
	x365: [  0.0000,   0.0500] 
	x366: [  0.0000,   0.0500] 
	x367: [  0.0000,   0.0500] 
	x368: [  0.0000,   0.0500] 
	x369: [  0.0000,   0.0500] 
	x370: [  0.0000,   0.0500] 
	x371: [  0.0000,   0.0500] 
	x372: [  0.0000,   0.0500] 
	x373: [  0.0000,   0.0500] 
	x374: [  0.0000,   0.0500] 
	x375: [  0.0000,   0.0500] 
	x376: [  0.0000,   0.0500] 
	x377: [  0.3578,   0.4578] 
	x378: [  0.9343,   1.0000] 
	x379: [  0.9422,   1.0000] 
	x380: [  0.6716,   0.7716] 
	x381: [  0.0088,   0.1088] 
	x382: [  0.0000,   0.0500] 
	x383: [  0.0000,   0.0500] 
	x384: [  0.0000,   0.0500] 
	x385: [  0.0000,   0.0500] 
	x386: [  0.0000,   0.0500] 
	x387: [  0.0000,   0.0500] 
	x388: [  0.0000,   0.0500] 
	x389: [  0.0000,   0.0500] 
	x390: [  0.0000,   0.0500] 
	x391: [  0.0000,   0.0500] 
	x392: [  0.0000,   0.0500] 
	x393: [  0.0000,   0.0500] 
	x394: [  0.0000,   0.0500] 
	x395: [  0.0000,   0.0500] 
	x396: [  0.0000,   0.0500] 
	x397: [  0.0000,   0.0500] 
	x398: [  0.0000,   0.0500] 
	x399: [  0.0000,   0.0500] 
	x400: [  0.0000,   0.0500] 
	x401: [  0.0000,   0.0500] 
	x402: [  0.0000,   0.0500] 
	x403: [  0.0000,   0.0500] 
	x404: [  0.2637,   0.3637] 
	x405: [  0.8912,   0.9912] 
	x406: [  0.9343,   1.0000] 
	x407: [  0.7069,   0.8069] 
	x408: [  0.0402,   0.1402] 
	x409: [  0.0000,   0.0500] 
	x410: [  0.0000,   0.0500] 
	x411: [  0.0000,   0.0500] 
	x412: [  0.0000,   0.0500] 
	x413: [  0.0000,   0.0500] 
	x414: [  0.0000,   0.0500] 
	x415: [  0.0000,   0.0500] 
	x416: [  0.0000,   0.0500] 
	x417: [  0.0000,   0.0500] 
	x418: [  0.0000,   0.0500] 
	x419: [  0.0000,   0.0500] 
	x420: [  0.0000,   0.0500] 
	x421: [  0.0000,   0.0500] 
	x422: [  0.0000,   0.0500] 
	x423: [  0.0000,   0.0500] 
	x424: [  0.0000,   0.0500] 
	x425: [  0.0000,   0.0500] 
	x426: [  0.0000,   0.0500] 
	x427: [  0.0000,   0.0500] 
	x428: [  0.0000,   0.0500] 
	x429: [  0.0000,   0.0500] 
	x430: [  0.0000,   0.0500] 
	x431: [  0.0755,   0.1755] 
	x432: [  0.9422,   1.0000] 
	x433: [  0.9422,   1.0000] 
	x434: [  0.9422,   1.0000] 
	x435: [  0.5735,   0.6735] 
	x436: [  0.0000,   0.0500] 
	x437: [  0.0000,   0.0500] 
	x438: [  0.0000,   0.0500] 
	x439: [  0.0000,   0.0500] 
	x440: [  0.0000,   0.0500] 
	x441: [  0.0000,   0.0500] 
	x442: [  0.0000,   0.0500] 
	x443: [  0.0000,   0.0500] 
	x444: [  0.0000,   0.0500] 
	x445: [  0.0000,   0.0500] 
	x446: [  0.0000,   0.0500] 
	x447: [  0.0000,   0.0500] 
	x448: [  0.0000,   0.0500] 
	x449: [  0.0000,   0.0500] 
	x450: [  0.0000,   0.0500] 
	x451: [  0.0000,   0.0500] 
	x452: [  0.0000,   0.0500] 
	x453: [  0.0000,   0.0500] 
	x454: [  0.0000,   0.0500] 
	x455: [  0.0000,   0.0500] 
	x456: [  0.0000,   0.0500] 
	x457: [  0.0000,   0.0500] 
	x458: [  0.0000,   0.0500] 
	x459: [  0.5422,   0.6422] 
	x460: [  0.9343,   1.0000] 
	x461: [  0.9343,   1.0000] 
	x462: [  0.9343,   1.0000] 
	x463: [  0.1029,   0.2029] 
	x464: [  0.0000,   0.0500] 
	x465: [  0.0000,   0.0500] 
	x466: [  0.0000,   0.0500] 
	x467: [  0.0000,   0.0500] 
	x468: [  0.0000,   0.0500] 
	x469: [  0.0000,   0.0500] 
	x470: [  0.0000,   0.0500] 
	x471: [  0.0000,   0.0500] 
	x472: [  0.0000,   0.0500] 
	x473: [  0.0000,   0.0500] 
	x474: [  0.0000,   0.0500] 
	x475: [  0.0000,   0.0500] 
	x476: [  0.0000,   0.0500] 
	x477: [  0.0000,   0.0500] 
	x478: [  0.0000,   0.0500] 
	x479: [  0.0000,   0.0500] 
	x480: [  0.0000,   0.0500] 
	x481: [  0.0000,   0.0500] 
	x482: [  0.0000,   0.0500] 
	x483: [  0.0000,   0.0500] 
	x484: [  0.0000,   0.0500] 
	x485: [  0.0000,   0.0500] 
	x486: [  0.1382,   0.2382] 
	x487: [  0.8167,   0.9167] 
	x488: [  0.9343,   1.0000] 
	x489: [  0.9343,   1.0000] 
	x490: [  0.6245,   0.7245] 
	x491: [  0.0000,   0.0500] 
	x492: [  0.0000,   0.0500] 
	x493: [  0.0000,   0.0500] 
	x494: [  0.0000,   0.0500] 
	x495: [  0.0000,   0.0500] 
	x496: [  0.0000,   0.0500] 
	x497: [  0.0000,   0.0500] 
	x498: [  0.0000,   0.0500] 
	x499: [  0.0000,   0.0500] 
	x500: [  0.0000,   0.0500] 
	x501: [  0.0000,   0.0500] 
	x502: [  0.0000,   0.0500] 
	x503: [  0.0000,   0.0500] 
	x504: [  0.0000,   0.0500] 
	x505: [  0.0000,   0.0500] 
	x506: [  0.0000,   0.0500] 
	x507: [  0.0000,   0.0500] 
	x508: [  0.0000,   0.0500] 
	x509: [  0.0000,   0.0500] 
	x510: [  0.0000,   0.0500] 
	x511: [  0.0000,   0.0500] 
	x512: [  0.0000,   0.0500] 
	x513: [  0.0000,   0.0500] 
	x514: [  0.8676,   0.9676] 
	x515: [  0.9343,   1.0000] 
	x516: [  0.9343,   1.0000] 
	x517: [  0.7186,   0.8186] 
	x518: [  0.0000,   0.0971] 
	x519: [  0.0000,   0.0500] 
	x520: [  0.0000,   0.0500] 
	x521: [  0.0000,   0.0500] 
	x522: [  0.0000,   0.0500] 
	x523: [  0.0000,   0.0500] 
	x524: [  0.0000,   0.0500] 
	x525: [  0.0000,   0.0500] 
	x526: [  0.0000,   0.0500] 
	x527: [  0.0000,   0.0500] 
	x528: [  0.0000,   0.0500] 
	x529: [  0.0000,   0.0500] 
	x530: [  0.0000,   0.0500] 
	x531: [  0.0000,   0.0500] 
	x532: [  0.0000,   0.0500] 
	x533: [  0.0000,   0.0500] 
	x534: [  0.0000,   0.0500] 
	x535: [  0.0000,   0.0500] 
	x536: [  0.0000,   0.0500] 
	x537: [  0.0000,   0.0500] 
	x538: [  0.0000,   0.0500] 
	x539: [  0.0000,   0.0500] 
	x540: [  0.0000,   0.0500] 
	x541: [  0.0000,   0.0500] 
	x542: [  0.9422,   1.0000] 
	x543: [  0.9343,   1.0000] 
	x544: [  0.9343,   1.0000] 
	x545: [  0.2990,   0.3990] 
	x546: [  0.0000,   0.0500] 
	x547: [  0.0000,   0.0500] 
	x548: [  0.0000,   0.0500] 
	x549: [  0.0000,   0.0500] 
	x550: [  0.0000,   0.0500] 
	x551: [  0.0000,   0.0500] 
	x552: [  0.0000,   0.0500] 
	x553: [  0.0000,   0.0500] 
	x554: [  0.0000,   0.0500] 
	x555: [  0.0000,   0.0500] 
	x556: [  0.0000,   0.0500] 
	x557: [  0.0000,   0.0500] 
	x558: [  0.0000,   0.0500] 
	x559: [  0.0000,   0.0500] 
	x560: [  0.0000,   0.0500] 
	x561: [  0.0000,   0.0500] 
	x562: [  0.0000,   0.0500] 
	x563: [  0.0000,   0.0500] 
	x564: [  0.0000,   0.0500] 
	x565: [  0.0000,   0.0500] 
	x566: [  0.0000,   0.0500] 
	x567: [  0.0000,   0.0500] 
	x568: [  0.0000,   0.0500] 
	x569: [  0.5735,   0.6735] 
	x570: [  0.9500,   1.0000] 
	x571: [  0.9422,   1.0000] 
	x572: [  0.9422,   1.0000] 
	x573: [  0.0716,   0.1716] 
	x574: [  0.0000,   0.0500] 
	x575: [  0.0000,   0.0500] 
	x576: [  0.0000,   0.0500] 
	x577: [  0.0000,   0.0500] 
	x578: [  0.0000,   0.0500] 
	x579: [  0.0000,   0.0500] 
	x580: [  0.0000,   0.0500] 
	x581: [  0.0000,   0.0500] 
	x582: [  0.0000,   0.0500] 
	x583: [  0.0000,   0.0500] 
	x584: [  0.0000,   0.0500] 
	x585: [  0.0000,   0.0500] 
	x586: [  0.0000,   0.0500] 
	x587: [  0.0000,   0.0500] 
	x588: [  0.0000,   0.0500] 
	x589: [  0.0000,   0.0500] 
	x590: [  0.0000,   0.0500] 
	x591: [  0.0000,   0.0500] 
	x592: [  0.0000,   0.0500] 
	x593: [  0.0000,   0.0500] 
	x594: [  0.0000,   0.0500] 
	x595: [  0.0000,   0.0500] 
	x596: [  0.1382,   0.2382] 
	x597: [  0.8441,   0.9441] 
	x598: [  0.9422,   1.0000] 
	x599: [  0.9186,   1.0000] 
	x600: [  0.4990,   0.5990] 
	x601: [  0.0000,   0.0814] 
	x602: [  0.0000,   0.0500] 
	x603: [  0.0000,   0.0500] 
	x604: [  0.0000,   0.0500] 
	x605: [  0.0000,   0.0500] 
	x606: [  0.0000,   0.0500] 
	x607: [  0.0000,   0.0500] 
	x608: [  0.0000,   0.0500] 
	x609: [  0.0000,   0.0500] 
	x610: [  0.0000,   0.0500] 
	x611: [  0.0000,   0.0500] 
	x612: [  0.0000,   0.0500] 
	x613: [  0.0000,   0.0500] 
	x614: [  0.0000,   0.0500] 
	x615: [  0.0000,   0.0500] 
	x616: [  0.0000,   0.0500] 
	x617: [  0.0000,   0.0500] 
	x618: [  0.0000,   0.0500] 
	x619: [  0.0000,   0.0500] 
	x620: [  0.0000,   0.0500] 
	x621: [  0.0000,   0.0500] 
	x622: [  0.0000,   0.0500] 
	x623: [  0.0000,   0.0500] 
	x624: [  0.2010,   0.3010] 
	x625: [  0.9343,   1.0000] 
	x626: [  0.9422,   1.0000] 
	x627: [  0.8127,   0.9127] 
	x628: [  0.0000,   0.0500] 
	x629: [  0.0000,   0.0500] 
	x630: [  0.0000,   0.0500] 
	x631: [  0.0000,   0.0500] 
	x632: [  0.0000,   0.0500] 
	x633: [  0.0000,   0.0500] 
	x634: [  0.0000,   0.0500] 
	x635: [  0.0000,   0.0500] 
	x636: [  0.0000,   0.0500] 
	x637: [  0.0000,   0.0500] 
	x638: [  0.0000,   0.0500] 
	x639: [  0.0000,   0.0500] 
	x640: [  0.0000,   0.0500] 
	x641: [  0.0000,   0.0500] 
	x642: [  0.0000,   0.0500] 
	x643: [  0.0000,   0.0500] 
	x644: [  0.0000,   0.0500] 
	x645: [  0.0000,   0.0500] 
	x646: [  0.0000,   0.0500] 
	x647: [  0.0000,   0.0500] 
	x648: [  0.0000,   0.0500] 
	x649: [  0.0000,   0.0500] 
	x650: [  0.0000,   0.0500] 
	x651: [  0.0000,   0.0500] 
	x652: [  0.2010,   0.3010] 
	x653: [  0.9343,   1.0000] 
	x654: [  0.9422,   1.0000] 
	x655: [  0.8127,   0.9127] 
	x656: [  0.0000,   0.0500] 
	x657: [  0.0000,   0.0500] 
	x658: [  0.0000,   0.0500] 
	x659: [  0.0000,   0.0500] 
	x660: [  0.0000,   0.0500] 
	x661: [  0.0000,   0.0500] 
	x662: [  0.0000,   0.0500] 
	x663: [  0.0000,   0.0500] 
	x664: [  0.0000,   0.0500] 
	x665: [  0.0000,   0.0500] 
	x666: [  0.0000,   0.0500] 
	x667: [  0.0000,   0.0500] 
	x668: [  0.0000,   0.0500] 
	x669: [  0.0000,   0.0500] 
	x670: [  0.0000,   0.0500] 
	x671: [  0.0000,   0.0500] 
	x672: [  0.0000,   0.0500] 
	x673: [  0.0000,   0.0500] 
	x674: [  0.0000,   0.0500] 
	x675: [  0.0000,   0.0500] 
	x676: [  0.0000,   0.0500] 
	x677: [  0.0000,   0.0500] 
	x678: [  0.0000,   0.0500] 
	x679: [  0.0000,   0.0500] 
	x680: [  0.0441,   0.1441] 
	x681: [  0.7069,   0.8069] 
	x682: [  0.9422,   1.0000] 
	x683: [  0.8127,   0.9127] 
	x684: [  0.0000,   0.0500] 
	x685: [  0.0000,   0.0500] 
	x686: [  0.0000,   0.0500] 
	x687: [  0.0000,   0.0500] 
	x688: [  0.0000,   0.0500] 
	x689: [  0.0000,   0.0500] 
	x690: [  0.0000,   0.0500] 
	x691: [  0.0000,   0.0500] 
	x692: [  0.0000,   0.0500] 
	x693: [  0.0000,   0.0500] 
	x694: [  0.0000,   0.0500] 
	x695: [  0.0000,   0.0500] 
	x696: [  0.0000,   0.0500] 
	x697: [  0.0000,   0.0500] 
	x698: [  0.0000,   0.0500] 
	x699: [  0.0000,   0.0500] 
	x700: [  0.0000,   0.0500] 
	x701: [  0.0000,   0.0500] 
	x702: [  0.0000,   0.0500] 
	x703: [  0.0000,   0.0500] 
	x704: [  0.0000,   0.0500] 
	x705: [  0.0000,   0.0500] 
	x706: [  0.0000,   0.0500] 
	x707: [  0.0000,   0.0500] 
	x708: [  0.0000,   0.0500] 
	x709: [  0.0000,   0.0500] 
	x710: [  0.0000,   0.0500] 
	x711: [  0.0000,   0.0500] 
	x712: [  0.0000,   0.0500] 
	x713: [  0.0000,   0.0500] 
	x714: [  0.0000,   0.0500] 
	x715: [  0.0000,   0.0500] 
	x716: [  0.0000,   0.0500] 
	x717: [  0.0000,   0.0500] 
	x718: [  0.0000,   0.0500] 
	x719: [  0.0000,   0.0500] 
	x720: [  0.0000,   0.0500] 
	x721: [  0.0000,   0.0500] 
	x722: [  0.0000,   0.0500] 
	x723: [  0.0000,   0.0500] 
	x724: [  0.0000,   0.0500] 
	x725: [  0.0000,   0.0500] 
	x726: [  0.0000,   0.0500] 
	x727: [  0.0000,   0.0500] 
	x728: [  0.0000,   0.0500] 
	x729: [  0.0000,   0.0500] 
	x730: [  0.0000,   0.0500] 
	x731: [  0.0000,   0.0500] 
	x732: [  0.0000,   0.0500] 
	x733: [  0.0000,   0.0500] 
	x734: [  0.0000,   0.0500] 
	x735: [  0.0000,   0.0500] 
	x736: [  0.0000,   0.0500] 
	x737: [  0.0000,   0.0500] 
	x738: [  0.0000,   0.0500] 
	x739: [  0.0000,   0.0500] 
	x740: [  0.0000,   0.0500] 
	x741: [  0.0000,   0.0500] 
	x742: [  0.0000,   0.0500] 
	x743: [  0.0000,   0.0500] 
	x744: [  0.0000,   0.0500] 
	x745: [  0.0000,   0.0500] 
	x746: [  0.0000,   0.0500] 
	x747: [  0.0000,   0.0500] 
	x748: [  0.0000,   0.0500] 
	x749: [  0.0000,   0.0500] 
	x750: [  0.0000,   0.0500] 
	x751: [  0.0000,   0.0500] 
	x752: [  0.0000,   0.0500] 
	x753: [  0.0000,   0.0500] 
	x754: [  0.0000,   0.0500] 
	x755: [  0.0000,   0.0500] 
	x756: [  0.0000,   0.0500] 
	x757: [  0.0000,   0.0500] 
	x758: [  0.0000,   0.0500] 
	x759: [  0.0000,   0.0500] 
	x760: [  0.0000,   0.0500] 
	x761: [  0.0000,   0.0500] 
	x762: [  0.0000,   0.0500] 
	x763: [  0.0000,   0.0500] 
	x764: [  0.0000,   0.0500] 
	x765: [  0.0000,   0.0500] 
	x766: [  0.0000,   0.0500] 
	x767: [  0.0000,   0.0500] 
	x768: [  0.0000,   0.0500] 
	x769: [  0.0000,   0.0500] 
	x770: [  0.0000,   0.0500] 
	x771: [  0.0000,   0.0500] 
	x772: [  0.0000,   0.0500] 
	x773: [  0.0000,   0.0500] 
	x774: [  0.0000,   0.0500] 
	x775: [  0.0000,   0.0500] 
	x776: [  0.0000,   0.0500] 
	x777: [  0.0000,   0.0500] 
	x778: [  0.0000,   0.0500] 
	x779: [  0.0000,   0.0500] 
	x780: [  0.0000,   0.0500] 
	x781: [  0.0000,   0.0500] 
	x782: [  0.0000,   0.0500] 
	x783: [  0.0000,   0.0500] 

Branching heuristics set to PseudoImpact

Engine::solve: Initial statistics

18:30:57 Statistics update:
	--- Time Statistics ---
	Total time elapsed: 70 milli (00:00:00)
		Main loop: 0 milli (00:00:00)
		Preprocessing time: 45 milli (00:00:00)
		Unknown: 25 milli (00:00:00)
	Breakdown for main loop:
		[0.00%] Simplex steps: 0 milli
		[0.00%] Explicit-basis bound tightening: 0 milli
		[0.00%] Constraint-matrix bound tightening: 0 milli
		[0.00%] Degradation checking: 0 milli
		[0.00%] Precision restoration: 0 milli
		[0.00%] Statistics handling: 0 milli
		[0.00%] Constraint-fixing steps: 0 milli
		[0.00%] Valid case splits: 0 milli. Average per split: 0.00 milli
		[0.00%] Applying stored bound-tightening: 0 milli
		[0.00%] SMT core: 0 milli
		[0.00%] Symbolic Bound Tightening: 6 milli
		[0.00%] SoI-based local search: 0 milli
		[0.00%] SoI-based local search: 0 milli
		[0.00%] Unaccounted for: 0 milli
	--- Preprocessor Statistics ---
	Number of preprocessor bound-tightening loop iterations: 48
	Number of eliminated variables: 1
	Number of constraints removed due to variable elimination: 1
	Number of equations removed due to variable elimination: 0
	--- Engine Statistics ---
	Number of main loop iterations: 1
		0 iterations were simplex steps. Total time: 0 milli. Average: 0.00 milli.
		0 iterations were constraint-fixing steps. Total time: 0 milli. Average: 0.00 milli
	Number of active piecewise-linear constraints: 99 / 99
		Constraints disabled by valid splits: 0. By SMT-originated splits: 0
	Last reported degradation: 0.0000000000. Max degradation so far: 0.0000000000. Restorations so far: 0
	Number of simplex pivots we attempted to skip because of instability: 0.
	Unstable pivots performed anyway: 0
	--- Tableau Statistics ---
	Total number of pivots performed: 0
		Real pivots: 0. Degenerate: 0 (0.00%)
		Degenerate pivots by request (e.g., to fix a PL constraint): 0 (0.00%)
		Average time per pivot: 0.00 milli
	Total number of fake pivots performed: 0
	Total number of rows added: 0. Number of merged columns: 0
	Current tableau dimensions: M = 219, N = 1321
	--- SMT Core Statistics ---
	Total depth is 0. Total visited states: 1. Number of splits: 0. Number of pops: 0
	Max stack depth: 0
	--- Bound Tightening Statistics ---
	Number of tightened bounds: 0.
		Number of rows examined by row tightener: 0. Consequent tightenings: 0
		Number of explicit basis matrices examined by row tightener: 0. Consequent tightenings: 0
		Number of bound tightening rounds on the entire constraint matrix: 0. Consequent tightenings: 0
		Number of bound notifications sent to PL constraints: 594. Tightenings proposed: 0
	--- Basis Factorization statistics ---
	Number of basis refactorizations: 2
	--- Projected Steepest Edge Statistics ---
	Number of iterations: 0.
	Number of resets to reference space: 1. Avg. iterations per reset: 0
	--- SBT ---
	Number of tightened bounds: 297
	--- SoI-based local search ---
	Number of proposed phase pattern update: 0. Number of accepted update: 0 [0.00%]
	Total time (% of local search time) updating SoI phase pattern : 0 milli [0.00%]
	Total time obtaining current assignment: 0 milli [0.00%]
	Total time getting SoI phase pattern : 0 milli [0.00%]
	--- Context dependent statistics ---
	Number of pushes / pops: 0 / 0
		[0.00%] Pre-Push hook: 0 milli
		[0.00%] Push : 0 milli
		[0.00%] Post-Pop hook: 0 milli
		[0.00%] Pop : 0 milli
		[0.00%] Total context-switching time: 0 milli
	--- Proof Certificate ---
	Number of certified leaves: 0
	Number of leaves to delegate: 0

---

Engine::solve: sat assignment found

18:30:58 Statistics update:
	--- Time Statistics ---
	Total time elapsed: 1220 milli (00:00:01)
		Main loop: 1149 milli (00:00:01)
		Preprocessing time: 45 milli (00:00:00)
		Unknown: 25 milli (00:00:00)
	Breakdown for main loop:
		[85.04%] Simplex steps: 977 milli
		[3.04%] Explicit-basis bound tightening: 34 milli
		[0.00%] Constraint-matrix bound tightening: 0 milli
		[0.55%] Degradation checking: 6 milli
		[0.00%] Precision restoration: 0 milli
		[0.26%] Statistics handling: 3 milli
		[0.00%] Constraint-fixing steps: 0 milli
		[0.00%] Valid case splits: 0 milli. Average per split: 0.00 milli
		[0.02%] Applying stored bound-tightening: 0 milli
		[0.08%] SMT core: 0 milli
		[8.29%] Symbolic Bound Tightening: 95 milli
		[71.89%] SoI-based local search: 826 milli
		[0.00%] SoI-based local search: 0 milli
		[2.71%] Unaccounted for: 31 milli
	--- Preprocessor Statistics ---
	Number of preprocessor bound-tightening loop iterations: 48
	Number of eliminated variables: 1
	Number of constraints removed due to variable elimination: 1
	Number of equations removed due to variable elimination: 0
	--- Engine Statistics ---
	Number of main loop iterations: 6824
		6784 iterations were simplex steps. Total time: 977 milli. Average: 0.14 milli.
		0 iterations were constraint-fixing steps. Total time: 0 milli. Average: 0.00 milli
	Number of active piecewise-linear constraints: 78 / 99
		Constraints disabled by valid splits: 2. By SMT-originated splits: 19
	Last reported degradation: 0.0000000000. Max degradation so far: 0.0000000005. Restorations so far: 0
	Number of simplex pivots we attempted to skip because of instability: 0.
	Unstable pivots performed anyway: 0
	--- Tableau Statistics ---
	Total number of pivots performed: 5974
		Real pivots: 5972. Degenerate: 2 (0.03%)
		Degenerate pivots by request (e.g., to fix a PL constraint): 0 (0.00%)
		Average time per pivot: 0.01 milli
	Total number of fake pivots performed: 546
	Total number of rows added: 0. Number of merged columns: 0
	Current tableau dimensions: M = 219, N = 1321
	--- SMT Core Statistics ---
	Total depth is 19. Total visited states: 20. Number of splits: 19. Number of pops: 0
	Max stack depth: 19
	--- Bound Tightening Statistics ---
	Number of tightened bounds: 1991.
		Number of rows examined by row tightener: 5974. Consequent tightenings: 2
		Number of explicit basis matrices examined by row tightener: 4. Consequent tightenings: 62
		Number of bound tightening rounds on the entire constraint matrix: 0. Consequent tightenings: 0
		Number of bound notifications sent to PL constraints: 3409. Tightenings proposed: 0
	--- Basis Factorization statistics ---
	Number of basis refactorizations: 51
	--- Projected Steepest Edge Statistics ---
	Number of iterations: 6520.
	Number of resets to reference space: 6. Avg. iterations per reset: 1086
	--- SBT ---
	Number of tightened bounds: 2288
	--- SoI-based local search ---
	Number of proposed phase pattern update: 112. Number of accepted update: 94 [83.93%]
	Total time (% of local search time) updating SoI phase pattern : 2639 milli [0.32%]
	Total time obtaining current assignment: 9749 milli [1.18%]
	Total time getting SoI phase pattern : 3368 milli [0.29%]
	--- Context dependent statistics ---
	Number of pushes / pops: 19 / 0
		[0.05%] Pre-Push hook: 0 milli
		[0.00%] Push : 0 milli
		[0.00%] Post-Pop hook: 0 milli
		[0.00%] Pop : 0 milli
		[0.05%] Total context-switching time: 0 milli
	--- Proof Certificate ---
	Number of certified leaves: 0
	Number of leaves to delegate: 0
sat
Input assignment:
	x0 = 0.000000
	x1 = 0.000000
	x2 = 0.050000
	x3 = 0.000000
	x4 = 0.050000
	x5 = 0.050000
	x6 = 0.000000
	x7 = 0.000000
	x8 = 0.050000
	x9 = 0.050000
	x10 = 0.050000
	x11 = 0.050000
	x12 = 0.050000
	x13 = 0.000000
	x14 = 0.000000
	x15 = 0.000000
	x16 = 0.000000
	x17 = 0.000000
	x18 = 0.000000
	x19 = 0.000000
	x20 = 0.050000
	x21 = 0.000000
	x22 = 0.000000
	x23 = 0.000000
	x24 = 0.050000
	x25 = 0.000000
	x26 = 0.050000
	x27 = 0.000000
	x28 = 0.050000
	x29 = 0.050000
	x30 = 0.050000
	x31 = 0.000000
	x32 = 0.000000
	x33 = 0.050000
	x34 = 0.000000
	x35 = 0.000000
	x36 = 0.000000
	x37 = 0.000000
	x38 = 0.000000
	x39 = 0.000000
	x40 = 0.012165
	x41 = 0.000000
	x42 = 0.050000
	x43 = 0.000000
	x44 = 0.000000
	x45 = 0.000000
	x46 = 0.000000
	x47 = 0.050000
	x48 = 0.050000
	x49 = 0.050000
	x50 = 0.000000
	x51 = 0.000000
	x52 = 0.050000
	x53 = 0.050000
	x54 = 0.050000
	x55 = 0.050000
	x56 = 0.000000
	x57 = 0.050000
	x58 = 0.000000
	x59 = 0.027542
	x60 = 0.050000
	x61 = 0.050000
	x62 = 0.000000
	x63 = 0.000000
	x64 = 0.000000
	x65 = 0.000000
	x66 = 0.000000
	x67 = 0.050000
	x68 = 0.000000
	x69 = 0.000000
	x70 = 0.050000
	x71 = 0.050000
	x72 = 0.050000
	x73 = 0.050000
	x74 = 0.050000
	x75 = 0.041255
	x76 = 0.050000
	x77 = 0.050000
	x78 = 0.050000
	x79 = 0.000000
	x80 = 0.000000
	x81 = 0.000000
	x82 = 0.050000
	x83 = 0.050000
	x84 = 0.050000
	x85 = 0.050000
	x86 = 0.000000
	x87 = 0.000000
	x88 = 0.050000
	x89 = 0.000000
	x90 = 0.000000
	x91 = 0.000000
	x92 = 0.000000
	x93 = 0.000000
	x94 = 0.000000
	x95 = 0.000000
	x96 = 0.000000
	x97 = 0.000000
	x98 = 0.050000
	x99 = 0.050000
	x100 = 0.000000
	x101 = 0.050000
	x102 = 0.050000
	x103 = 0.050000
	x104 = 0.050000
	x105 = 0.050000
	x106 = 0.000000
	x107 = 0.000000
	x108 = 0.050000
	x109 = 0.000000
	x110 = 0.000000
	x111 = 0.000000
	x112 = 0.050000
	x113 = 0.000000
	x114 = 0.000000
	x115 = 0.000000
	x116 = 0.050000
	x117 = 0.000000
	x118 = 0.000000
	x119 = 0.050000
	x120 = 0.000000
	x121 = 0.000000
	x122 = 0.000000
	x123 = 0.050000
	x124 = 0.000000
	x125 = 0.050000
	x126 = 0.050000
	x127 = 0.000000
	x128 = 0.000000
	x129 = 0.000000
	x130 = 0.050000
	x131 = 0.000000
	x132 = 0.000000
	x133 = 0.050000
	x134 = 0.050000
	x135 = 0.000000
	x136 = 0.050000
	x137 = 0.000000
	x138 = 0.000000
	x139 = 0.000000
	x140 = 0.000000
	x141 = 0.050000
	x142 = 0.000000
	x143 = 0.000000
	x144 = 0.000000
	x145 = 0.000000
	x146 = 0.050000
	x147 = 0.000000
	x148 = 0.050000
	x149 = 0.050000
	x150 = 0.000000
	x151 = 0.000000
	x152 = 0.000000
	x153 = 0.000000
	x154 = 0.000000
	x155 = 0.050000
	x156 = 0.000000
	x157 = 0.000000
	x158 = 0.436275
	x159 = 0.942157
	x160 = 0.950000
	x161 = 0.197059
	x162 = 0.050000
	x163 = 0.000000
	x164 = 0.050000
	x165 = 0.050000
	x166 = 0.000000
	x167 = 0.000000
	x168 = 0.000000
	x169 = 0.000000
	x170 = 0.050000
	x171 = 0.050000
	x172 = 0.050000
	x173 = 0.000000
	x174 = 0.000000
	x175 = 0.050000
	x176 = 0.000000
	x177 = 0.000000
	x178 = 0.000000
	x179 = 0.000000
	x180 = 0.000000
	x181 = 0.000000
	x182 = 0.000000
	x183 = 0.000000
	x184 = 0.000000
	x185 = 0.326471
	x186 = 0.906863
	x187 = 0.934314
	x188 = 1.000000
	x189 = 0.193137
	x190 = 0.050000
	x191 = 0.050000
	x192 = 0.050000
	x193 = 0.050000
	x194 = 0.000000
	x195 = 0.050000
	x196 = 0.050000
	x197 = 0.000000
	x198 = 0.050000
	x199 = 0.000000
	x200 = 0.000000
	x201 = 0.000000
	x202 = 0.000000
	x203 = 0.000000
	x204 = 0.000000
	x205 = 0.000000
	x206 = 0.000000
	x207 = 0.000000
	x208 = 0.000000
	x209 = 0.000000
	x210 = 0.000000
	x211 = 0.000000
	x212 = 0.000000
	x213 = 0.548039
	x214 = 1.000000
	x215 = 0.934314
	x216 = 0.942157
	x217 = 0.193137
	x218 = 0.000000
	x219 = 0.050000
	x220 = 0.000000
	x221 = 0.050000
	x222 = 0.000000
	x223 = 0.000000
	x224 = 0.000000
	x225 = 0.000000
	x226 = 0.000000
	x227 = 0.000000
	x228 = 0.000000
	x229 = 0.050000
	x230 = 0.000000
	x231 = 0.000000
	x232 = 0.000000
	x233 = 0.000000
	x234 = 0.000000
	x235 = 0.000000
	x236 = 0.000000
	x237 = 0.000000
	x238 = 0.000000
	x239 = 0.000000
	x240 = 0.216667
	x241 = 0.875490
	x242 = 0.934314
	x243 = 0.777451
	x244 = 0.171569
	x245 = 0.081373
	x246 = 0.000000
	x247 = 0.050000
	x248 = 0.000000
	x249 = 0.050000
	x250 = 0.000000
	x251 = 0.000000
	x252 = 0.000000
	x253 = 0.000000
	x254 = 0.000000
	x255 = 0.000000
	x256 = 0.000000
	x257 = 0.000000
	x258 = 0.050000
	x259 = 0.000000
	x260 = 0.000000
	x261 = 0.000000
	x262 = 0.000000
	x263 = 0.000000
	x264 = 0.000000
	x265 = 0.000000
	x266 = 0.050000
	x267 = 0.185294
	x268 = 0.944118
	x269 = 0.934314
	x270 = 0.934314
	x271 = 0.418627
	x272 = 0.000000
	x273 = 0.000000
	x274 = 0.000000
	x275 = 0.000000
	x276 = 0.050000
	x277 = 0.000000
	x278 = 0.000000
	x279 = 0.000000
	x280 = 0.000000
	x281 = 0.000000
	x282 = 0.000000
	x283 = 0.050000
	x284 = 0.000000
	x285 = 0.000000
	x286 = 0.000000
	x287 = 0.050000
	x288 = 0.000000
	x289 = 0.050000
	x290 = 0.000000
	x291 = 0.000000
	x292 = 0.050000
	x293 = 0.050000
	x294 = 0.035038
	x295 = 0.657843
	x296 = 0.942157
	x297 = 1.000000
	x298 = 0.691176
	x299 = 0.050000
	x300 = 0.000000
	x301 = 0.000000
	x302 = 0.050000
	x303 = 0.050000
	x304 = 0.050000
	x305 = 0.050000
	x306 = 0.050000
	x307 = 0.000000
	x308 = 0.000000
	x309 = 0.000000
	x310 = 0.000000
	x311 = 0.050000
	x312 = 0.050000
	x313 = 0.000000
	x314 = 0.000000
	x315 = 0.050000
	x316 = 0.028766
	x317 = 0.000000
	x318 = 0.050000
	x319 = 0.050000
	x320 = 0.050000
	x321 = 0.050000
	x322 = 0.128431
	x323 = 1.000000
	x324 = 1.000000
	x325 = 0.971569
	x326 = 0.208824
	x327 = 0.000000
	x328 = 0.000000
	x329 = 0.050000
	x330 = 0.000000
	x331 = 0.050000
	x332 = 0.000000
	x333 = 0.050000
	x334 = 0.050000
	x335 = 0.000000
	x336 = 0.000000
	x337 = 0.000000
	x338 = 0.050000
	x339 = 0.050000
	x340 = 0.000000
	x341 = 0.000000
	x342 = 0.050000
	x343 = 0.050000
	x344 = 0.050000
	x345 = 0.050000
	x346 = 0.050000
	x347 = 0.050000
	x348 = 0.050000
	x349 = 0.175490
	x350 = 0.853922
	x351 = 1.000000
	x352 = 1.000000
	x353 = 0.544118
	x354 = 0.050000
	x355 = 0.000000
	x356 = 0.000000
	x357 = 0.000000
	x358 = 0.000000
	x359 = 0.000000
	x360 = 0.000000
	x361 = 0.000000
	x362 = 0.050000
	x363 = 0.000000
	x364 = 0.000000
	x365 = 0.000000
	x366 = 0.000000
	x367 = 0.050000
	x368 = 0.050000
	x369 = 0.050000
	x370 = 0.050000
	x371 = 0.050000
	x372 = 0.050000
	x373 = 0.050000
	x374 = 0.050000
	x375 = 0.050000
	x376 = 0.050000
	x377 = 0.357843
	x378 = 0.934314
	x379 = 0.942157
	x380 = 0.671569
	x381 = 0.108824
	x382 = 0.050000
	x383 = 0.050000
	x384 = 0.000000
	x385 = 0.050000
	x386 = 0.050000
	x387 = 0.000000
	x388 = 0.000000
	x389 = 0.050000
	x390 = 0.000000
	x391 = 0.000000
	x392 = 0.050000
	x393 = 0.050000
	x394 = 0.000000
	x395 = 0.050000
	x396 = 0.050000
	x397 = 0.050000
	x398 = 0.050000
	x399 = 0.050000
	x400 = 0.050000
	x401 = 0.050000
	x402 = 0.050000
	x403 = 0.050000
	x404 = 0.363725
	x405 = 0.891176
	x406 = 0.934314
	x407 = 0.806863
	x408 = 0.140196
	x409 = 0.050000
	x410 = 0.000000
	x411 = 0.050000
	x412 = 0.050000
	x413 = 0.000000
	x414 = 0.050000
	x415 = 0.050000
	x416 = 0.050000
	x417 = 0.000000
	x418 = 0.000000
	x419 = 0.000000
	x420 = 0.000000
	x421 = 0.000000
	x422 = 0.000000
	x423 = 0.050000
	x424 = 0.050000
	x425 = 0.050000
	x426 = 0.050000
	x427 = 0.000000
	x428 = 0.000000
	x429 = 0.050000
	x430 = 0.050000
	x431 = 0.075490
	x432 = 1.000000
	x433 = 0.942157
	x434 = 0.942157
	x435 = 0.573529
	x436 = 0.000000
	x437 = 0.050000
	x438 = 0.050000
	x439 = 0.050000
	x440 = 0.050000
	x441 = 0.000000
	x442 = 0.050000
	x443 = 0.000000
	x444 = 0.000000
	x445 = 0.000000
	x446 = 0.000000
	x447 = 0.000000
	x448 = 0.000000
	x449 = 0.000000
	x450 = 0.000000
	x451 = 0.000000
	x452 = 0.000000
	x453 = 0.000000
	x454 = 0.000000
	x455 = 0.000000
	x456 = 0.000000
	x457 = 0.000000
	x458 = 0.000000
	x459 = 0.542157
	x460 = 0.934314
	x461 = 0.934314
	x462 = 0.934314
	x463 = 0.202941
	x464 = 0.000000
	x465 = 0.050000
	x466 = 0.050000
	x467 = 0.000000
	x468 = 0.050000
	x469 = 0.050000
	x470 = 0.050000
	x471 = 0.000000
	x472 = 0.000000
	x473 = 0.000000
	x474 = 0.000000
	x475 = 0.000000
	x476 = 0.050000
	x477 = 0.000000
	x478 = 0.000000
	x479 = 0.050000
	x480 = 0.000000
	x481 = 0.050000
	x482 = 0.050000
	x483 = 0.050000
	x484 = 0.000000
	x485 = 0.000000
	x486 = 0.138235
	x487 = 0.816667
	x488 = 0.934314
	x489 = 0.934314
	x490 = 0.624510
	x491 = 0.050000
	x492 = 0.000000
	x493 = 0.000000
	x494 = 0.050000
	x495 = 0.050000
	x496 = 0.050000
	x497 = 0.050000
	x498 = 0.050000
	x499 = 0.050000
	x500 = 0.000000
	x501 = 0.000000
	x502 = 0.000000
	x503 = 0.000000
	x504 = 0.000000
	x505 = 0.050000
	x506 = 0.000000
	x507 = 0.050000
	x508 = 0.050000
	x509 = 0.000000
	x510 = 0.050000
	x511 = 0.000000
	x512 = 0.050000
	x513 = 0.000000
	x514 = 0.867647
	x515 = 0.934314
	x516 = 0.934314
	x517 = 0.818627
	x518 = 0.097059
	x519 = 0.000000
	x520 = 0.000000
	x521 = 0.000000
	x522 = 0.050000
	x523 = 0.000000
	x524 = 0.050000
	x525 = 0.050000
	x526 = 0.000000
	x527 = 0.000000
	x528 = 0.000000
	x529 = 0.000000
	x530 = 0.000000
	x531 = 0.000000
	x532 = 0.050000
	x533 = 0.050000
	x534 = 0.000000
	x535 = 0.050000
	x536 = 0.050000
	x537 = 0.000000
	x538 = 0.050000
	x539 = 0.000000
	x540 = 0.050000
	x541 = 0.000000
	x542 = 1.000000
	x543 = 1.000000
	x544 = 0.934314
	x545 = 0.299020
	x546 = 0.050000
	x547 = 0.000000
	x548 = 0.000000
	x549 = 0.000000
	x550 = 0.000000
	x551 = 0.050000
	x552 = 0.000000
	x553 = 0.050000
	x554 = 0.050000
	x555 = 0.000000
	x556 = 0.000000
	x557 = 0.000000
	x558 = 0.000000
	x559 = 0.000000
	x560 = 0.000000
	x561 = 0.000000
	x562 = 0.050000
	x563 = 0.000000
	x564 = 0.000000
	x565 = 0.000000
	x566 = 0.000000
	x567 = 0.000000
	x568 = 0.000000
	x569 = 0.573529
	x570 = 1.000000
	x571 = 0.942157
	x572 = 1.000000
	x573 = 0.171569
	x574 = 0.050000
	x575 = 0.000000
	x576 = 0.000000
	x577 = 0.050000
	x578 = 0.000000
	x579 = 0.000000
	x580 = 0.000000
	x581 = 0.000000
	x582 = 0.000000
	x583 = 0.000000
	x584 = 0.000000
	x585 = 0.000000
	x586 = 0.000000
	x587 = 0.000000
	x588 = 0.000000
	x589 = 0.000000
	x590 = 0.000000
	x591 = 0.000000
	x592 = 0.000000
	x593 = 0.000000
	x594 = 0.000000
	x595 = 0.000000
	x596 = 0.238235
	x597 = 0.844118
	x598 = 0.942157
	x599 = 0.918627
	x600 = 0.599020
	x601 = 0.081373
	x602 = 0.050000
	x603 = 0.000000
	x604 = 0.000000
	x605 = 0.000000
	x606 = 0.000000
	x607 = 0.000000
	x608 = 0.000000
	x609 = 0.000000
	x610 = 0.000000
	x611 = 0.000000
	x612 = 0.000000
	x613 = 0.000000
	x614 = 0.000000
	x615 = 0.050000
	x616 = 0.000000
	x617 = 0.000000
	x618 = 0.000000
	x619 = 0.000000
	x620 = 0.000000
	x621 = 0.000000
	x622 = 0.000000
	x623 = 0.000000
	x624 = 0.200980
	x625 = 0.934314
	x626 = 0.942157
	x627 = 0.912745
	x628 = 0.000000
	x629 = 0.050000
	x630 = 0.000000
	x631 = 0.050000
	x632 = 0.050000
	x633 = 0.000000
	x634 = 0.000000
	x635 = 0.000000
	x636 = 0.000000
	x637 = 0.000000
	x638 = 0.000000
	x639 = 0.000000
	x640 = 0.000000
	x641 = 0.050000
	x642 = 0.050000
	x643 = 0.050000
	x644 = 0.050000
	x645 = 0.050000
	x646 = 0.000000
	x647 = 0.000000
	x648 = 0.000000
	x649 = 0.050000
	x650 = 0.000000
	x651 = 0.000000
	x652 = 0.300980
	x653 = 0.934314
	x654 = 0.942157
	x655 = 0.812745
	x656 = 0.000000
	x657 = 0.000000
	x658 = 0.000000
	x659 = 0.000000
	x660 = 0.000000
	x661 = 0.000000
	x662 = 0.000000
	x663 = 0.000000
	x664 = 0.000000
	x665 = 0.000000
	x666 = 0.000000
	x667 = 0.000000
	x668 = 0.050000
	x669 = 0.050000
	x670 = 0.050000
	x671 = 0.050000
	x672 = 0.050000
	x673 = 0.000000
	x674 = 0.000000
	x675 = 0.050000
	x676 = 0.000000
	x677 = 0.050000
	x678 = 0.000000
	x679 = 0.000000
	x680 = 0.044118
	x681 = 0.706863
	x682 = 0.942157
	x683 = 0.812745
	x684 = 0.000000
	x685 = 0.000000
	x686 = 0.000000
	x687 = 0.000000
	x688 = 0.000000
	x689 = 0.050000
	x690 = 0.000000
	x691 = 0.000000
	x692 = 0.000000
	x693 = 0.050000
	x694 = 0.000000
	x695 = 0.050000
	x696 = 0.000000
	x697 = 0.000000
	x698 = 0.000000
	x699 = 0.050000
	x700 = 0.000000
	x701 = 0.050000
	x702 = 0.050000
	x703 = 0.050000
	x704 = 0.000000
	x705 = 0.000000
	x706 = 0.000000
	x707 = 0.000000
	x708 = 0.000000
	x709 = 0.050000
	x710 = 0.000000
	x711 = 0.000000
	x712 = 0.000000
	x713 = 0.000000
	x714 = 0.000000
	x715 = 0.000000
	x716 = 0.000000
	x717 = 0.000000
	x718 = 0.000000
	x719 = 0.000000
	x720 = 0.050000
	x721 = 0.050000
	x722 = 0.000000
	x723 = 0.050000
	x724 = 0.050000
	x725 = 0.000000
	x726 = 0.000000
	x727 = 0.000000
	x728 = 0.000000
	x729 = 0.000000
	x730 = 0.050000
	x731 = 0.000000
	x732 = 0.050000
	x733 = 0.050000
	x734 = 0.050000
	x735 = 0.000000
	x736 = 0.000000
	x737 = 0.050000
	x738 = 0.000000
	x739 = 0.000000
	x740 = 0.000000
	x741 = 0.000000
	x742 = 0.000000
	x743 = 0.000000
	x744 = 0.000000
	x745 = 0.050000
	x746 = 0.050000
	x747 = 0.050000
	x748 = 0.049914
	x749 = 0.050000
	x750 = 0.050000
	x751 = 0.000000
	x752 = 0.050000
	x753 = 0.000000
	x754 = 0.000000
	x755 = 0.000000
	x756 = 0.050000
	x757 = 0.050000
	x758 = 0.050000
	x759 = 0.000000
	x760 = 0.000000
	x761 = 0.050000
	x762 = 0.000000
	x763 = 0.000000
	x764 = 0.000000
	x765 = 0.000000
	x766 = 0.000000
	x767 = 0.000000
	x768 = 0.000000
	x769 = 0.000000
	x770 = 0.000000
	x771 = 0.000000
	x772 = 0.000000
	x773 = 0.000000
	x774 = 0.050000
	x775 = 0.000000
	x776 = 0.000000
	x777 = 0.050000
	x778 = 0.050000
	x779 = 0.050000
	x780 = 0.050000
	x781 = 0.000000
	x782 = 0.000000
	x783 = 0.000000

Output:
	y0 = -1.048894
	y1 = -2.389758
	y2 = -0.252501
	y3 = -1.400691
	y4 = -0.865522
	y5 = 0.250462
	y6 = 0.250462
	y7 = -2.147256
	y8 = 0.127807
	y9 = -1.727677

victorg@victors-air Marabou % ./build/Marabou
Error: no network file provided!
Caught a MarabouError error. Code: 15, Errno: 0, Message: .
victorg@victors-air Marabou % ./build/Marabou -h
libc++abi: terminating due to uncaught exception of type boost::wrapexcept<boost::program_options::unknown_option>: unrecognised option '-h'
zsh: abort      ./build/Marabou -h
victorg@victors-air Marabou % python3 from maraboupy import Marabou

/opt/homebrew/Cellar/python@3.11/3.11.3/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/victorg/Marabou/from': [Errno 2] No such file or directory
victorg@victors-air Marabou % python3 test.py                      
/Users/victorg/Marabou/maraboupy/Marabou.py:27: UserWarning: Tensorflow parser is unavailable because tensorflow package is not installed
  warnings.warn("Tensorflow parser is unavailable because tensorflow package is not installed")
/Users/victorg/Marabou/maraboupy/Marabou.py:31: UserWarning: ONNX parser is unavailable because onnx or onnxruntime packages are not installed
  warnings.warn("ONNX parser is unavailable because onnx or onnxruntime packages are not installed")
victorg@victors-air Marabou % pip install tensorflow onnx onnxruntime

Collecting tensorflow
  Downloading tensorflow-2.15.0-cp311-cp311-macosx_12_0_arm64.whl.metadata (3.6 kB)
Collecting onnx
  Downloading onnx-1.15.0-cp311-cp311-macosx_10_12_universal2.whl.metadata (15 kB)
Collecting onnxruntime
  Downloading onnxruntime-1.16.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (4.3 kB)
Collecting tensorflow-macos==2.15.0 (from tensorflow)
  Downloading tensorflow_macos-2.15.0-cp311-cp311-macosx_12_0_arm64.whl.metadata (4.2 kB)
Collecting absl-py>=1.0.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading absl_py-2.1.0-py3-none-any.whl.metadata (2.3 kB)
Collecting astunparse>=1.6.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Collecting flatbuffers>=23.5.26 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading flatbuffers-23.5.26-py2.py3-none-any.whl.metadata (850 bytes)
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading gast-0.5.4-py3-none-any.whl (19 kB)
Collecting google-pasta>=0.1.1 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 1.4 MB/s eta 0:00:00
Collecting h5py>=2.9.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading h5py-3.10.0-cp311-cp311-macosx_11_0_arm64.whl.metadata (2.5 kB)
Collecting libclang>=13.0.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading libclang-16.0.6-py2.py3-none-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting ml-dtypes~=0.2.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading ml_dtypes-0.2.0-cp311-cp311-macosx_10_9_universal2.whl.metadata (20 kB)
Requirement already satisfied: numpy<2.0.0,>=1.23.5 in /opt/homebrew/lib/python3.11/site-packages (from tensorflow-macos==2.15.0->tensorflow) (1.26.2)
Collecting opt-einsum>=2.3.2 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.5/65.5 kB 2.5 MB/s eta 0:00:00
Requirement already satisfied: packaging in /opt/homebrew/lib/python3.11/site-packages (from tensorflow-macos==2.15.0->tensorflow) (23.1)
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading protobuf-4.25.2-cp37-abi3-macosx_10_9_universal2.whl.metadata (541 bytes)
Requirement already satisfied: setuptools in /opt/homebrew/lib/python3.11/site-packages (from tensorflow-macos==2.15.0->tensorflow) (67.6.1)
Requirement already satisfied: six>=1.12.0 in /opt/homebrew/lib/python3.11/site-packages (from tensorflow-macos==2.15.0->tensorflow) (1.16.0)
Collecting termcolor>=1.1.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading termcolor-2.4.0-py3-none-any.whl.metadata (6.1 kB)
Requirement already satisfied: typing-extensions>=3.6.6 in /opt/homebrew/lib/python3.11/site-packages (from tensorflow-macos==2.15.0->tensorflow) (4.6.2)
Collecting wrapt<1.15,>=1.11.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading wrapt-1.14.1-cp311-cp311-macosx_11_0_arm64.whl.metadata (6.7 kB)
Collecting tensorflow-io-gcs-filesystem>=0.23.1 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading tensorflow_io_gcs_filesystem-0.34.0-cp311-cp311-macosx_12_0_arm64.whl.metadata (14 kB)
Collecting grpcio<2.0,>=1.24.3 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading grpcio-1.60.0-cp311-cp311-macosx_10_10_universal2.whl.metadata (4.0 kB)
Collecting tensorboard<2.16,>=2.15 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading tensorboard-2.15.1-py3-none-any.whl.metadata (1.7 kB)
Collecting tensorflow-estimator<2.16,>=2.15.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting keras<2.16,>=2.15.0 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading keras-2.15.0-py3-none-any.whl.metadata (2.4 kB)
Collecting coloredlogs (from onnxruntime)
  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.0/46.0 kB 3.5 MB/s eta 0:00:00
Collecting sympy (from onnxruntime)
  Downloading sympy-1.12-py3-none-any.whl (5.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 3.2 MB/s eta 0:00:00
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime)
  Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.8/86.8 kB 3.3 MB/s eta 0:00:00
Collecting mpmath>=0.19 (from sympy->onnxruntime)
  Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 3.0 MB/s eta 0:00:00
Requirement already satisfied: wheel<1.0,>=0.23.0 in /opt/homebrew/lib/python3.11/site-packages (from astunparse>=1.6.0->tensorflow-macos==2.15.0->tensorflow) (0.40.0)
Collecting google-auth<3,>=1.6.3 (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading google_auth-2.27.0-py2.py3-none-any.whl.metadata (4.7 kB)
Collecting google-auth-oauthlib<2,>=0.5 (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading google_auth_oauthlib-1.2.0-py2.py3-none-any.whl.metadata (2.7 kB)
Collecting markdown>=2.6.8 (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading Markdown-3.5.2-py3-none-any.whl.metadata (7.0 kB)
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 (from tensorflow-macos==2.15.0->tensorflow)
  Downloading protobuf-4.23.4-cp37-abi3-macosx_10_9_universal2.whl.metadata (540 bytes)
Requirement already satisfied: requests<3,>=2.21.0 in /opt/homebrew/lib/python3.11/site-packages (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (2.31.0)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
Requirement already satisfied: werkzeug>=1.0.1 in /opt/homebrew/lib/python3.11/site-packages (from tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (3.0.1)
Collecting cachetools<6.0,>=2.0.0 (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading cachetools-5.3.2-py3-none-any.whl.metadata (5.2 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading pyasn1_modules-0.3.0-py2.py3-none-any.whl (181 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.3/181.3 kB 4.0 MB/s eta 0:00:00
Collecting rsa<5,>=3.1.4 (from google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading rsa-4.9-py3-none-any.whl (34 kB)
Collecting requests-oauthlib>=0.7.0 (from google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: charset-normalizer<4,>=2 in /opt/homebrew/lib/python3.11/site-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (3.1.0)
Requirement already satisfied: idna<4,>=2.5 in /opt/homebrew/lib/python3.11/site-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (3.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/homebrew/lib/python3.11/site-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (2.0.2)
Requirement already satisfied: certifi>=2017.4.17 in /opt/homebrew/lib/python3.11/site-packages (from requests<3,>=2.21.0->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (2023.5.7)
Requirement already satisfied: MarkupSafe>=2.1.1 in /opt/homebrew/lib/python3.11/site-packages (from werkzeug>=1.0.1->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow) (2.1.2)
Collecting pyasn1<0.6.0,>=0.4.6 (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading pyasn1-0.5.1-py2.py3-none-any.whl.metadata (8.6 kB)
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->google-auth-oauthlib<2,>=0.5->tensorboard<2.16,>=2.15->tensorflow-macos==2.15.0->tensorflow)
  Downloading oauthlib-3.2.2-py3-none-any.whl (151 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.7/151.7 kB 3.1 MB/s eta 0:00:00
Downloading tensorflow-2.15.0-cp311-cp311-macosx_12_0_arm64.whl (2.1 kB)
Downloading tensorflow_macos-2.15.0-cp311-cp311-macosx_12_0_arm64.whl (208.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 208.8/208.8 MB 1.1 MB/s eta 0:00:00
Downloading onnx-1.15.0-cp311-cp311-macosx_10_12_universal2.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 1.5 MB/s eta 0:00:00
Downloading onnxruntime-1.16.3-cp311-cp311-macosx_11_0_arm64.whl (6.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 1.2 MB/s eta 0:00:00
Downloading flatbuffers-23.5.26-py2.py3-none-any.whl (26 kB)
Downloading absl_py-2.1.0-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.7/133.7 kB 1.2 MB/s eta 0:00:00
Downloading grpcio-1.60.0-cp311-cp311-macosx_10_10_universal2.whl (9.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 1.4 MB/s eta 0:00:00
Downloading h5py-3.10.0-cp311-cp311-macosx_11_0_arm64.whl (2.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 1.6 MB/s eta 0:00:00
Downloading keras-2.15.0-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 1.7 MB/s eta 0:00:00
Downloading libclang-16.0.6-py2.py3-none-macosx_11_0_arm64.whl (20.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.6/20.6 MB 2.0 MB/s eta 0:00:00
Downloading ml_dtypes-0.2.0-cp311-cp311-macosx_10_9_universal2.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.1 MB/s eta 0:00:00
Downloading tensorboard-2.15.1-py3-none-any.whl (5.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 1.2 MB/s eta 0:00:00
Downloading protobuf-4.23.4-cp37-abi3-macosx_10_9_universal2.whl (400 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 400.3/400.3 kB 1.2 MB/s eta 0:00:00
Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl (441 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 442.0/442.0 kB 1.9 MB/s eta 0:00:00
Downloading tensorflow_io_gcs_filesystem-0.34.0-cp311-cp311-macosx_12_0_arm64.whl (1.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.9/1.9 MB 1.2 MB/s eta 0:00:00
Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)
Downloading wrapt-1.14.1-cp311-cp311-macosx_11_0_arm64.whl (36 kB)
Downloading google_auth-2.27.0-py2.py3-none-any.whl (186 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 186.8/186.8 kB 475.7 kB/s eta 0:00:00
Downloading google_auth_oauthlib-1.2.0-py2.py3-none-any.whl (24 kB)
Downloading Markdown-3.5.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.9/103.9 kB 729.9 kB/s eta 0:00:00
Downloading tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
Downloading cachetools-5.3.2-py3-none-any.whl (9.3 kB)
Downloading pyasn1-0.5.1-py2.py3-none-any.whl (84 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.9/84.9 kB 1.7 MB/s eta 0:00:00
Installing collected packages: mpmath, libclang, flatbuffers, wrapt, termcolor, tensorflow-io-gcs-filesystem, tensorflow-estimator, tensorboard-data-server, sympy, pyasn1, protobuf, opt-einsum, oauthlib, ml-dtypes, markdown, keras, humanfriendly, h5py, grpcio, google-pasta, gast, cachetools, astunparse, absl-py, rsa, requests-oauthlib, pyasn1-modules, onnx, coloredlogs, onnxruntime, google-auth, google-auth-oauthlib, tensorboard, tensorflow-macos, tensorflow
Successfully installed absl-py-2.1.0 astunparse-1.6.3 cachetools-5.3.2 coloredlogs-15.0.1 flatbuffers-23.5.26 gast-0.5.4 google-auth-2.27.0 google-auth-oauthlib-1.2.0 google-pasta-0.2.0 grpcio-1.60.0 h5py-3.10.0 humanfriendly-10.0 keras-2.15.0 libclang-16.0.6 markdown-3.5.2 ml-dtypes-0.2.0 mpmath-1.3.0 oauthlib-3.2.2 onnx-1.15.0 onnxruntime-1.16.3 opt-einsum-3.3.0 protobuf-4.23.4 pyasn1-0.5.1 pyasn1-modules-0.3.0 requests-oauthlib-1.3.1 rsa-4.9 sympy-1.12 tensorboard-2.15.1 tensorboard-data-server-0.7.2 tensorflow-2.15.0 tensorflow-estimator-2.15.0 tensorflow-io-gcs-filesystem-0.34.0 tensorflow-macos-2.15.0 termcolor-2.4.0 wrapt-1.14.1
victorg@victors-air Marabou %
