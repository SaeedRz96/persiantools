from unittest import TestCase

import pytest

from persiantools import digits


class TestDigits(TestCase):
    def test_en_to_fa(self):
        self.assertEqual(digits.en_to_fa("0987654321"), "۰۹۸۷۶۵۴۳۲۱")
        self.assertEqual(digits.en_to_fa("0987654321"), "۰۹۸۷۶۵۴۳۲۱")
        self.assertEqual(digits.en_to_fa("۰۹۸۷۶۵۴۳۲۱"), "۰۹۸۷۶۵۴۳۲۱")
        self.assertEqual(digits.en_to_fa("+0987654321 abcd"), "+۰۹۸۷۶۵۴۳۲۱ abcd")

        with pytest.raises(TypeError):
            digits.en_to_fa(12345)

    def test_ar_to_fa(self):
        self.assertEqual(digits.ar_to_fa("٠٩٨٧٦٥٤٣٢١"), "۰۹۸۷۶۵۴۳۲۱")
        self.assertEqual(digits.ar_to_fa("٠٩٨٧٦٥٤٣٢١"), "۰۹۸۷۶۵۴۳۲۱")

        orig = "0987٦٥٤٣۲۱"
        converted = digits.en_to_fa(orig)
        converted = digits.ar_to_fa(converted)

        self.assertEqual(converted, "۰۹۸۷۶۵۴۳۲۱")

    def test_fa_to_en(self):
        self.assertEqual(digits.fa_to_en("۰۹۸۷۶۵۴۳۲۱"), "0987654321")

    def test_fa_to_ar(self):
        self.assertEqual(digits.fa_to_ar("۰۹۸۷۶۵۴۳۲۱"), "٠٩٨٧٦٥٤٣٢١")
        self.assertEqual(digits.fa_to_ar(" ۰۹۸۷۶۵۴۳۲۱"), " ٠٩٨٧٦٥٤٣٢١")

    def test_to_letter(self):
        self.assertEqual(digits.to_word(1), "یک")
        self.assertEqual(digits.to_word(12), "دوازده")
        self.assertEqual(digits.to_word(49), "چهل و نه")
        self.assertEqual(digits.to_word(77), "هفتاد و هفت")
        self.assertEqual(digits.to_word(250), "دویست و پنجاه")
        self.assertEqual(digits.to_word(809), "هشتصد و نه")
        self.assertEqual(digits.to_word(1001), "یک هزار و یک")
        self.assertEqual(digits.to_word(3512), "سه هزار و پانصد و دوازده")
        self.assertEqual(digits.to_word(10000), "ده هزار")
        self.assertEqual(digits.to_word(20010), "بیست هزار و ده")
        self.assertEqual(digits.to_word(10001), "ده هزار و یک")
        self.assertEqual(digits.to_word(500253), "پانصد هزار و دویست و پنجاه و سه")
        self.assertEqual(digits.to_word(6000123), "شش میلیون و یکصد و بیست و سه")
        self.assertEqual(digits.to_word(1000000985), "یک میلیارد و نهصد و هشتاد و پنج")
        self.assertEqual(digits.to_word(100000000000004), "یکصد تریلیون و چهار")

        self.assertEqual(digits.to_word(-305), "منفی سیصد و پنج")
        self.assertEqual(digits.to_word(10.02), "ده و دو صدم")
        self.assertEqual(digits.to_word(15.007), "پانزده و هفت هزارم")
        self.assertEqual(digits.to_word(12519.85), "دوازده هزار و پانصد و نوزده و هشتاد و پنج صدم")
        self.assertEqual(digits.to_word(123.50), "یکصد و بیست و سه و پنج دهم")

        self.assertEqual(
            digits.to_word(-0.1554845), "منفی یک میلیون و پانصد و پنجاه و چهار هزار و هشتصد و چهل و پنج ده میلیونیم"
        )

        with pytest.raises(digits.OutOfRangeException):
            digits.to_word(1000000000000001)
