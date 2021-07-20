# 7. You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops
# on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first
# mile at 7mph; then run the next two at15mph; before jogging
# the last at 7mph again. Will this be quicker or slower than the bus?


universityDisance= 4

bus_mph_into_mpm= 25/60  #for bus

#human
human_jog_mph_into_mpm=7/60 #while jogging
human_run_mph_into_mpm=15/60 #while running
by_jogging=2/human_jog_mph_into_mpm
by_running=2/human_run_mph_into_mpm

No_stops=10
time_Spends_at_Stop=2

total_Time_Spends_at_Stops=No_stops*time_Spends_at_Stop

time_takes_bus=(universityDisance/bus_mph_into_mpm)+total_Time_Spends_at_Stops
# print('time taken by bus for the university is ',time_takes_bus)

time_takes_human=by_jogging+by_running


def fastest():
    if time_takes_bus>time_takes_human:
        print('time taken by bus is ',time_takes_bus)
        print('time taken by human is',time_takes_human)
        print('Human is faster then bus.')
    else:
        print('time taken by bus is ', time_takes_bus)
        print('time taken by human is', time_takes_human)
        print('Bus is slower then human')

fastest()