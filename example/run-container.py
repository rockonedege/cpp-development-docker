from pathlib import Path
import subprocess
import re


this_folder = Path(__file__).absolute().parent


def make_commands(images, workspace):
    def compiler(x): return re.sub(r'(^.+/)|(:+.$)', '', x)
    return [f'''docker run -it --name {compiler(image)} \
-v {workspace}:/workspace \
-v {this_folder}:/scripts \
{image}:latest  \
/bin/bash "/scripts/init.sh"
''' for image in images]


def run_one(cmd):
    print(cmd)
    subprocess.run(cmd, shell=True)


def main(use_local, workspace):
    import concurrent.futures

        # locally built images
    local_images = ['local/gcc9', 'local/clang9']
    # pre-built images on docker hub
    remote_images = ['tomgee/cpp-dev-gcc', 'tomgee/cpp-dev-clang']
    images = local_images if use_local else remote_images

    commands = make_commands(images, workspace)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(run_one, commands)

    print(
        f'''done with {images}:
    {workspace} ==> /workspace
    {this_folder} ==> /scripts
''')


if __name__ == "__main__":

    default_workspace = this_folder.parent
    main(use_local=False, workspace='default_workspace')
