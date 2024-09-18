import unittest
import gendoc


class Testgendoc(unittest.TestCase):

    def test_gendoc(self):
        gendoc.gen_doc("./config.json", 5)

    def test_gen_document(self):
        context = {"name": "Aden", "age": "12"}
        template_file = "./template/Student.docx"
        output_file = "./output/StudentAden.docx"
        gendoc.gen_document(context, template_file, output_file)


if __name__ == "__main__":
    unittest.main()
