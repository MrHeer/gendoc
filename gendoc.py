import argparse
import csv
import json
import os

from concurrent.futures import ThreadPoolExecutor
from docxtpl import DocxTemplate
from os import path


version = "0.0.1"
maxThread = 20


def genDocument(context, templateFile, outputFile):
    doc = DocxTemplate(templateFile)
    doc.render(context)
    print("Generate document: " + outputFile)
    doc.save(outputFile)


def loadCsv(csvPath):
    with open(csvPath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data


def checkDir(dir):
    if not path.exists(dir):
        print("Directory not found: " + dir)
        os.makedirs(dir)
        print("Create directory: " + dir)


def gendocRunner(inputFile, outputDir, templateFile):
    checkDir(outputDir)
    data = loadCsv(inputFile)
    for row in data:
        outputFile = path.join(outputDir, row['fileName'])
        del row['fileName']
        genDocument(row, templateFile, outputFile)


def loadConfig(configPath):
    with open(configPath) as f:
        config = json.load(f)
        return config


def runTasks(tasks, executor):
    for task in tasks:
        inputFile = task['inputFile']
        outputDir = task['outputDir']
        templateFile = task['templateFile']
        executor.submit(gendocRunner, inputFile, outputDir, templateFile)


def gendoc(configPath, thread):
    if thread > maxThread:
        thread = maxThread

    config = loadConfig(configPath)
    tasks = config['tasks']
    with ThreadPoolExecutor(max_workers=thread) as executor:
        runTasks(tasks, executor)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from csv file through .docx template.")
    parser.add_argument(
        "-c", "--config", default="./config.json", help="config file")
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
