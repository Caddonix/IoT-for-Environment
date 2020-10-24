import pandas as pd
from flask import Flask, render_template, url_for, request, redirect, make_response
from random import choice, random
import json
from time import time
app = Flask(__name__)

# complete dataset of North Pole
north_pole = pd.read_csv('assets/N_seaice_extent_daily_v3.0.csv')

# complete dataset of South Pole
south_pole = pd.read_csv('assets/S_seaice_extent_daily_v3.0.csv')

months = [None, "Jan", "Feb", "Mar", "Apr", "May",
          "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


@app.route('/', methods=["GET", "POST"])
def main():
    year = None
    month = None
    month_name = None
    data_north = []
    data_south = []
    if request.method == 'POST':
        year = request.form.get("year")
        month = request.form.get("month")
        month_name = months[int(month)]

        # year wise dataset of North Pole including month of years and extent of ice
        north_data_year = north_pole.loc[north_pole["Year"]==year]

        # year wise dataset of South Pole including month of years and extent of ice
        south_data_year = south_pole.loc[south_pole["Year"]==year]

        #month wise dataset of North Pole including day of month and extent of ice
        north_data_month = north_data_year.loc[north_data_year["Month"]==month, ["Extent"]]

        #month wise dataset of South Pole including day of month and extent of ice
        south_data_month = south_data_year.loc[south_data_year["Month"]==month, ["Extent"]]

        n = pd.Series(north_data_month["Extent"]).reset_index(drop=True)
        s = pd.Series(south_data_month["Extent"]).reset_index(drop=True)
        data_north = []
        data_south = []

        for i in range(len(n)):
            a = [i, float(n[i])]
            b = [i, float(s[i])]
            data_north.append(a)
            data_south.append(b)

    return render_template('index.html', north = data_north, south = data_south, year=year, month_name=month_name)
        

        # if(pole == 'N' or pole == 'n'):
            
            # plot for month wise data at North Pole
            # plt.plot(north_data_month["Day"],
            #          north_data_month["Extent"], color='r')
            # plt.xlabel(f"Days of {month_name} Month", color='g')
            # plt.ylabel(f"Extent of Ice (x10^6 Sq Km)", color='g')
            # plt.title(
            #     f"Extent of Ice at North Pole in {month_name} {year}", color='r')
            # plt.grid(True, color='b')
            # plt.figure()

            # figfile = BytesIO()
            # plt.savefig(figfile, format='png')
            # figfile.seek(0)  # rewind to beginning of file
            # figdata_png = base64.b64encode(figfile.getvalue())


            # plt.rc('lines', linewidth=2, linestyle='-', marker='*')
            # plt.rcParams["figure.figsize"] = (20, 10)
            # plt.savefig('/static/images/' + str(year) +
            #             '_' + str(month) + '_north' + '.png')
            # url = '/static/images/' + \
            #     str(year) + '_' + str(month) + '_south' + '.png'


        # elif(pole == 'S' or pole == 's'):
        #     # plot for month wise data at South Pole
        #     plt.plot(south_data_month["Day"],
        #              south_data_month["Extent"], color='r')
        #     plt.xlabel(f"Days of {month_name} Month", color='g')
        #     plt.ylabel(f"Extent of Ice (x10^6 Sq Km)", color='g')
        #     plt.title(
        #         f"Extent of Ice at South Pole in {month_name} {year}", color='r')
        #     plt.grid(True, color='b')
        #     plt.rc('lines', linewidth=2, linestyle='-', marker='*')
        #     plt.rcParams["figure.figsize"] = (20, 10)
        #     plt.savefig('/static/images/' + str(year) +
        #                 '_' + str(month) + '_south' + '.png')
        #     url = '/static/images/' + \
        #         str(year) + '_' + str(month) + '_south' + '.png'
        # else:
        #     url = '/static/images/ice_caps_pseudo.jpg'

    


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, TemperatureS, TemperatureN]

    TemperatureS = choice((-55, -52))
    TemperatureN = choice((-12, -10))

    data = [time() * 1000, TemperatureS, TemperatureN]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
