import unittest

from pkg_resources import resource_filename
from qextractor.preprocessing import baseline
from qextractor.preprocessing import globoquotes

GLOBOQUOTES_FILE = resource_filename('qextractor', 'data/corpus-globocom-cv.txt')

class TestBaseline(unittest.TestCase):
    _corpus = None

    @classmethod
    def setUpClass(cls):
        cls._corpus = globoquotes.load(GLOBOQUOTES_FILE)
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_detoken(self):

        #sne = [ e[0] for e in self._corpus[0] ]
        sne = ["O", "cachorro", "abanou", "o", "rabo", "."]
        resp1 = "  O cachorro abanou o rabo .\n"
        resp2 = [0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,4,4,4,4,4,5,5]

        text, tr = baseline.detoken(sne)
        #print(text)
        #print(tr)
        self.assertTrue(text == resp1 and resp2 == tr)

    def test_boundedChunk(self):
        s = [["\'"], ["Basta"], ["\'"], [","], ["disse"], ["o"], ["guarda"], ["."], ["\""], ["Agora"], [","], ["só"], ["nos"], ["resta"], ["esperar"], ["\""], [","], ["falou"], ["o"], ["sol."], ["-"], ["A"], ["vida"], ["é"], ["-"], ["afirmou"], ["a"], ["presidente"], ["."]]

        bc = baseline.boundedChunk(s)
        #for i in range(len(bc)):
        #    print(s[i][0], bc[i])

        self.assertTrue(True)


    def test_firstLetterUpperCase(self):
        s = [["Guilherme"],["disse"],["a"], ["Maria"], [":"], ["olha"], ["lá"], ["!"]]
        resp = [1,0,0,1,0,0,0,0]

        uc = baseline.firstLetterUpperCase(s)

        self.assertEqual(uc, resp)

    def test_verbSpeechNeighb(self):
        s = [["disse", "VSAY"], ["o", "XX"], ["juiz", "ABC"], ["de", "PREP"], ["o", "ART"]]
        resp = [1,1,1,0,0]

        vsn = baseline.verbSpeechNeighb(s)

        self.assertEqual(resp, vsn)

    def test_quotationStart(self):
        # Sentence that fits in the first regular expression rule:
        qs = baseline.quotationStart(self._corpus[0])
        #for i in range(len(qs)):
        #    print(self._corpus[0][i][0], "\t", qs[i])

        # Sentence that fits in the second regular expression rule:
        qs = baseline.quotationStart(self._corpus[231])
        #for i in range(len(qs)):
        #    print(self._corpus[231][i][0], "\t", qs[i])

        self.assertTrue(True)

    def test_quotationEnd(self):
        # Sentence that fits in the first regular expression rule:
        qs = baseline.quotationStart(self._corpus[0])
        qe = baseline.quotationEnd(self._corpus[0], qs)

        # Sentence that fits in the second regular expression rule:
        qs = baseline.quotationStart(self._corpus[231])
        qe = baseline.quotationEnd(self._corpus[231], qs)

        self.assertTrue(True)

    def test_quoteBounds(self):
        # Sentence that fits in the first regular expression rule:
        qs = baseline.quotationStart(self._corpus[0])
        qe = baseline.quotationEnd(self._corpus[0], qs)
        qb = baseline.quoteBounds(qs, qe)
        #for i in range(len(qe)):
        #    print(self._corpus[0][i][0], "\t", qs[i], qe[i], qb[i])

        # Sentence that fits in the second regular expression rule:
        qs = baseline.quotationStart(self._corpus[231])
        qe = baseline.quotationEnd(self._corpus[231], qs)
        qb = baseline.quoteBounds(qs, qe)
        #for i in range(len(qe)):
        #    print(self._corpus[231][i][0], "\t", qs[i], qe[i], qb[i])

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()