"""对xlsx文件的读写"""
import unittest
import openpyxl


class TestOpenpyxl(unittest.TestCase):

    def setUp(self):
        self.file = "lib\\openpyxl\\demo.xlsx"
        self.sheetname = "Sheet1"
        self.wb = openpyxl.load_workbook(self.file)
        self.sh = self.wb[self.sheetname]
        pass

    def tearDown(self):
        pass

    def testRead(self):
        print(self.wb.sheetnames)
        print(self.sh)
        cell = self.sh["A1"]
        print(type(cell))
        cell = self.sh.cell(1, 100)
        print(type(cell))
        print(cell.value)

    def testWrite(self):
        cell = self.sh["C1"]
        cell.value = 0
        self.wb.save(self.file)

    def testTraverse(self):
        """遍历"""
        pass

    def testSave(self):
        a = list(range(10))
        wb = openpyxl.Workbook()
        ws = wb.active
        for i in range(10):
            ws.cell(i+1, i+1).value = a[i]
        wb.save("lib\\openpyxl\\demo2.xlsx")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestOpenpyxl("testRead"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
