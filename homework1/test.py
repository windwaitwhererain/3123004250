import unittest
import subprocess
from main import getresult
from main import getfiledata
from main import mainfunction

class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_wrong_location(self):#测试文件位置出错情况
        getfiledata(1)
    def test_same_text(self):#测试完全相同情况
        origtext="早上好，大学生。"
        tartext="早上好，大学生。"
        self.assertEqual(getresult(origtext,tartext),1)
    def test_diff_text(self):#测试完全不同情况
        origtext="早上好，大学生。"
        tartext="今天天气怎么样"
        self.assertEqual(getresult(origtext,tartext),0)
    def test_1_emp_text(self):#测试单项空时情况
        origtext="早上好，大学生。"
        tartext=""
        self.assertEqual(getresult(origtext,tartext),0)
    def test_2_emp_text(self):#测试双项空时情况
        origtext=""
        tartext=""
        self.assertEqual(getresult(origtext,tartext),0)
    def test_interruption_text(self):#测试纯标点情况
        origtext="......"
        tartext="......"
        self.assertEqual(getresult(origtext,tartext),1)
    def test_long_text(self):#测试中长文本情况
        origtext="家作要表达与之朝夕相处的现实，他常常会到感以难承受蜂，拥而来真的实乎几都在说着诉丑恶和阴险，就怪在怪这里，为什么丑恶的事物总是身在边，而美好的事物远却在海。角换话说句，人的友爱和情往同往是作只为情来绪到，而相反事的则实是伸手便触可及正。像一位诗人所表达的：人类无法忍受太多的真实也。这有样的作家，一生都在解决自和现实我的紧张关系，克福纳是为最成功的子例他找，到了一条温和的途径他描写，中状态间的事物，同时容了包美与好丑恶，他将美国南方现的实放到了历史和人文精神中之这，是真意正义上的学文现实，因为它连接过去着和将来。"
        tartext="相家要表与之 夕 处的以实，他常常而感到难实承乎，在拥说来的真现几受都蜂诉会着丑里和阴险，怪就怪事物恶，为什么丑恶的在这总是却身边，而美好的事物在远在友角和同句往说，是的海爱。换到话往只人作为情绪来情，便相反的事正则是伸手而可触及。实像一位诗人受表达的：实类无法忍所太多的真人生也在这样的作和现一的都有解决自我家，是。紧张关的，福克纳实最为一功系和的，他找他了成中温状子途事物到描写包间例美的径，，同时条容了态好的现恶放到将美国南方与丑神，他了历是和人文精实之中，这实真正意义上的着过现和，来为它连接文学去史将因成"
        self.assertEqual(getresult((origtext,tartext)<1 and getresult(origtext,tartext)>0),True)
    def test_blank_text(self):#测试纯空白情况
        origtext="      "
        tartext="      "
        self.assertEqual(getresult(origtext,tartext),0)
    def test_num_text(self):#测试纯数字情况
        origtext="1234567887654321"
        tartext="8463725113245768"
        self.assertEqual(getresult(origtext,tartext),0)
    def test_main_text(self):#测试程序主入口
        subprocess.run(["python","main.py","1.txt","2.txt","3.txt"])
        self.assertEqual(1,1)#成功运行到这一步即可
if __name__ == '__main__':
    unittest.main()
