hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
print((mins + dura) % 60, hour+(mins + dura) // 60)
