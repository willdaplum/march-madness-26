# march-madness-26
Predict the 2026 March Madness tournament using code! Go Blue and Go Cats :)

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

#### Write Your Prediction Logic
In march-madness.py, the function predict_matchup determines which teams will win and lose. By default, it picks the higher seed as a demo, but this can be made much better using the data from kaggle.
```python
def predict_matchup(team1: Team, team2: Team):
    """Returns True if team 1 wins, false if team 2 wins"""
    ### ADD GAME PREDICTION LOGIC BELOW

    # e.g.: always predict the higher (better) seeded team to win
    if team1.seed <= team2.seed:
        return True
    return False

    ### END GAME PREDICTION LOGIC
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
***Important:*** Change the *name* field of the *payload* object in submit-predictions.py to your bracket name

### Done!
View the bracket competition [here](https://www.wcooley.net/march-madness) - with live updates!!
