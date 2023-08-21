import argparse
import sys
from collections import Counter


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        if 'expected one argument' in message and '-sortingType' in message:
            print("No sorting type defined!")
            sys.exit()
        elif 'expected one argument' in message and '-dataType' in message:
            print('No data type defined!')
            sys.exit()
        else:
            self.print_usage(sys.stderr)
            print(f"Error: {message}")


def parser():
    parser = CustomArgumentParser()
    parser.add_argument('-dataType', choices=['long', 'line', 'word'])
    parser.add_argument('-sortingType', choices=['byCount', 'natural'])
    parser.add_argument('-inputFile')
    parser.add_argument('-outputFile')
    args, unknown = parser.parse_known_args()

    if unknown:
        [print(f'"{arg_}" is not a valid parameter. It will be skipped.') for arg_ in unknown]

    return args


def get_input(data_type, file_obj=None):
    line = file_obj.readline().strip() if file_obj else input()
    return line.split() if data_type in ['long', 'word'] else [line]


def process_num(num):
    try:
        return int(num)
    except ValueError:
        print(f'{num} is not a long. It will be skipped')
        return None


def output_natural(data, data_type, file_obj=None):
    custom_print(f'Total {data_type}s: {len(data)}', file_obj)
    sep = '\n' if data_type == 'line' else ' '
    custom_print('Sorted data:' + sep.join(map(str, sorted(data))), file_obj)


def output_by_count(data, data_type, file_obj=None):
    total_count = sum(count for _, count in data)
    custom_print(f'Total {data_type}s: {total_count}.', file_obj)
    for data_tuple in data:
        custom_print(f'{data_tuple[0]}: {data_tuple[1]} time(s), {int((data_tuple[1] / total_count) * 100)}%.', file_obj)


def custom_print(message, file_obj=None):
    if file_obj:
        file_obj.write(message + '\n')
    else:
        print(message)


def main():
    args = parser()
    input_list = []
    data_type = args.dataType or 'word'
    process_func = process_num if data_type == 'long' else lambda x: x
    output_file = open(args.outputFile, 'w') if args.outputFile else None

    if args.inputFile:
        with open(args.inputFile, 'r') as file_obj:
            while True:
                data = get_input(data_type, file_obj)
                if not data:  # Break the loop if there is no more data
                    break
                input_list.extend(process_func(num) for num in data if process_func(num) is not None)
    else:
        while True:
            try:
                data = get_input(data_type)
                input_list.extend(process_func(num) for num in data if process_func(num) is not None)
            except EOFError:
                break

    if not args.sortingType or args.sortingType == 'natural':
        output_natural(input_list, data_type, output_file)
    else:
        counted_input_list = sorted(Counter(input_list).items(), key=lambda x: (x[1], x[0]))
        output_by_count(counted_input_list, data_type, output_file)

    if output_file:
        output_file.close()


if __name__ == "__main__":
    main()
