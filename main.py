# -*- coding: utf-8 -*-
import weasyprint
from memory_profiler import profile
import time

@profile()
def create_pdf(file_path: str):
    generate(file_path)
    generate(file_path)
    generate(file_path)
    generate(file_path)
    generate(file_path)
    return True


def generate(file_path: str):
    start_time = time.perf_counter()
    print('start.')

    html_obj = weasyprint.HTML(file_path)
    pdf = html_obj.write_pdf(None)

    end_time = time.perf_counter()
    print(f'finished. {end_time - start_time:.1f} seconds')


if __name__ == '__main__':
    create_pdf('single_byte.html')
    create_pdf('multi_byte.html')
