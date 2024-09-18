# gendoc

Generate docx from csv file through .docx template.

## Usage

```bash
usage: gendoc.py [-h] [-c CONFIG] [-t THREADS] [-v]

Generate docx from csv file through .docx template.

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        config file
  -t THREADS, --threads THREADS
                        number of threads (max 20)
  -v, --version         version info
```

### Example of the `config.json` file

```json
{
    "tasks": [
        {
            "input_file": "./input/student.csv",
            "output_dir": "./output/",
            "template_file": "./template/Student.docx"
        },
        {
            "input_file": "./input/teacher.csv",
            "output_dir": "./output/",
            "template_file": "./template/Teacher.docx"
        }
    ]
}
```

> Note: the `file_name` field is necessary in the `input_file`.
