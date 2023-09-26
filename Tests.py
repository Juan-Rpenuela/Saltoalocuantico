import unittest
import matplotlib.pyplot as plot
import saltoalocuant as sac
import math

class TestSalto_Clasico_Cuantico(unittest.TestCase):
        def test_canica(self):
                v1 = [2,4,6]
                w1 = [[0,0,1],[1,0,0],[0,1,0]]
                clics1 = 5
                resultm = [4, 6, 2]
                resultc = sac.Canicas(w1,v1,clics1)
                self.assertEqual(resultm, resultc)

        def test_canica2(self):
                v2 = [4,8,9,1]
                w2 = [[0,1,0,1],[0,0,1,0],[1,0,0,0],[0,0,0,0]]
                clics2 = 3
                resultm = [4, 9, 9, 0]
                resultc = sac.Canicas(w2,v2,clics2)
                self.assertEqual(resultm, resultc)

        def test_fracciones(self):
                v1 = [1,0,0]
                w1 = [[1/3,2/3,0],[2/3,1/3,0],[0,0,1]]
                clics1 = 5
                resultm = [0.5, 0.5, 0.0]
                resultc = sac.Fracciones(w1,v1,clics1)
                self.assertEqual(resultm, resultc)

        def test_fracciones2(self):
                v2 = [0,0,1,0]
                w2 = [[3/4,1/4,0,0],[1/4,1/4,1/4,1/4],[0,1/4,3/4,0],[0,1/4,0,3/4]]
                clics2 = 3
                resultm = [0.11, 0.25, 0.53, 0.11]
                resultc = sac.Fracciones(w2,v2,clics2)
                self.assertEqual(resultm, resultc)

        def test_experimentorendijas(self):
                blancos1 = 5
                rendijas1 = 2
                resultm = ([[0, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0, 0.33, 0, 1, 0, 0, 0, 0], [0, 0.33, 0, 0, 1, 0, 0, 0], [0, 0.33, 0.33, 0, 0, 1, 0, 0], [0, 0, 0.33, 0, 0, 0, 1, 0], [0, 0, 0.33, 0, 0, 0, 0, 1]], [0.0, 0.0, 0.0, 0.165, 0.165, 0.33, 0.165, 0.165])
                resultc = sac.ExperimentoRendijas(blancos1,rendijas1)
                self.assertEqual(resultm, resultc)

        def test_experimentorendijas_2(self):
                blancos2 = 6
                rendijas2 = 3
                resultm = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0.5, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0.5, 0.5, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0.5, 0.5, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0.5, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], [0.0, 0.0, 0.0, 0.0, 0.165, 0.33, 0.33, 0.165, 0.0, 0.0])
                resultc = sac.ExperimentoRendijas(blancos2,rendijas2)
                self.assertEqual(resultm, resultc)

        def test_complejosfracciones(self):
                v1 = [1/math.sqrt(3),2j/math.sqrt(15),math.sqrt(2/5)]
                w1 = [[1/math.sqrt(2),1/math.sqrt(2),0],[-1j/math.sqrt(2),1j/math.sqrt(2),0],[0,0,1j]]
                clics1 = 1
                resultm = [(0.408248290463863+0.36514837167011066j), (-0.36514837167011066-0.408248290463863j), 0.6324555320336759j]
                resultc = sac.cplx(w1,v1,clics1)
                self.assertEqual(resultm, resultc)

        def test_complejosfracciones_2(self):
                v2 = [1,0,0,0]
                w2 = [[0,1/math.sqrt(2),1/math.sqrt(2),0],[1/math.sqrt(2),0,0,-1/math.sqrt(2)],[1/math.sqrt(2),0,0,1/math.sqrt(2)],[0,-1/math.sqrt(2),1/math.sqrt(2),0]]
                clics2 = 1
                resultm = [0.0, 0.7071067811865475, 0.7071067811865475, 0.0]
                resultc = sac.cplx(w2,v2,clics2)
                self.assertEqual(resultm, resultc)

        def test_experimentorendijascuantico(self):
                matrix1 = [[0,0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0],[0,(-1+1j)/math.sqrt(6),0,1,0,0,0,0],[0,(-1-1j)/math.sqrt(6),0,0,1,0,0,0],[0,(1-1j)/math.sqrt(6),(-1+1j)/math.sqrt(6),0,0,1,0,0],[0,0,(-1-1j)/math.sqrt(6),0,0,0,1,0],[0,0,(1-1j)/math.sqrt(6),0,0,0,0,1]]
                resultm = [0, 0.7071067811865475, 0.7071067811865475, 0j, 0j, 0j, 0j, 0j]
                resultc = sac.ExperimentoRendijasCua(matrix1)
                self.assertEqual(resultm, resultc)

        def test_experimentorendijascuantico_2(self):
                matrix2 = [[0,0,0,0,0,0,0,0,0],[1/math.sqrt(3),0,0,0,0,0,0,0,0],[1/math.sqrt(3),0,0,0,0,0,0,0,0],[1/math.sqrt(3),0,0,0,0,0,0,0,0],[0,(-1+1j)/math.sqrt(6),0,0,1,0,0,0,0],[0,(-1-1j)/math.sqrt(6),(-1+1j)/math.sqrt(6),0,0,1,0,0,0],[0,(1-1j)/math.sqrt(6),(-1-1j)/math.sqrt(6),(-1+1j)/math.sqrt(6),0,0,1,0,0],[0,0,(1-1j)/math.sqrt(6),(-1-1j)/math.sqrt(6),0,0,0,1,0],[0,0,0,(1-1j)/math.sqrt(6),0,0,0,0,1]]
                resultm = [0,0.5773502691896258,0.5773502691896258,0.5773502691896258,0j,0j,0j,0j,0j]
                resultc = sac.ExperimentoRendijasCua(matrix2)
                self.assertEqual(resultm, resultc)

        def test_grafica(self):
                resultm = None
                resultc = sac.graficar(sac.Fracciones([[1/3,2/3,0],[2/3,1/3,0],[0,0,1]],[1,0,0],1))
                self.assertEqual(resultm, resultc)

        def test_grafica2(self):
                resultm = None
                resultc = sac.graficar(sac.Fracciones([[3/4,1/4,0,0],[1/4,1/4,1/4,1/4],[0,1/4,3/4,0],[0,1/4,0,3/4]],[0,0,1,0],3))
                self.assertEqual(resultm, resultc)

                
if __name__ == "__main__":
        unittest.main()
