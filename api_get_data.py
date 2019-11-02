import requests

# Build Arguments
def get_curr_usage():
    curr_usage = requests.get("https://sfuec-2019.herokuapp.com/usage/current").json()
    return curr_usage

def get_weekly_usage():
    curr_weekly_usage = requests.get("https://sfuec-2019.herokuapp.com/usage/week").json()
    return curr_weekly_usage

def get_daily_usage():
    curr_daily_usage = requests.get("https://sfuec-2019.herokuapp.com/usage/day").json()
    return curr_daily_usage

def get_monthly_usage():
    curr_monthly_usage = requests.get("https://sfuec-2019.herokuapp.com/usage/month").json()
    return curr_monthly_usage
