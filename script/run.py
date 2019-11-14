import re
from pathlib import Path

PWD = Path(__file__).absolute().parent
RELEASE = PWD.parent / 'release'


def get_name_from_tag(image_base):
    stem = re.sub(r'[:/]', '-', image_base)
    return stem + '.Dockerfile'


def make_dockerfile(image_base):
    snippet = PWD / 'snippet.Dockerfile'

    to = RELEASE / get_name_from_tag(image_base)
    to.write_text('\n'.join([f'FROM {image_base}', snippet.read_text()]))


def make_dockerfiles(image_bases):
    for image_base in image_bases:
        filename = get_name_from_tag(image_base)
        make_dockerfile(image_base)
        print(f'Done: {image_base} => {filename}.')


def make_build_scripts(image_bases):
    lines = []
    for i in image_bases:
        tag = 'ttan/' + i.split('/', 1)[-1]
        name = get_name_from_tag(i)
        lines.append(f'docker build --rm --tag {tag} -f "{name}" .')

    to = RELEASE / 'build.bat'
    to.write_text('\n'.join(lines))
    print(f'Done: docker build script => {to}.')


def main():
    image_bases = ['conanio/gcc9', 'conanio/clang9']

    make_dockerfiles(image_bases)
    make_build_scripts(image_bases)


if __name__ == "__main__":
    main()
