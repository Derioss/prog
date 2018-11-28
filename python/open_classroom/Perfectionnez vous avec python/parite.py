
import analysis.csv as c_an
import analysis.xml as x_an
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of information about the members of parliament""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    #import pdb; pdb.set_trace() # debug
    if args.extension == 'xml':
        x_an.launch_analysis(args.datafile)
    elif args.extension == 'csv':
        c_an.launch_analysis(args.datafile)
    else:
        print("launch parity.py with -e or --extension and xml or csv")


if __name__ == "__main__":
  main()