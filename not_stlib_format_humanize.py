import humanize
# https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size

# KiB, Kib, KB, Kb
# https://habr.com/ru/articles/193256/
# Для обозначения степеней двойки в ближайшей приставке СИ второй слог заменяется на «bi» от binary (двоичный):
# kibibyte — KiB, mebibyte — MiB, gibibyte — GiB.
# kibibyte KiB 1024 byte
# kilobyte KB 1000 byte
# kilobit  Kb 1000 bit

disk_sizes_list = [1, 100, 999, 1000,1024, 2000,2048, 3000, 9999, 10000, 2048000000, 9990000000, 9000000000000000000000]
for size in disk_sizes_list:
    natural_size = humanize.naturalsize(size)
    binary_size = humanize.naturalsize(size, binary=True)
    print(f" {natural_size} \t| {binary_size}\t|{size}")