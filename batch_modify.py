from pathlib import Path
import re


def modify_title():
    sourec_dir = "./source/_posts"

    for path in Path(sourec_dir).glob("*.md"):
        # if path.stem == 'oracle-join':
        #     # text = path.read_text(encoding="utf-8")
        #     # text = 'title: oracle join'
        #     # text = re.sub('title: (.*?)', 'title: ' + '\1'.upper(), text)
        #     # print(text)

        temp_path = Path(str(path) + '.temp')

        with open(path, encoding='utf-8') as fr, open(temp_path, 'w', encoding="utf-8") as fw:
            for line in fr.readlines():
                if line.startswith('title: ') and line.islower():
                    fw.write(
                        f'title: {line.replace("title: ", "").title()}')
                # elif line.startswith('tag: '):
                #     fw.write(line)
                #     fw.write(line.replace('tags', 'categories'))
                else:
                    fw.write(line)

        path.unlink()
        temp_path.rename(path)

        print(f"update {str(path)} title success!")


def modify_date():
    sourec_dir = "./source/_posts"

    for path in Path(sourec_dir).glob("*.md"):
        temp_path = Path(str(path) + '.temp')
        if path.read_text(encoding="utf-8").find("date: ") == -1:
            with open(path, encoding='utf-8') as fr, open(temp_path, 'w', encoding="utf-8") as fw:
                for line in fr.readlines():
                    if line.startswith('tags: '):
                        fw.write(line)
                        fw.write("date: 2019-04-30\n")
                    else:
                        fw.write(line)

            path.unlink()
            temp_path.rename(path)

            print(f"update {str(path)} title success!")


if __name__ == "__main__":
    modify_date()
