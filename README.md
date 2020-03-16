# gendoc

Generate docx from csv file through .docx template.

## Usage

```bash
$python gendoc --config=config.json
```

### Example of the `config.json` file

```json
{
    "tasks": [
        {
            "inputFile": "./input/student.csv",
            "outputDir": "./output/",
            "templateFile": "./template/Student.docx"
        },
        {
            "inputFile": "./input/teacher.csv",
            "outputDir": "./output/",
            "templateFile": "./template/Teacher.docx"
        }
    ]
}
```

> Note: the `fileName` field is necessary in the `inputFile`.
