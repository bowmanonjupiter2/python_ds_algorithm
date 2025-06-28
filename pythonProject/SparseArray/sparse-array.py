import sys


def file_to_sparse_array(file_path):
    collection = []

    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

    if lines.__len__() == 0:
        print("File is empty.")
        return

    for line in lines:
        try:
            row, col, value = map(int, line.split(','))
            collection.append([row, col, value])
        except ValueError:
            print(f"Error: Invalid line format '{line}'. Each line should contain 'row col value'.")
            sys.exit(1)

    result = [[0 for _ in range(collection[0][1])] for _ in range(collection[0][0])]

    # skip the first element in collection as it contains the dimensions
    for row, col, value in collection[1:]:
        if row >= len(result) or col >= len(result[0]):
            print(f"Error: Index out of bounds for row {row}, column {col}.")
            sys.exit(1)
        result[row][col] = value

    return result


def sparse_array_to_file(sparse_array):
    if sparse_array is None:
        print(f'Error: Sparse array is None.')
        sys.exit(1)
    result = []

    non_zero = 0
    for i in range(len(sparse_array)):
        for j in range(len(sparse_array[0])):
            if sparse_array[i][j] != 0:
                result.append([i, j, sparse_array[i][j]])
                non_zero += 1
    result.insert(0, [len(sparse_array), len(sparse_array[0]), non_zero])
    return result


def main():
    path = input("Enter the file path: ")
    result = file_to_sparse_array(path)
    if result:
        print("Sparse Array:")
        for row in result:
            print(' '.join(map(str, row)))

        sparse_result = sparse_array_to_file(result)
        if sparse_result:
            print("\nSparse Array Representation:")
            for row in sparse_result:
                print(', '.join(map(str, row)))


if __name__ == "__main__":
    main()
