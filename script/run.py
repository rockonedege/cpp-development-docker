import re
from pathlib import Path

PWD = Path(__file__).absolute().parent
RELEASE = PWD.parent / 'release'


def get_name_from_tag(image_base):
    stem =  re.sub(r'[:/]', '-', image_base)
    return stem + '.Dockerfile'


def run(image_base):
    snippet = PWD / 'snippet.Dockerfile'

    to = RELEASE / get_name_from_tag(image_base)
    to.write_text('\n'.join([f'FROM {image_base}', snippet.read_text()]))


def main():
    for image_base in ['conanio/gcc9', 'conanio/clang9']:
        run(image_base)
        print(f'Done: {image_base} => {get_name_from_tag(image_base)}.')


if __name__ == "__main__":
    main()
