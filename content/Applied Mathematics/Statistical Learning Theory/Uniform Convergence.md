---
draft: "true"
---

**Prerequisites:** [[APAC Learnability]], [[Bias-Complexity Tradeoff]]

## Introduction

모델의 APAC Learnability는 approximation error와 estimation error에 의해 정해진다. 이때 estimation error는 우리가 실제 분포 $D$ 대신 sampling $S$를 사용하기 때문에 발생하는 에러를 포함한다. 따라서 만약 empirical risk와 true risk간의 차이가 bounded 되어 있다면 학습이 가능하리라고 추론해 볼 수 있다.