import simpy
import numpy as np
import random
import pandas as pd

#create working function
def working(env, hours, employee_id, day, data):
    start = env.now
    yield env.timeout(round(np.random.normal(hours)*4)/4)
    worked_hours = env.now - start
    data.append((day, employee_id, "Working Hours", worked_hours))

#create holiday function
def holiday(env, employee_id, day, hours, data):
    start = env.now
    yield env.timeout(hours)
    vacations = env.now - start
    data.append((day, employee_id, "Vacation Hours", vacations))


#create main simulation function
def work(nemployees = 3, 
         daily_hours = 8.4,
         ndays = 5*52,
         vacation_days = 25):
    
    #store outputs in data
    data= []
    #create environment
    env = simpy.Environment()
    #run simulation for each employeee
    for employee_id in range(nemployees+1):
        free_vacations = vacation_days * daily_hours
        #run for each day the processes
        for day in range(ndays):
                #employee needs holidays in 5 % of his days
                if random.random() < 0.05 and free_vacations > 0:
                    vacation_hours = round(random.uniform(0,free_vacations)*4)/4
                    free_vacations = free_vacations - vacation_hours
                    env.process(holiday(env, employee_id, day,  vacation_hours, data))
                else:
                    env.process(working(env, daily_hours, employee_id, day, data))
    #run simulation environment
    env.run()
    #return pandas dataframe
    return pd.DataFrame(data, columns = ['Day', 'Employee', 'Kind', 'Hours'])