import pandas

FILE_NAME = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"


def main() -> None:
    df = pandas.read_csv(FILE_NAME)
    print(df.groupby("Primary Fur Color").size())


if __name__ == "__main__":
    main()
