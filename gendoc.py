import argparse

version = "0.0.1"


def gendoc(config):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from csv file through .docx template.")
    parser.add_argument("-c", "--config", help="config file")
    parser.add_argument("-v", "--version",
                        help="version info", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(version)
        parser.exit()

    if args.config:
        gendoc(args.config)
    else:
        parser.print_help()
        parser.exit()
