import datetime

while True:
    now = datetime.datetime.now()
    new_time = str(now + datetime.timedelta(minutes = 43))
    now = str(now)
    now = now[11:17]
    new_time = new_time[11:17]
    mob = input()
    with open("timezen.txt", "a") as a:
        a.write("\n")
        a.write(now)
        a.write(" -> ")
        a.write(new_time)
        a.write("Mob: ")
        a.write(mob)
    print("-----------Do an Please------------")
    print(now, "->", new_time, "도안몹, 채널: ", mob)
    print("-----------Do an Please------------")
