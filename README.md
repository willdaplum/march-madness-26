# march-madness-26

### Getting Started

#### Download Starter Code
```bash
git clone https://github.com/willdaplum/march-madness-26.git
cd march-madness-26
```

#### Training Data
- Download csv files from [here](https://www.kaggle.com/competitions/march-machine-learning-mania-2026/data)
- Copy files into march-madness-26/data
- Data can be used from elsewhere as well, but the script relies on MTeams.csv and MNCAATourneySeeds.csv from this source to build the bracket.

#### Setting Up the Python Project
```bash
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
#### Run a tournament simulation
```bash
python3 march-madness.py
```
This writes (or overwrites) the file *simulation_results.json*, containing the program's tournament predictions in machine readable format.

#### Submitting Predictions
Once you're satisfied with the bracket your program generates, it can be submitted by running
```bash
python3 submit-predictions.py
```
***Important: Only do this when ready as it will be a bit annoying to delete***

### Done!
View the bracket competition [here](https://www.wcooley.net/march-madness) - with live updates!!
