# GBMAD
Sihan Wang, Shitong Cheng, **Zhong Yuan***, Hongmei Chen, and Dezhong Peng, [Granular-Ball Computing-Based Markov Random Walk for Anomaly Detection](Paper/2024-GBMAD.pdf). (Code)

## Abstract
Anomaly detection is a key task in data mining, which has been successfully employed in many practical scenarios. However, most existing methods usually analyze the anomalous characteristics of samples at a single and finest granularity, which leads to high computational cost and low efficiency. As one of the important mathematical models in the theory of granular computing, granular-ball computing can portray the distributional characteristics of data from a multi-granularity perspective. For this reason, this paper proposes an unsupervised anomaly detection method based on granular-ball computing. Firstly, the samples are covered by generating adaptive granular-balls and the local distribution properties of the samples are inscribed. Secondly, the granular-balls are used to fit the samples for constructing a state transfer matrix in the Markov random walk. Then, the steady-state distribution is generated using iterative computation and is normalized as the degree of anomaly for each granular-ball. Finally, the anomaly score for each sample is computed by relating the anomaly degree of each granular-ball to the samples it covers. Comparative experiments show that the proposed anomaly detection method performs well on multiple datasets, demonstrating its feasibility and superiority in practical applications. The code is publicly available online at [https://github.com/optimusprimeyy/GBMAD](https://github.com/optimusprimeyy/GBMAD).

## Usage
You can run GBMAD.py:
```
if __name__ == "__main__":
      main()
```
## Contact
If you have any question, please contact [wangsihan0713@foxmail.com](wangsihan0713@foxmail.com).

