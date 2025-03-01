# Project Title: Urban Dynamics

## Notebook description

- austria_NNSI.ipynb: For reproducing legacy spatial interaction model in http://openjournals.wu.ac.at/region/paper_175_revised/175.html

- SI.ipynb: Data collection and exploration for this project.

- Taxi_NNSI.ipynb: Prepare NYC taxi data for NNSI and visualization

- MainPlayground: Stage for running Spatial dependence SI model. (OLS/GLM/MLP)

- LSTM_NNSI.ipynb: Stage for running Temporal dependence SI model. (OLS/MLP/RNN/LSTM)


## Update 12/16
- [x] Clean notebooks
- [x] Visualization from streamlit


## Update 12/10

### Task today:


- [x] OLS/NN/RNN/LSTM SI model for flow time series
- [x] Interpretation template for PDP/SHAP
- [ ] Interpretation template for counterfactual explanation
- [ ] tuning and compare RNN/LSTM SI model
## Update 12/09

### Task today:

- [x] Real world-- Taxi data on NN run init result
- [ ] Real world-- Taxi data on NN run parameters comparison
- [ ] LSTM SI model
- [ ] Interpretation template of NN and LSTM model


## Update 12/04

### Task today:
- [x] Markdown description
- [x] Function definition position
- [x] Clear legacy code in notebook
- [X] Clear ERROR
- [x] Use test data in comparison
- [x] Upload data file
- [x] Make simulated SI data
- [ ] Real world data run

## Update 12/03
### Finished:
Add mainPlayground notebook with all data/computation modules wrapped in function

### Ongoing:
study real SI data to get valid output in NN model.

## Update 12/01
### Finished:
Simple linear regression can be realized in Step0 neural network.

### Ongoing:
introduce NNSI

## Update 10/29
### Finished:

NYC Taxi/Bike data processing (SI.ipynb)

Gravity spatial interaction prototyping (austria.ipynb)

BP neural network prototyping (austria.ipynb)

### Ongoing:
Newly added Taxi_nn.ipynb:

**Part 1**

Processing and generate Data of NYC Taxi

Almost done. Is ready for use in part 2 and part 3

**Part 2**

Using PyTorch to implement LSTM model

Too advanced. Put away for now

**Part 3**
Manual simple NN

**Tuning now** Hand writing numpy based Neural Net with 3 input and 1 output features.

### Todo:
Data formating from Taxi dataframe to LSTM input features

(partial done)LSTM neural network prototyping (LSTM.ipynb)

Calibration of models

Explanation of models
