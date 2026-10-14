"""Checks the photo carousel's consent gate, export contracts and rejection paths."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
from render_photo_carousel import ROOT, render

PHOTOS_DIR = ROOT / 'uploads' / 'Europe Batch 3' / 'Post 1'


class PhotoRendererTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.data = {
            'id': 'TEST', 'version': 'v001', 'title': 'Brussels, one waffle at a time',
            'category': 'TOUR', 'consent_status': 'APPROVED',
            'post_caption': 'Day 4 in Brussels. A waffle stop that turned into the highlight of the day.',
            'slides': [
                {'file': '078A1500.jpg', 'caption': ''},
                {'file': '078A1391.jpg', 'label': 'Atomium', 'caption': 'First stop, the Atomium.'},
                {'file': '078A1400.jpg', 'caption': ''},
            ],
        }

    def run_render(self):
        src = self.base / 'input.json'; src.write_text(json.dumps(self.data), encoding='utf-8')
        return render(src, PHOTOS_DIR, self.base / 'out')

    def test_exports_match_contract(self):
        out = self.run_render()
        manifest = json.loads((out / 'manifest.json').read_text())
        self.assertEqual(manifest['status'], 'REVIEW')
        self.assertIsNone(manifest['human_approval'])
        self.assertEqual(manifest['consent_status_declared'], 'APPROVED')
        self.assertEqual(len(PdfReader(next(out.glob('*.pdf'))).pages), 3)
        for name, height in [('instagram_4x5', 1350), ('square_1x1', 1080)]:
            pngs = list((out / name).glob('*.png'))
            self.assertEqual(len(pngs), 3)
            for p in pngs:
                with Image.open(p) as im: self.assertEqual(im.size, (1080, height))
        for rel, digest in manifest['files_sha256'].items():
            self.assertEqual(hashlib.sha256((out / rel).read_bytes()).hexdigest(), digest)
        with self.assertRaisesRegex(ValueError, 'Output exists'): self.run_render()

    def test_consent_unknown_blocks_with_no_output(self):
        self.data['consent_status'] = 'UNKNOWN'
        with self.assertRaisesRegex(ValueError, 'consent_status'): self.run_render()
        self.assertFalse((self.base / 'out').exists())

    def test_consent_denied_blocks_with_no_output(self):
        self.data['consent_status'] = 'DENIED'
        with self.assertRaisesRegex(ValueError, 'consent_status'): self.run_render()
        self.assertFalse((self.base / 'out').exists())

    def test_missing_photo_rejected(self):
        self.data['slides'][0]['file'] = 'does-not-exist.jpg'
        with self.assertRaisesRegex(ValueError, 'photo not found'): self.run_render()

    def test_style_violation_rejected(self):
        self.data['post_caption'] = 'Unlock a remarkable trip!'
        with self.assertRaisesRegex(ValueError, 'prohibited'): self.run_render()

    def test_overlay_word_cap_rejected(self):
        self.data['slides'][1]['caption'] = ' '.join(['word'] * 11)
        with self.assertRaisesRegex(ValueError, 'max 10 words'): self.run_render()

    def test_title_word_cap_rejected(self):
        self.data['title'] = ' '.join(['word'] * 11)
        with self.assertRaisesRegex(ValueError, 'max 10 words'): self.run_render()


if __name__ == '__main__': unittest.main()
