import argparse
import csv
import json
from typing import Dict, List

from concurrent.futures import ThreadPoolExecutor
from docxtpl import DocxTemplate
from os import path, makedirs


VERSION = "0.0.2"
ENCODING = "utf-8"
MAX_THREADS = 20


def generate_document(
    context: Dict[str, str],
    template_file: str,
    output_file: str,
) -> None:
    """Generate a docx file from a template and a context dictionary.

    Args:
        context (Dict[str, str]): A dictionary of key-value pairs that will be
            used to replace placeholders in the template.
        template_file (str): The path to the docx template file.
        output_file (str): The path to the file where the generated docx will
            be saved.
    """
    doc = DocxTemplate(template_file)
    doc.render(context)
    doc.save(output_file)
    print(f"Generated docx to {output_file}.")


def create_directory_if_not_exists(directory: str) -> None:
    """Create a directory if it does not already exist.

    Args:
        directory (str): The path to the directory that should be created.
    """
    if not path.exists(directory):
        makedirs(directory)


def generate_documents(
    rows: List[Dict[str, str]],
    output_directory: str,
    template_file: str,
) -> None:
    """Generate multiple docx files from a list of rows and a template.

    Args:
        rows (List[Dict[str, str]]): A list of dictionaries, where each dictionary
            represents a single docx file that should be generated.
        output_directory (str): The path to the directory where the generated
            docx files should be saved.
        template_file (str): The path to the docx template file.
    """
    for row in rows:
        output_file = path.join(output_directory, row["file_name"])
        generate_document(row, template_file, output_file)


def run_task(
    input_file: str,
    output_directory: str,
    template_file: str,
) -> None:
    """Run a single task by reading a csv file, generating a docx file from
    each row, and saving it to the specified directory.

    Args:
        input_file (str): The path to the csv file that should be read.
        output_directory (str): The path to the directory where the generated
            docx files should be saved.
        template_file (str): The path to the docx template file.
    """
    with open(input_file, encoding=ENCODING) as csv_file:
        rows = csv.DictReader(csv_file)
        generate_documents(rows, output_directory, template_file)


def load_configuration(config_path: str) -> Dict[str, List[Dict[str, str]]]:
    """Load a configuration from a json file.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        Dict[str, List[Dict[str, str]]]: A dictionary containing the
            configuration. The dictionary should have a single key, "tasks",
            which maps to a list of dictionaries. Each dictionary in the list
            should contain the following keys:

                - "input_file": The path to the csv file that should be read.
                - "output_directory": The path to the directory where the
                    generated docx files should be saved.
                - "template_file": The path to the docx template file.
    """
    with open(config_path, encoding=ENCODING) as f:
        return json.load(f)


def run_tasks(
    tasks: List[Dict[str, str]],
    executor: ThreadPoolExecutor,
) -> None:
    """Run a list of tasks in parallel using a ThreadPoolExecutor.

    Args:
        tasks (List[Dict[str, str]]): A list of dictionaries, where each
            dictionary represents a single task. Each dictionary should contain
            the following keys:

                - "input_file": The path to the csv file that should be read.
                - "output_directory": The path to the directory where the
                    generated docx files should be saved.
                - "template_file": The path to the docx template file.
        executor (ThreadPoolExecutor): The ThreadPoolExecutor that should be
            used to run the tasks.
    """
    for task in tasks:
        input_file = task["input_file"]
        output_directory = task["output_dir"]
        template_file = task["template_file"]
        create_directory_if_not_exists(output_directory)
        executor.submit(run_task, input_file, output_directory, template_file)


def generate_documents_from_config(
    config_path: str,
    threads: int,
) -> None:
    """Generate docx files from a configuration file.

    Args:
        config_path (str): The path to the configuration file.
        threads (int): The number of threads to use when generating the docx
            files. If this number is greater than MAX_THREADS, it will be
            capped at MAX_THREADS.
    """
    if threads > MAX_THREADS:
        threads = MAX_THREADS

    configuration = load_configuration(config_path)
    tasks = configuration["tasks"]
    with ThreadPoolExecutor(max_workers=threads) as executor:
        run_tasks(tasks, executor)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate docx from csv file through .docx template."
    )
    parser.add_argument(
        "-c",
        "--config",
        default="./config.json",
        help="config file",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--threads",
        default=5,
        help="number of threads (max {})".format(MAX_THREADS),
        type=int,
    )
    parser.add_argument(
        "-v",
        "--version",
        help="version info",
        action="store_true",
    )
    args = parser.parse_args()

    if args.version:
        print(VERSION)
        parser.exit()

    if args.config:
        generate_documents_from_config(args.config, args.threads)
        print("Generated all docx files.")
    else:
        parser.print_help()
        parser.exit()
