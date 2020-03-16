import argparse
import csv
import json
import threading

from concurrent.futures import ThreadPoolExecutor
from docxtpl import DocxTemplate
from os import path


version = "0.0.1"
maxThread = 20


def genDocument(context, templateFile, outputFile):
    doc = DocxTemplate(templateFile)
    doc.render(context)
    doc.save(outputFile)


def gendocRunner(inputFile, outputDir, templateFile):
    with open(inputFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            outputFile = path.join(outputDir, row['fileName'])
            del row['fileName']
            genDocument(row, templateFile, outputFile)


def gendoc(config, thread):
    if thread > maxThread:
        thread = maxThread

    executor = ThreadPoolExecutor(thread)
    with open(config) as f:
        data = json.load(f)
        with ThreadPoolExecutor(max_workers=thread) as executor:
            for task in data['tasks']:
                executor.submit(gendocRunner, task['inputFile'], task['outputDir'],
                                task['templateFile'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from csv file through .docx template.")
    parser.add_argument("-c", "--config", help="config file")
    parser.add_argument("-m", "--maxThread", default=5,
                        help="max number of thread", type=int)
    parser.add_argument("-v", "--version",
                        help="version info", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(version)
        parser.exit()

    if args.config:
        gendoc(args.config, args.maxThread)
    else:
        parser.print_help()
        parser.exit()
