from src import *
import argparse
import logging

if __name__ == "__main__":
    # Setting up logging configuration for the script to keep track of the process and potential errors.
    logging.basicConfig(level=logging.INFO,
                        filename='log.txt',
                        filemode='w',
                        encoding='utf-8', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        datefmt="%Y-%m-%d %H:%M")
    
    logging.info("Starting the script.")
    # Parsing command line arguments to get the directory of the file to be read.
    args = parsing_args()
    logging.info(f"Arguments parsed: {args}")
    # Reading the file specified in the command line arguments.

    logging.info("Reading the file...")
    directory = args.directory
    logging.info(f"Directory: {directory}")
    data, dims = read_file(directory)

    # Creating Vertex objects from the data read from the file.
    vertexes = [Vertex(**point) for point in data]

    kruskal_algorithm = Kruskal(vertexes,k=3)
    kruskal_algorithm.define_groups()
    output_groups = kruskal_algorithm.get_groups()

    for group in output_groups:
        print(group)
    
    logging.info(f"Data read successfully. Number of vertexes: {len(data)}, Dimensions: {dims}")

