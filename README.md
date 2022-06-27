# file-sorting

Purpose is to create a small utility that sorts files containing monotonically increasing numbers.
The application assumes that the elements in all files cannot be stored in memory at the same time. For this reason, the application divides each file according to a maximum buffer size. The application workflow is the following:
1. Divides each file based on a buffer size (by default set to 10) and writes partitioned files to a temporary directory. The buffer size value can be updated by running the appropiate set method (set_buffer_size).
2. Creates a heap with the first element of each file and obtains the minimum value among them. Given that the value inside the files are monotonically increasing, this means that the smallest element among all files (including temporary) would always be the first element of one of the temporary files.
3. After the smallest value in all partitioned files is determined, it is printed to standard output and removed from the heap.
4. Then the next value in the same file as the smallest value is read and added to the heap.
5. The minimum value in the heap is again printed to standard output and removed from the data structure until all values among all files are exhausted and the heap is empty.

Notes:
- Since the task description assumes 10 files are provided, it is considered that the memory would be able to hold at least 10 elements at a time. 
- Uses heapq python package to manage the heap data structure.

## Getting started

Run the python program python sort_files.py

There are some sample files in the "files" directory. Replace the source files as appropiate. If required, change the directory name with the set method "set_source_directory".

