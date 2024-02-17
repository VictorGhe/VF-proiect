Error for installation on ARM:

victorg@Victors-MacBook-Air ~ % git clone https://github.com/dynaroars/neuralsat.git
Cloning into 'neuralsat'...
remote: Enumerating objects: 10062, done.
remote: Counting objects: 100% (1392/1392), done.
remote: Compressing objects: 100% (464/464), done.
remote: Total 10062 (delta 942), reused 1368 (delta 921), pack-reused 8670
Receiving objects: 100% (10062/10062), 201.84 MiB | 1.54 MiB/s, done.
Resolving deltas: 100% (6223/6223), done.
victorg@Victors-MacBook-Air ~ % conda deactivate; conda env remove --name neuralsat

victorg@Victors-MacBook-Air ~ % cd neuralsat 
victorg@Victors-MacBook-Air neuralsat % conda env create -f env.yaml

Channels:
 - gurobi
 - pytorch
 - nvidia
 - defaults
Platform: osx-arm64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - _libgcc_mutex==0.1=main
  - _openmp_mutex==5.1=1_gnu
  - blas==1.0=mkl
  - brotli-python==1.0.9=py310h6a678d5_7
  - bzip2==1.0.8=h7b6447c_0
  - ca-certificates==2023.08.22=h06a4308_0
  - certifi==2023.11.17=py310h06a4308_0
  - cffi==1.16.0=py310h5eee18b_0
  - cryptography==41.0.7=py310hdda0065_0
  - cuda-cudart==11.8.89=0
  - cuda-cupti==11.8.87=0
  - cuda-libraries==11.8.0=0
  - cuda-nvrtc==11.8.89=0
  - cuda-nvtx==11.8.86=0
  - cuda-runtime==11.8.0=0
  - ffmpeg==4.3=hf484d3e_0
  - filelock==3.13.1=py310h06a4308_0
  - freetype==2.12.1=h4a9f257_0
  - giflib==5.2.1=h5eee18b_3
  - gmp==6.2.1=h295c915_3
  - gmpy2==2.1.2=py310heeb90bb_0
  - gnutls==3.6.15=he1e5248_0
  - idna==3.4=py310h06a4308_0
  - intel-openmp==2023.1.0=hdb19cb5_46306
  - jinja2==3.1.2=py310h06a4308_0
  - jpeg==9e=h5eee18b_1
  - lame==3.100=h7b6447c_0
  - lcms2==2.12=h3be6417_0
  - ld_impl_linux-64==2.38=h1181459_1
  - lerc==3.0=h295c915_0
  - libcublas==11.11.3.6=0
  - libcufft==10.9.0.58=0
  - libcufile==1.8.1.2=0
  - libcurand==10.3.4.101=0
  - libcusolver==11.4.1.48=0
  - libcusparse==11.7.5.86=0
  - libdeflate==1.17=h5eee18b_1
  - libffi==3.4.4=h6a678d5_0
  - libgcc-ng==11.2.0=h1234567_1
  - libgomp==11.2.0=h1234567_1
  - libiconv==1.16=h7f8727e_2
  - libidn2==2.3.4=h5eee18b_0
  - libjpeg-turbo==2.0.0=h9bf148f_0
  - libnpp==11.8.0.86=0
  - libnvjpeg==11.9.0.86=0
  - libpng==1.6.39=h5eee18b_0
  - libstdcxx-ng==11.2.0=h1234567_1
  - libtasn1==4.19.0=h5eee18b_0
  - libtiff==4.5.1=h6a678d5_0
  - libunistring==0.9.10=h27cfd23_0
  - libuuid==1.41.5=h5eee18b_0
  - libwebp==1.3.2=h11a3e52_0
  - libwebp-base==1.3.2=h5eee18b_0
  - llvm-openmp==14.0.6=h9e868ea_0
  - lz4-c==1.9.4=h6a678d5_0
  - markupsafe==2.1.1=py310h7f8727e_0
  - mkl==2023.1.0=h213fc3f_46344
  - mkl-service==2.4.0=py310h5eee18b_1
  - mkl_fft==1.3.8=py310h5eee18b_0
  - mkl_random==1.2.4=py310hdb19cb5_0
  - mpc==1.1.0=h10f8cd9_1
  - mpfr==4.0.2=hb69a4c5_1
  - mpmath==1.3.0=py310h06a4308_0
  - ncurses==6.4=h6a678d5_0
  - nettle==3.7.3=hbbd107a_1
  - networkx==3.1=py310h06a4308_0
  - numpy==1.26.2=py310h5f9d8c6_0
  - numpy-base==1.26.2=py310hb5e798b_0
  - openh264==2.1.1=h4ff587b_0
  - openjpeg==2.4.0=h3ad879b_0
  - openssl==3.0.12=h7f8727e_0
  - pillow==10.0.1=py310ha6cbd5a_0
  - pip==23.3.1=py310h06a4308_0
  - pyopenssl==23.2.0=py310h06a4308_0
  - pysocks==1.7.1=py310h06a4308_0
  - python==3.10.13=h955ad1f_0
  - pytorch==2.1.2=py3.10_cuda11.8_cudnn8.7.0_0
  - pytorch-cuda==11.8=h7e8668a_5
  - pyyaml==6.0.1=py310h5eee18b_0
  - readline==8.2=h5eee18b_0
  - requests==2.31.0=py310h06a4308_0
  - setuptools==68.2.2=py310h06a4308_0
  - sqlite==3.41.2=h5eee18b_0
  - sympy==1.12=py310h06a4308_0
  - tbb==2021.8.0=hdb19cb5_0
  - tk==8.6.12=h1ccaba5_0
  - torchaudio==2.1.2=py310_cu118
  - torchtriton==2.1.0=py310
  - torchvision==0.16.2=py310_cu118
  - typing_extensions==4.7.1=py310h06a4308_0
  - urllib3==1.26.18=py310h06a4308_0
  - wheel==0.41.2=py310h06a4308_0
  - xz==5.4.5=h5eee18b_0
  - yaml==0.2.5=h7b6447c_0
  - zlib==1.2.13=h5eee18b_0
  - zstd==1.5.5=hc292b87_0

Current channels:

  - https://conda.anaconda.org/gurobi/osx-arm64
  - https://conda.anaconda.org/pytorch/osx-arm64
  - https://conda.anaconda.org/nvidia/osx-arm64
  - https://repo.anaconda.com/pkgs/main/osx-arm64
  - https://repo.anaconda.com/pkgs/r/osx-arm64

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


victorg@Victors-MacBook-Air neuralsat % 