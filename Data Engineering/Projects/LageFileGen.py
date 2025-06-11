# import os
# import time

# GB1 = 1024*1024*1024  # 1GB
# size = 1 # 1 GB for testing
# filename = 'test_file'

# if os.path.exists(filename):
#     print(f"Error: {filename} already exists.")
#     exit(1)

# try:
#     start_time = time.time()
#     with open(filename, 'wb') as fout:
#         for i in range(size):
#             fout.write(os.urandom(GB1))
#     end_time = time.time()
#     print(f"Created {filename} of size {size} GB in {end_time - start_time:.2f} seconds")
# except OSError as e:
#     print(f"Error: {e}")


# import os
# import time
# GB1 = 1024*1024*1024
# Size = 1
# filename = 'test_file'
# if os.path.exists(filename):
#     print(f"Error:{filename} already exists.")
# try:
#     start_time = time.time()
#     with open(filename,'wb') as fout:
#         for i in range(size):
#             fout.write(os.urandom(GB1))
#         end_time = time.time()
#         print(f"Created {filename} of size {size} GB in {end_time-start_time:.2f} seconds")
# except OSError as e:
#     print(f"Error: {e}")




# import os
# import time

# GB1 = 1024*1024*1024  # 1GB
# size = 1  # 1 GB for testing
# filename = 'test_file.txt'

# if os.path.exists(filename):
#     print(f"Error: {filename} already exists.")
#     exit(1)

# try:
#     start_time = time.time()
#     with open(filename, 'w') as fout:
#         chunk = "A" * 1024 * 1024  # 1 MB of 'A' characters
#         for i in range(1024):  # 1024 MB = 1 GB
#             fout.write(chunk)
#     end_time = time.time()
#     print(f"Created {filename} of size {size} GB in {end_time - start_time:.2f} seconds")
# except OSError as e:
#     print(f"Error: {e}")









# Creates a 50 GB file instantly (sparse file)
GB1 = 1024 * 1024 * 1024  # 1 GB
size = 100  # GB
filename = 'test_file'

with open(filename, 'wb') as fout:
    fout.seek(size * GB1 - 1)
    fout.write(b'\0')

print(f"Created {filename} of size {size} GB instantly (sparse file)")
