import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from pandas import read_csv

north_pole = read_csv('assets/N_seaice_extent_daily_v3.0.csv')
south_pole = read_csv('assets/S_seaice_extent_daily_v3.0.csv')



years = [str(x) for x in range(1979, 2021)]
months = [x for x in range(1,13)]

print(years)


# year = '2019'
# for month in months:
#     month = str(month)
#     # year wise dataset of North Pole including month of years and extent of ice
#     north_data_year = north_pole.loc[north_pole["Year"]==year]

#     # year wise dataset of South Pole including month of years and extent of ice
#     south_data_year = south_pole.loc[south_pole["Year"]==year]

#     #month wise dataset of North Pole including day of month and extent of ice
#     north_data_month = north_data_year.loc[north_data_year["Month"]==month, ["Day","Extent"]]

#     #month wise dataset of South Pole including day of month and extent of ice
#     south_data_month = south_data_year.loc[south_data_year["Month"]==month, ["Day","Extent"]]

    # m = [None,"Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    # month_name = m[int(month)]
    # plot for month wise data at North Pole
    # plot for month wise data at North Pole
    # plt.plot(north_data_month["Day"],north_data_month["Extent"], color='r')
    # plt.xlabel(f"Days of {month_name} Month", color='g')
    # plt.ylabel(f"Extent of Ice (x10^6 Sq Km)",color='g')
    # plt.title(f"Extent of Ice at North Pole in {month_name} 2019", color='r')
    # plt.grid(True, color='b')
    # plt.rc('lines', linewidth=2, linestyle='-', marker='*')
    # plt.rcParams["figure.figsize"] = (20, 10)
    # plt.savefig('static/images/' + 'north_2019' + '_' + month + '.png')
    # print(north_data_year)
    # print()
    # print(south_data_year)
    # print()
    # print(north_data_month)
    # print()
    # print(south_data_month)