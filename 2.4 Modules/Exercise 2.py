import DataScienceBasics as dsb

def main():
    data = dsb.load_data('data.txt')
    new_data = dsb.filter_data(data, lambda x: x['score'] != 100)
    new_data = dsb.transform_data(new_data, 'score', lambda x: x - 5)
    stats = dsb.describe_data(new_data, 'score')

    print(f"Unique Players: {dsb.get_unique_values(new_data, 'name')}")
    print(f"Score Mean: {stats[0]}\nScore Median: {stats[1]}")
    print(f"Players By Age:\n{dsb.aggregate_data(new_data, 'age')}")

if __name__ == "__main__":
    main()


