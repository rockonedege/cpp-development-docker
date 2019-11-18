from pathlib import Path
import subprocess
import re


this_folder = Path(__file__).absolute().parent
workspace = this_folder.parent


def run(image):
    compiler = re.sub(r'(^.+/)|(:+.$)', '', image)
    cmd = f'''docker run -it --name {compiler} \
-v {workspace}:/workspace \
-v {this_folder}:/scripts \
{image}:latest  \
/bin/bash "/scripts/init.sh"
'''
    print(cmd)
    subprocess.run(cmd, shell=True)


def main(use_local):
    import concurrent.futures

    # locally built images
    local_images = ['local/gcc9', 'local/clang9']  
    # pre-built images on docker hub
    remote_images = ['tomgee/cpp-dev-gcc', 'tomgee/cpp-dev-clang']

    images = local_images if use_local else remote_images

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(run, images)

    print(
        f'''done with {images}: 
    {workspace} ==> /workspace
    {this_folder} ==> /scripts
''')


if __name__ == "__main__":
    main(use_local=True)
