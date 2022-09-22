import pandas

FILE_NAME = "weather_data.csv"


def main() -> None:
    r = pandas.read_csv(FILE_NAME)
    temperatures = r["temp"].to_list()

    # print(r[r.temp == r.temp.max()].day)

    r = r.assign(Fahrenheit=lambda x: (9 / 5) * x["temp"] + 32)

    monday = r[r.day == "Monday"]
    print(int(monday.Fahrenheit))


if __name__ == "__main__":
    main()
