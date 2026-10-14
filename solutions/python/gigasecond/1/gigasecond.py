from datetime import timedelta, datetime
def add(moment:datetime):
    return moment + timedelta(0, 1_000_000_000)