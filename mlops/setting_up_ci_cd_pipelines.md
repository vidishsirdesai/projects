# Introduction
The following flowchart shows the lifecycle of an ML project,

```mermaid
flowchart LR
    A(Requirement Gathering) --> B(Data Collection)
    B --> C(EDA)
    C --> D(Model Building)
    D --> E(Testing)
    E --> F(Containerization)
    F --> G(Deploy)
```

In the lifecycle above the code changes keep happening quite frequently at different steps, and it is imperative to make sure that after code commit, the code does not break. Hence, developers carry out unit tests to ensure that their addition to the code base has not had a disastrous effect.

This task of developing, testing, and deploying is a tedious task if done manually. This is where automated pipelines come into the picture. These pipelines are divided into 2 parts,
1. Continuous Integration (CI)
2. Continuous Delivery (CD)

The following figure illustrates the CI/ CD pipeline,

```mermaid
flowchart LR
    subgraph CI
        A(PLAN) --> B(CODE)
        B --> C(BUILD)
        C --> D(TEST)
    end
    subgraph CD
        E(RELEASE) --> F(DEPLOY)
        F --> G(OPERATE)
        G --> H(MONITOR)
    end
    D --> E
    H --> A
```


#