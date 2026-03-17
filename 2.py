from datetime import datetime, timedelta
s1 = input()


dt1 = datetime.strptime(s1, "%Y-%m-%d")
days=int(input())

date=dt1+timedelta(days=days)
print(date.strftime("%Y-%m-%d"))
