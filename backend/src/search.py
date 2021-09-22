import uuid
import pathlib
import pandas as pd
from src.utils import cfg


class SearchJob(object):

    def __init__(self, tmp_folder: str = cfg['tmp_dir']):
        self.method = ''
        self.input = ''
        self.command = ''
        self.job_id = ''
        self.local_tmp = pathlib.Path('')
        self.base_local_tmp = tmp_folder
        self.available_methods = ['text', 'mmseqs', 'hmmer']
        self.available_commands = dict(
            text='sqlite query ',
            mmseqs='',
            hmmer=''
        )

    def init(self, method: str, input: str):
        self.method = method
        self.input = input
        self.command = self.available_commands[method]
        self.job_id = self.__gen_job_id()
        self.local_tmp = self.__create_local_tmp()

    def run(self):
        if self.method == 'text':
            pass
            # run sql query
        else:
            pass
            # run self.subprocess to execute the query

    def result_file(self):
        return self.local_tmp.joinpath('result.txt')

    def result_page(self, page_size: int, page: int):
        pass
        # TODO add detail here./

    def __gen_job_id(self):
        return self.method + '.' + str(uuid.uuid4())

    def __create_local_tmp(self):
        local_tmp = pathlib.Path(self.base_local_tmp).joinpath(self.job_id)
        if not local_tmp.exists() or not local_tmp.is_dir():
            local_tmp.mkdir()
        return local_tmp
