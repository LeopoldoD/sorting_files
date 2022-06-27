import logging
import os
import heapq

logging.getLogger().setLevel(logging.INFO)


# Helper functions for listing files, creating a directory and deleting files inside a directory

def get_list_of_files(directory_name):
    x = os.listdir(f"./{directory_name}")
    return x


def create_directory(directory_name):
    if os.path.exists(directory_name):
        pass
    else:
        os.makedirs(directory_name)
        logging.info(f"Created directory {directory_name}")


def clean_directory(directory):
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))
        logging.info(f"Removed {f}")


class MyFile:

    def __init__(self):
        self.source_directory = "files/"
        self.temp_directory = "temp/"
        self.buffer_size = 10

    def set_source_directory(self, directory_name):
        self.source_directory = directory_name

    def get_source_directory(self):
        return self.source_directory

    def set_temp_directory(self, directory_name):
        self.temp_directory = directory_name

    def get_temp_directory(self):
        return self.temp_directory

    def set_buffer_size(self, buffer_size):
        self.buffer_size = buffer_size

    def get_buffer_size(self):
        return self.buffer_size

    def prepare_temp_directory(self):
        create_directory("temp")
        clean_directory(self.temp_directory)

    def split_files(self):
        """
        Splits a file into smaller pieces that can be handled in memory
        :param directory: name of the output directory (e.g. temp)
        :return: None
        """
        self.prepare_temp_directory()
        for file in get_list_of_files(self.source_directory):
            fname, ext = file.rsplit('.', 1)
            file_path = self.source_directory + file

            i = 1
            written = False
            with open(file_path) as infile:
                while True:
                    temp_file = "{}_{}.{}".format(fname, i, ext)
                    with open(self.temp_directory + temp_file, 'w') as output_file:
                        for line in (infile.readline() for _ in range(self.buffer_size)):
                            if not line == '':
                                output_file.write(line)
                        written = bool(line)
                    if not written:
                        break
                    i += 1
                    output_file.close()
                infile.close()
        logging.info("Splitted source files")

    def sort(self):
        """
        Triggers the sorting process using min heap data structure
        :return: None
        """
        self.split_files()
        self.min_heap_sort()

    def get_min_heap(self):
        """
        Obtains the smallest heap value among all files by reading the first element of each file
        This works since the first value on eacfile is always the smallest (i.e. monotonically increasing)
        :return: min_heap (int)
        """
        open_files = []
        min_heap = []
        count = 0
        heapq.heapify(min_heap)

        for f in os.listdir(self.temp_directory):
            if os.path.isfile(self.temp_directory + f):
                file = open(self.temp_directory + f)
                open_files.append(file)
                val = file.readline()
                if val is not '':
                    heapq.heappush(min_heap, (int(val), count, file))
                    count += 1
        return min_heap

    def min_heap_sort(self):
        """
        Prints the smallest element among all files, by returning the smallest element on the heap (get_min_heap).
        Then reads the next element on the same file and adds it to the heap data structure.
        Aftetwards, repeats the same process until all elements are sorted.
        :return: None. Prints to standard out
        """
        min_heap = self.get_min_heap()
        while len(min_heap) > 0:
            smallest = heapq.heappop(min_heap)
            print(str(smallest[0]) + ',', end='')
            next_elem = smallest[2].readline()
            if next_elem:
                temp_count = smallest[1]
                heapq.heappush(min_heap, (int(next_elem), temp_count, smallest[2]))
            else:
                smallest[2].close()


if __name__ == '__main__':
    test = MyFile()
    test.sort()
