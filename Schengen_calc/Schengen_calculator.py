import time

residence_limit = 90  # 45, 60
schengen_constraint = 180

def visit_duration(*arguments):
    return(max(arguments) - min(arguments) + 1)

def check_input_data(visits_list, new_visit):
    days_of_visits = set()
    new_visit_set = set()
    for each in visits_list: days_of_visits.update(range(each[0], each[1] + 1))
    new_visit_set.update(range(new_visit[0], new_visit[1] + 1))
    if new_visit_set.intersection(days_of_visits):
        raise Exception('Вы уже были в это время в Европе')
    elif max(days_of_visits) >= min(new_visit_set):
        raise Exception('Ой-ей, что-то пошло не так...Вы хотите въехать в Шенген раньше последней даты выезда')

def check_date_consistency(date_start, date_end):
    if date_start >= date_end:
        print("Дата отъезда должна быть позднее даты начала поездки. Попробуйте еще раз", end='\n \n')
        add_visit()

def visits_left(visits_list, new_visit_enter, residence_limit, schengen_constraint):
    period_start = (new_visit_enter) - (schengen_constraint)
    days_left = residence_limit
    for each_visit in visits_list:
        if each_visit[0] < period_start <= each_visit[1]:
            days_left -= visit_duration(each_visit[1], period_start)
            pass
        elif period_start <= each_visit[0]: days_left -= visit_duration(each_visit[1], each_visit[0])
    return (days_left)

def visit_add(visits_left, start, end):
    if visits_left >= (end - start + 1):
        visits.append([start, end])
        print('Ваша поездка добавлена')
    else:
        print('У вас не хватает дней для данной поездки, к этой дате въезда остаток составит всего лишь {} д'.format(visits_left))

def visit_left_print(visits_left):
    if visits_left > 0: print('Вы можете провести в путешествии {}д'.format(visits_left))
    else: print('К сожалению, Вы израсходовали все дни. Остаток: {}'.format(visits_left))

def preliminary_check():
    x = visits_left(visits, visits[-1][0], residence_limit, schengen_constraint)
    if x < 0:
        print('Что-то не в порядке с данными о поездках - вы пробыли в Европе больше дней, чем положено. Пожалуйста, проверьте информацию', visits, 'Дней израсходовано: {}'.format(residence_limit - x), sep='\n')
        delete_visit()
        #!!!DELETE
    time.sleep(0.75)

def welcoming_msg():
    print('v - добавить визит, p - расчитать допустимую продолжительность следующей поездки,\n r - удалить визит, e - выйти')
    time.sleep(0.25)
    print('Какое действие Вы хотите совершить?')

def delete_visit():
    print('Список поездок: {0}'.format(visits))
    print('Какую поездку Вы хотите удалить?')
    start = int(input('Дата начала поездки?'))
    end = int(input('Дата окончания поездки?'))
    time.sleep(0.75)
    counter=0
    for each in visits:
        if (start == each[0]) & (end == each[1]):
            visits.remove(each)
            counter += 1
            print('Поездка {0} была удалена. \n Список поездок: {1}'.format(each, visits))
    if counter == 0: print('Мы не смогли найти Вашу поездку...')

def add_visit():
    start = int(input ('Дата начала поездки?'))
    end = int(input ('Дата окончания поездки?'))
    check_date_consistency(start, end)
    time.sleep(0.75)
    check_input_data (visits, [start, end])
    days_for_new_travel = visits_left(visits, start, residence_limit, schengen_constraint)
    visit_add(days_for_new_travel, start,end)
    print('Список поездок: {0}'.format(visits))

def exit_msg():
    print('До свидания!')
    working = False

def calculate_next_visit():
    start = int(input('Дата начала поездки?'))
    check_input_data(visits, [start,start])
    visit_left_print(
        visits_left(visits, start, residence_limit, schengen_constraint))

#number of days used till 174 included - (10+15+44+5)
visits=[[1, 10], [25, 39], [87, 130], [150, 155]]
#[87, 130]

working = True
while working:
    preliminary_check()
    welcoming_msg()
    user_input = input()
    if user_input == 'v': add_visit()
    elif user_input == 'r': delete_visit()
    elif user_input == 'p': calculate_next_visit()
    elif user_input == 'e':
        exit_msg()
        working = False
