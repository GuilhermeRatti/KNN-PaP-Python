import argparse

def read_file(directory:str) -> tuple:
    """
    Reads a file and returns its contents as a list of lines.
    
    Args:
        directory (str): The path to the file to be read.
        
    Returns:
        tuple: A tuple containing:
            - points (list): A list of dictionaries, each containing an id and coordinates.
            - dimensions (int): The number of dimensions of the coordinates.
    """
    
    points = []
    id = 1
    with open(directory, 'r') as file:
        for line in file:
            print(line.strip())
            coordinates = [float(num) for num in line.strip().split(',')]
            points.append({"id": id, "coordinates": coordinates})
            id+=1
    
    dimensions = len(points[0]['coordinates'])
    
    return points, dimensions

def parsing_args() -> argparse.Namespace:
    
    """
    Parses command line arguments.
    
    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('directory', type=str, help='Directory of the file to be read')
    
    args = parser.parse_args()
    
    return args

