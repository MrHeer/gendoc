import argparse

version = "0.0.1"


def gendoc(data, template, output):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from data(csv, excel, etc) through .docx template.")
    parser.add_argument("-d", "--data", help="input data(csv, excel, etc")
    parser.add_argument("-t", "--template", help="template file(.docx)")
    parser.add_argument("-o", "--output", help="output file name")
    parser.add_argument("-v", "--version",
                        help="version info", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(version)
        parser.exit()

    if args.data and args.template and args.output:
        gendoc(args.data, args.template, args.output)
    else:
        parser.print_help()
        parser.exit()
