# VF-proiect

Benchmark Collins Rul CNN: https://github.com/ChristopherBrix/vnncomp2023_benchmarks/tree/main/benchmarks/collins_rul_cnn

Tools: 
1. Alpha-beta-crown: https://github.com/Verified-Intelligence/alpha-beta-CROWN

2. NeuralSAT https://github.com/dynaroars/neuralsat

Saptamana 9

Am examinat materialele prezentate în curs pentru a determina ce set de date și instrumente vom folosi. În urma acestei revizuiri, am selectat instrumentele alpha-beta-crown și pyrat, iar pentru evaluarea comparativă am optat pentru ViT (Vision Transformer).

În etapele următoare:

-Am consultat documentația oficială a alpha-beta crown pentru a înțelege cum se instalează acest instrument;
-Am evaluat benchmark-ul care va fi utilizat cu alpha-beta crown, pentru a compara rezultatele cu cele obținute în cadrul unei competiții recent încheiate.

Saptamana 10

Instalarea tool-ului mentionat mai sus pe Linux si pe Mac OS.
Rezolvarea erorilor intampinate.

Saptamana 11

Testarea tool-ului alpha-beta-crown cu succes pe sistemul de operare Linux, folosind configuratia cifar_resnet_2b.yaml

Saptamana 12

Rularea tool-ului asupra benchmark-ului si obtinerea rezultatelor
Datorita lipsei unei placi grafice CUDA pe masina virtuala, am fost nevoiti sa rulam pe baza CPU host-ului.
Realizarea draft-ului.

Saptamana 13 & 14

Esuarea instalarii tool-urilor Marabou, PyRaT datorita arhitecturii hardware-ului (M1 silicon).

Saptamana 5-11 Febr

5 Febr: Am schimbat scopul proiectului, collins_rul_cnn + alpha beta CROWN & NeuralSAT

6 Febr: Am esuat instalarea NeuralSAT pe arhitectura ARM, dar am reusit intalarea pe un laptop alternativ. S-a rulat primul onnx si vnnlib de test, rezultat cu succes.

7 Febr: Am dezvoltat un script Python pentru a rula verificarile in aceeasi ordine ca si cele de la VNNCOMP2023. (results.csv)
        Am rulat cu succes tool-ul NeuralSAT pe benchmark-ul collins_rul_cnn.
