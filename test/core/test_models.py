import pathlib
import unittest
import shutil
import importlib

from app.core import constraints, models


class ModelTestBase(unittest.TestCase):
    def setUp(self) -> None:
        shutil.rmtree(constraints.DATA_FOLDER)
        importlib.reload(constraints)  # creatate necessary folders
        (constraints.DATA_FOLDER / '.gitkeep').touch()

    def assertMetaContent(self, path, value: list):
        meta = pathlib.Path(path).read_text().strip().splitlines()
        self.assertListEqual(meta, value)


class TestBaseFunctions(ModelTestBase):
    def test_list_jobs(self):
        # arrange
        for i in range(1, 6):
            models.Job(str(i), client_name=f'Client {i}', client_address=f'{i}00 St')

        # act

        # assert
        jobs = list(models.iter_jobs())
        self.assertEqual(len(jobs), 5)
        self.assertEqual(jobs[0].client_name, 'Client 1')
        self.assertEqual(jobs[0].client_address, '100 St')


class TestJob(ModelTestBase):
    def test_set_meta_data(self):
        j = models.Job('1')

        j.client_name = 'A client'
        j.client_address = 'An address'

        self.assertEqual(j.client_name, 'A client')
        self.assertEqual(j.client_address, 'An address')
        self.assertMetaContent('data/jobs/1/meta.ini', [
            '[DEFAULT]',
            'client_name = A client',
            'client_address = An address'
        ])

        del j.client_address

        self.assertEqual(j.client_address, None)
        self.assertMetaContent('data/jobs/1/meta.ini', [
            '[DEFAULT]',
            'client_name = A client',
        ])

    def test_modify_equipments(self):
        j = models.Job('1')

        # add
        j.add_equipment('AAA', '123')
        # iter

        self.assertTrue('AAA_123' in j)
        self.assertEqual(len(j), 1)

        e = j['AAA_123']


if __name__ == '__main__':
    unittest.main()
