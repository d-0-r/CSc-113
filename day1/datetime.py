from datetime import datetime

tzinfo = datetime.now()

print('Current date and time:\n')
print(tzinfo.strftime("%Y-%m-%d %H:%M:%S"))
