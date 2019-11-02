import PySimpleGUI as sg
from api_get_data import get_curr_usage
from api_get_data import get_weekly_usage
from api_get_data import get_daily_usage
from api_get_data import get_monthly_usage
from test_ground import usage_breakdown
from test_ground import get_time
from test_ground import get_color
import plotly.graph_objects as go
# All the stuff inside your window.

curr_usage = get_curr_usage()
daily_usage = get_daily_usage()
weekly_usage = get_weekly_usage()
monthly_usage = get_monthly_usage()

# Parameters for current
first_name = curr_usage["user"]["first_name"]
last_name = curr_usage["user"]["last_name"]
curr_usage_kW = '%.3f'%(curr_usage["usage_kW"])
curr_level = curr_usage["level"]
cents_per_hr = curr_usage["cents_per_hr"]

# Parameters for daily
daily_usage_kWh = '%.3f'%(daily_usage["usage_kWh"])
daily_level = daily_usage["level"]

# Parameters for weekly
weekly_usage_kWh = '%.3f'%(weekly_usage["usage_kWh"])
weekly_level = weekly_usage["level"]

# Parameters for monthly
monthly_usage_kWh = '%.3f'%(monthly_usage["usage_kWh"])
monthly_level = monthly_usage["level"]

greetings = get_time()
curr_status_color = get_color(curr_level)
estimated_cost = '%.1f'%(float(cents_per_hr) * float(weekly_usage_kWh) * 4 / 100)

name_week, percent_week = usage_breakdown(weekly_usage)
name_day, percent_day = usage_breakdown(daily_usage)
name_month, percent_month = usage_breakdown(monthly_usage)

main_menu = [
            [sg.Text("Dashboard",font=("Helvetica", 20))],
            [sg.Text('{} {}!'.format(greetings, first_name))],
            [sg.Canvas(size=(20, 20), background_color=curr_status_color, key= 'canvas'),
                sg.Text('Current Usage Level: {}'.format(curr_level))],
            [sg.Text('Usage: {}kW'.format(curr_usage_kW)),
                sg.Text('Estimated Monthly Bill: ${}'.format(estimated_cost))],
            [sg.Button('Daily Usage'), sg.Button('Weekly Usage'), sg.Button('Monthly Usage'), sg.Button('Tips')],
            [sg.Button('Cancel')] ]



# Create the Window
win1 = sg.Window('Dashboard', main_menu)
win2_active = False
win3_active = False
win4_active = False
win5_active = False

# Main loop for the program
while True:
    ev1, vals1 = win1.read()

    if ev1 == 'Daily Usage' and not win2_active:

        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Daily Usage',font=("Helvetica", 15))],
                   [sg.Text('Current Usage Level: {}'.format(daily_level))],
                   [sg.Text('Usage: {}kW'.format(daily_usage_kWh))],
                   [sg.Button("Show Usage Breakdowns")],# note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Daily Usage', layout2)
        while True:
            ev2, vals2 = win2.Read()
            if ev2 == 'Show Usage Breakdowns':
                fig_day = go.Figure(data=[go.Pie(labels=name_day, values=percent_day)])
                fig_day.show()

            elif ev2 == 'Exit':
                win2.Close()
                win2_active = False
                win1.UnHide()
                break

    elif ev1 == 'Weekly Usage' and not win3_active:

        win3_active = True
        win1.Hide()
        layout3 = [[sg.Text('Weekly Usage',font=("Helvetica", 15))],
                   [sg.Text('Current Usage Level: {}'.format(weekly_level))],
                   [sg.Text('Usage: {}kW'.format(weekly_usage_kWh))],
                   [sg.Button("Show Usage Breakdowns")],# note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win3 = sg.Window('Weekly Usage', layout3)
        while True:
            ev3, vals3 = win3.Read()
            if ev3 == 'Show Usage Breakdowns':
                fig_week = go.Figure(data=[go.Pie(labels=name_week, values=percent_week)])
                fig_week.show()

            elif ev3 == 'Exit':
                win3.Close()
                win3_active = False
                win1.UnHide()
                break

    elif ev1 == 'Monthly Usage' and not win4_active:

        win4_active = True
        win1.Hide()
        layout4 = [[sg.Text('Monthly Usage',font=("Helvetica", 15))],
                   [sg.Text('Current Usage Level: {}'.format(monthly_level))],
                   [sg.Text('Usage: {}kW'.format(monthly_usage_kWh))],
                   [sg.Button("Show Usage Breakdowns")],# note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win4 = sg.Window('Monthly Usage', layout4)
        while True:
            ev4, vals4 = win4.Read()
            if ev4 == 'Show Usage Breakdowns':
                fig_week = go.Figure(data=[go.Pie(labels=name_month, values=percent_month)])
                fig_week.show()

            elif ev4 == 'Exit':
                win4.Close()
                win4_active = False
                win1.UnHide()
                break

    elif ev1 == "Tips" and not win5_active:
        win5_active = True
        win1.Hide()
        layout5 = [[sg.Text('Tips')],
                   [sg.Text("1. Unplug Appliances and Turn off Lights. When you're not using appliances, "
                            "make sure you turn them off.")],
                   [sg.Text("2. Hand-Wash the Dishes.")],
                   [sg.Text("3. Heating and AC Efficiency.")],
                   [sg.Text("4. Defrost Frozen Foods before You Cook Them.")],
                   [sg.Text("5. Buy Energy Efficient Lighting.")],
                   [sg.Text("7. Replace your light bulbs.")],
                   [sg.Text("8. Use smart power strips.")],
                   [sg.Text("9. Install a programmable or smart thermostat.")],
                   [sg.Text("10. Purchase energy efficient appliances.")],
                   [sg.Text("11. Reduce your water heating expenses.")],
                   [sg.Text("12. Install energy efficient windows.")],
                   [sg.Text("13. Upgrade your HVAC (Heating, Ventilation, Air Conditioning) system.")],
                   [sg.Button('Exit')]]
        win5 = sg.Window('Tips', layout5)
        while True:
            ev5, vals5 = win5.Read()
            if ev5 == 'Exit':
                win5.Close()
                win5_active = False
                win1.UnHide()
                break

    elif ev1 == "Cancel":
        break

win1.close()
