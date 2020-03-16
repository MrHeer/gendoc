import argparse

version = "0.0.1"


def gendoc(data, templateDir, outputDir):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from json file through .docx template.")
    parser.add_argument("-d", "--data", help="json file")
    parser.add_argument("-t", "--templateDir", help="template directory")
    parser.add_argument("-o", "--outputDir", help="output directory")
    parser.add_argument("-v", "--version",
                        help="version info", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(version)
        parser.exit()

    if args.data and args.templateDir and args.outputDir:
        gendoc(args.data, args.templateDir, args.outputDir)
    else:
        parser.print_help()
        parser.exit()
