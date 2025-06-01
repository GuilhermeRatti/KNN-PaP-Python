from src import *
import logging
import sys
import argparse


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
    if len(sys.argv) > 2:
        args = parsing_args()
    else:
        dir = input("Enter the directory of the file to be read: ")
        k  = int(input("Enter the number of clusters (k): "))
        output = input("Enter the output file name (optional, press Enter to skip and console will be used): ")

        args = argparse.Namespace(directory=dir, k=k, output=output if output else None)

    logging.info(f"Arguments parsed: {args}")
    # Reading the file specified in the command line arguments.

    logging.info("Reading the file...")
    directory = args.directory
    klusters = args.k
    logging.info(f"Directory: {directory}")
    data, dims = read_file(directory)
    logging.info(f"Data read successfully. Number of vertexes: {len(data)}, Dimensions: {dims}")

    logging.info("Creating Vertex objects...")
    # Creating Vertex objects from the data read from the file.
    vertexes = [Vertex(**point) for point in data]


    logging.info(f"Vertex objects created: {len(vertexes)}")
    # Initializing the KNN algorithm with the vertexes and the number of clusters (k).

    logging.info(f"Initializing KNN algorithm with k={klusters}...")
    knn_algorithm = KNN(vertexes,k=klusters)

    # Defining the groups using the KNN algorithm.
    logging.info("Defining groups using KNN algorithm...")
    knn_algorithm.define_groups()

    logging.info("Groups defined successfully.")
    # Getting the output groups from the KNN algorithm.
    logging.info("Getting output groups...")
    output_groups = knn_algorithm.get_groups()
    logging.info("Output groups obtained successfully.")

    logging.info("Writing results to file...")

    # If an output file name is provided, write the results to that file.
    if 'output' in args and args.output:
        output_file = args.output
   
        with open(output_file,"w") as f:
            for group in output_groups:
                # Writing each group to the file, converting each element to string and joining them with commas.
                f.write(", ".join(str(i) for i in group))
                # Adding a newline after each group.
                f.write("\n")
    else:
        # If no output file name is provided, print the results to the console.
        for group in output_groups:
            print(", ".join(str(i) for i in group))

    

