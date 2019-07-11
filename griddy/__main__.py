from argparse import ArgumentParser
from .LayoutGenerator import LayoutGenerator

def main():
    parser = ArgumentParser()
    parser.add_argument("layout", type = str, help = "The .json file that specifies the layout.")
    parser.add_argument("--colored", action = "store_true", help = "Whether to color the <div> blocks.")
    parser.add_argument("--border", action = "store_true", help = "Whether <div> blocks has borders.")
    parser.add_argument("--show", action = "store_true", help = "Show generated grid in browser.")
    args = parser.parse_args()
    generator = LayoutGenerator(args)
    generator.write()
    if args.show:
        generator.show()
    
if __name__ == "__main__":
    main()