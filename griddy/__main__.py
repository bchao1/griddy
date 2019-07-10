from argparse import ArgumentParser
from .LayoutGenerator import LayoutGenerator

def main():
    parser = ArgumentParser()
    parser.add_argument("layout", type = str, help = "The .json file that specifies the layout.")
    parser.add_argument("--no-color", action = "store_true", help = "Whether to color the <div> blocks.")
    args = parser.parse_args()
    generator = LayoutGenerator(args)
    generator.write()
    
if __name__ == "__main__":
    main()