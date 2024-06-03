import os
import time
import multiprocessing


def process_file(file_path):
    """Function to process each file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        time.sleep(1)
        print(f"Processing {file_path}:\n{content}\n")


def main(directory):
    """Main function to initiate multiprocessing for files in a directory."""
    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Create a pool of workers
    pool = multiprocessing.Pool(processes=5)

    # Process each file in the pool
    pool.map(process_file, files)

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()


if __name__ == "__main__":
    directory = 'files_test'  # Replace with the path to your directory
    start_time = time.time()
    main(directory)
    end_time = time.time()
    print("运行时间：", end_time - start_time)
