import os
import yaml

def edit(file_name):
    # Your implementation here
    print(f"Processing {file_name}")
    os.system(f'python edit.py {file_name}')

def main():
    with open("_quarto.yml", "r") as f:
        data = yaml.safe_load(f)
    qmd_files = data["book"]["chapters"] + data["book"]["appendices"]
    for file_name in qmd_files:
        edit(file_name)

if __name__ == "__main__":
    main()

