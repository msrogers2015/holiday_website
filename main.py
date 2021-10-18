from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)
holidays = {
    "New_Year" : ([1,1],'','black', 'white'),
    'Valentines' : ([2,14],'','#b3271d','white'),
    'April_Fools' : ([4,1],'The Killing Joke" by 1upLego is licensed with CC BY-NC-SA 2.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/2.0/ ','black','white'),
    'Cinco_De_Mayo' : ([5,5],'','#251232','white'),
    'Juneteenth' : ([6,19],'','black','white'),
    'Independence_Day' : ([7,1],'','#618ee9','black'),
    'Halloween' : ([10,31],' "Halloween Pumpkins" by lobo235 is licensed with CC BY 2.0. To view a copy of this license, visit https://creativecommons.org/licenses/by/2.0/ ','black','white'),
    'Veterns' : ([11,11],'','#',''),
    'Christmas' : ([12,25],'','#',''),
}




@app.route('/')
def index():
    return render_template('index.html', holidays=holidays)

@app.route('/holidays/<holiday>', methods=['GET'])
def timer(holiday):
    bgcolor=holidays[holiday][2]
    textcolor=holidays[holiday][3]
    credits=holidays[holiday][1]
        # If today month and day is the same as the saved value
    if holiday in holidays:
        # Creating date objects
        current = dt.datetime.utcnow()
        date = holidays[holiday][0]
        d = dt.datetime(current.year, date[0], date[1])
        # If date matches today
        if d.month and d.date == current.month and current.day:
            reply = f'Yes! Today is {holiday.capitalize()}.'
        else:
            reply = f'Sorry, it isn\'t {holiday.capitalize()}.'

    if holiday in holidays:
        # Creating date objects
        current = dt.datetime.utcnow()
        date = holidays[holiday][0]
        d = dt.datetime(current.year, date[0], date[1])
        year_offset = 365
        t_delta = d - current
        # If date matches today
        if d.day and d.month == current.day and current.month:
            time_left = 'Today is {holiday.capitalize()}. how are you going to celebrate?'
        # If date has passed
        elif t_delta.total_seconds() < 0:
            h_passed = (d + dt.timedelta(days=year_offset)) - current
            result = str(h_passed)
            info, leftover = result.split('.')
            time_left = f'{holiday.capitalize()} is in {info}.'
        # If date is in the future
        else:
            result = str(t_delta)
            info, leftover = result.split('.')

            time_left = f'{holiday.capitalize()} is in {info}'


    if holiday not in holidays:
        reply = f'Sorry, this holiday hasn\'t been added to the last. Try making a suggestion by opening an issue on the github repo {github}'

    return render_template("holiday.html", reply=reply, holiday=holiday, time_left=time_left, holidays=holidays, bg="/static/img/"+holiday+'.jpg', bgcolor=bgcolor, textcolor=textcolor, credits=credits)


if __name__ == '__main__':
    app.run(debug=True)