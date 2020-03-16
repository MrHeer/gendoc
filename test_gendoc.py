import unittest
import gendoc


class Testgendoc(unittest.TestCase):

    def test_gendoc(self):
        gendoc.gendoc("./config.json", 5)

    def test_genDocument(self):
        context = {"name": "Aiden", "age": "12"}
        templateFile = './template/Student.docx'
        outputFile = './output/StudentAiden.docx'
        gendoc.genDocument(context, templateFile, outputFile)


if __name__ == '__main__':
    unittest.main()
