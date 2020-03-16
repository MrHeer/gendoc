# gendoc

Generate docx from json file through .docx template.

## Usage

```bash
$python gendoc --data=input.json --templateDir=./templatetpl --outputDir=./output
```

### Example of the json file

```json
[
    {
        "templateFile": "Student.docx",
        "id": [
            "fileName", // it's necessary
            "name",
            "age",
            ...
        ],
        "value": [
            [
                "StudentAiden.docx",
                "Aiden",
                "12",
                ...
            ],
            ...
        ]
    },
    ...
]
```
