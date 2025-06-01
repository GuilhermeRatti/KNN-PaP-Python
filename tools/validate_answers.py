import os

if __name__ == "__main__":
    answer_directory = input("Enter the directory of the answers: ")
    result_directory = input("Enter the directory of the assignment script's results to be validated: ")

    assert os.path.exists(answer_directory), f"Answer directory {answer_directory} does not exist!"
    assert os.path.exists(result_directory), f"Result directory {result_directory} does not exist!"
    
    if not answer_directory.endswith('/'):
        answer_directory += '/'
    if not result_directory.endswith('/'):
        result_directory += '/'

    for file in os.listdir(answer_directory):
        answer_path = answer_directory + file
        result_path = result_directory + file

        with open(answer_path, "r") as f:
            answer = f.readlines()

            for i in range(len(answer)):
                answer[i] = [int(num) for num in answer[i].strip().split(',') if num]

            answer = [a for a in answer if a]
            
            for a in answer:
                a.sort()
            answer.sort()
        try:
            with open(result_path, "r") as f:
                result = f.readlines()

                for i in range(len(result)):
                    result[i] = [int(num) for num in result[i].strip().split(',') if num]
        except FileNotFoundError:
            raise FileNotFoundError(f"Result file {result_path} not found, please run all assignment tests first and name the results exactly like the input in the results directory!")

        err_msg = ""
        for r in result:
            if r not in answer:
                err_msg += f"\n\t-> {answer_path} - {result_path}"
        if err_msg:
            raise ValueError(f"Answer does not match, check the file(s): {err_msg}")
            
    print("Everything matched, congratulations, you've finished the assignment!!")