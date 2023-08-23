import argparse
import sys
from collections import Counter
from typing import List, Optional, Union, TextIO


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        if 'expected one argument' in message and '-sortingType' in message:
            print("No sorting type defined!")
            sys.exit()
        elif 'expected one argument' in message and '-dataType' in message:
            print('No data type defined!')
            sys.exit()
        else:
            self.print_usage(sys.stderr)
            print(f"Error: {message}")


def parse_arguments() -> argparse.Namespace:
    parser = CustomArgumentParser()
    parser.add_argument('-dataType', choices=['long', 'line', 'word'])
    parser.add_argument('-sortingType', choices=['byCount', 'natural'])
    parser.add_argument('-inputFile', type=argparse.FileType('r'))
    parser.add_argument('-outputFile', type=argparse.FileType('w'))
    args, unknown = parser.parse_known_args()

    if unknown:
        [print(f'"{arg_}" is not a valid parameter. It will be skipped.') for arg_ in unknown]

    return args


def get_input(data_type: str, file_obj: Optional[TextIO] = None) -> List[str]:
    line = file_obj.readline().strip() if file_obj else input()
    return line.split() if data_type in ['long', 'word'] else [line]


def get_input_lines(data_type: str, file_obj: Optional[TextIO] = None):
    while True:
        try:
            data = get_input(data_type, file_obj)
            if not data:
                break
            yield data
        except EOFError:
            break


def process_num(num: str) -> Optional[int]:
    try:
        return int(num)
    except ValueError:
        print(f'{num} is not a long. It will be skipped')
        return None


def custom_print(message: str, file_obj: Optional[TextIO] = None) -> None:
    if file_obj:
        file_obj.write(message + '\n')
    else:
        print(message)


def output_natural(data: List[Union[int, str]], data_type: str, file_obj: Optional[TextIO] = None) -> None:
    custom_print(f'Total {data_type}s: {len(data)}', file_obj)
    sep = '\n' if data_type == 'line' else ' '
    custom_print('Sorted data:' + sep.join(map(str, sorted(data))), file_obj)


def output_by_count(data: List[tuple], data_type: str, file_obj: Optional[TextIO] = None) -> None:
    total_count = sum(count for _, count in data)
    custom_print(f'Total {data_type}s: {total_count}.', file_obj)
    for data_tuple in data:
        custom_print(f'{data_tuple[0]}: {data_tuple[1]} time(s), {int((data_tuple[1] / total_count) * 100)}%.', file_obj)


def main() -> None:
    args = parse_arguments()
    input_list = []
    data_type = args.dataType or 'word'
    process_func = process_num if data_type == 'long' else lambda x: x

    if args.inputFile:
        with args.inputFile as file_obj:
            input_generator = get_input_lines(data_type, file_obj)
            for data in input_generator:
                input_list.extend(process_func(el) for el in data if process_func(el) is not None)

    if args.sortingType == 'byCount':
        counted_input_list = sorted(Counter(input_list).items(), key=lambda x: (x[1], x[0]))
        output_by_count(counted_input_list, data_type, args.outputFile)
    else:
        output_natural(input_list, data_type, args.outputFile)

    if args.outputFile:
        args.outputFile.close()


if __name__ == "__main__":
    main()
