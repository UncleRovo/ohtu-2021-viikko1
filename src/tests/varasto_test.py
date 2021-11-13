import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_varasto_ei_mene_negatiiviseksi(self):
        self.varasto.ota_varastosta(20)
        
        self.assertEqual(self.varasto.saldo, 11)
    
    def test_varastoon_ei_mene_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(20)
      
        self.assertEqual(self.varasto.saldo, 10)
    
    def test_toString_toimii_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        
    def test_negatiivista_maaraa_ei_oteta(self):
        
        self.assertEqual(self.varasto.ota_varastosta(-2), 0)
        
    def test_negatiivista_maaraa_ei_lisata(self):
        self.varasto.lisaa_varastoon(-33)
        self.assertEqual(self.varasto.saldo, 0)

    def test_ylijaama_menee_hukkaan(self):
        self.varasto.lisaa_varastoon(12)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)
       
    def test_virheinit_nollaa_kaiken(self):
        self.varasto = Varasto(-2)
        self.assertEqual(self.varasto.tilavuus, 0.0)
        
    def test_virheinit_ja_vaara_alkusaldo(self):
        self.varasto = Varasto(10, -2)
        self.assertEqual(self.varasto.saldo, 0)
