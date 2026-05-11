total_minutes = 0

for i in '1h 45m,365s,25m,30m 120s,2h 60s'.replace(',', ' ').split(' '):
    if i[-1] == 'h':
        total_minutes += int(i[:-1]) * 60
    elif i[-1] == 'm':
        total_minutes += int(i[:-1])
    elif i[-1] == 's':
        total_minutes += int(i[:-1]) // 60

print(total_minutes)