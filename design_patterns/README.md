# The Strategy Design Pattern

First problem in building delibrate ML pipelines is understanding what data structures to use for data ingestion, analysis, and validation. These processes require heavy filtering, grouping, and manipulation of the data and writing error prone-code can be consequential. 

The second step is feeding the data into algorithms that offer insight. This stage also requires modular functional programs, that have strategy built into design. Programs can be written for one particular type of algorithm, but lacks the choice aspect of picking which model to use for a particular use case.

This pattern has an interface like the factory pattern, and calls the algorithm as a class wrapper to get the output instead of calling the algorithm directly. Any input that is passed to the member function can be added to the constructor, and general functionality can be abstracted to be used across multiple model frameworks.

This way data scientists and ML practicioners can agree up a set of methods and attributes all models in the pipeline use, and the inner workings of each model have been abstracted up to prevent redundency and misuse.

The concept is simple: if all models have a load task, abstract the load method up to a base class that functions as a blueprint for the different say NLP class types. They all will have their own lemmatizer, parsing protocol, loading method, training/testing dictionaries, hyperparameter configurations, and metrics for testing. To further add on to testing, metrics for testing process can also be abstracted up to allow for fluidity acorss models, and the same graphs can be used for different models to compare their effectiveness and need for fine-tuning/deployment.

The design fine-tuning is up to the programmer. Different stages of the process can be broken down into sub-protocols and developed in isolated toolboxes and configure in the end. The loading phase can be one process, but its previous phase could have different class types from which one was chosen because the file being processed is csv and not json for example.


Design Pattern Code Adopted from Laszlo Sragner's Article in Deliberate ML