import os

if __name__ == "__main__":
    answer_directory = "Validacao/resultados/"
    result_directory = "resultados/"
    
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

        with open(result_path, "r") as f:
            result = f.readlines()

            for i in range(len(result)):
                result[i] = [int(num) for num in result[i].strip().split(',') if num]

        err_msg = ""
        for r in result:
            if r not in answer:
                err_msg += f"\n\t-> {answer_path} - {result_path}"
        if err_msg:
            raise ValueError(f"Answer does not match, check the file(s): {err_msg}")
            
    print("Everything matched, congratulations, you've finished the assignment!!")