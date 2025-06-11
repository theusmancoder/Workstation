# import os
# import shutil
# from concurrent.futures import ThreadPoolExecutor
# from tqdm import tqdm

# # ✅ Auto Configuration
# SOURCE_DIR = r"G:\New folder"
# DEST_DIR = r"E:\test"
# MAX_THREADS = min(8, os.cpu_count() or 4)  # Auto-detect safe max

# def is_same_file(src, dst):
#     try:
#         return (
#             os.path.getsize(src) == os.path.getsize(dst) and
#             int(os.path.getmtime(src)) == int(os.path.getmtime(dst))
#         )
#     except:
#         return False

# def copy_file(src_path, dest_path):
#     try:
#         os.makedirs(os.path.dirname(dest_path), exist_ok=True)
#         if not os.path.exists(dest_path) or not is_same_file(src_path, dest_path):
#             shutil.copy2(src_path, dest_path)
#             print(f"✅ Copied: {src_path} → {dest_path}")
#         else:
#             print(f"⏭️ Skipped (same file): {dest_path}")
#     except Exception as e:
#         print(f"❌ Error copying {src_path}: {e}")

# def transfer_all_files(source_dir, dest_dir):
#     files_to_copy = []

#     for root, dirs, files in os.walk(source_dir):
#         for file in files:
#             src_file = os.path.join(root, file)
#             relative_path = os.path.relpath(src_file, source_dir)
#             dest_file = os.path.join(dest_dir, relative_path)
#             files_to_copy.append((src_file, dest_file))

#     print(f"🔍 Total files to copy: {len(files_to_copy)}\n")

#     with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
#         for src, dest in tqdm(files_to_copy, desc="🔄 Copying Files", unit="file"):
#             executor.submit(copy_file, src, dest)

#     print("✅ All files transferred successfully.")

# # Run the function
# if __name__ == "__main__":
#     transfer_all_files(SOURCE_DIR, DEST_DIR)









# import subprocess

# SOURCE_DIR = r"G:\New folder"
# DEST_DIR = r"E:\test"

# def fast_copy_with_robocopy(src, dst):
#     command = [
#         "robocopy",
#         src,
#         dst,
#         "/E",        # Copy subdirectories, including empty ones
#         "/Z",        # Restartable mode
#         "/MT:8",     # Multithreaded copy (adjustable, max 128)
#         "/R:2",      # Retry 2 times
#         "/W:2"       # Wait 2 seconds between retries
#     ]

#     print("🚀 Starting robocopy transfer...\n")
#     result = subprocess.run(command, shell=True, text=True)
#     print("\n✅ Transfer finished with robocopy.")

# if __name__ == "__main__":
#     fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)












# import subprocess
# import os

# SOURCE_DIR = r"G:\New folder"
# DEST_DIR = r"E:\test"

# def fast_copy_with_robocopy(src, dst):
#     # Validate source and destination paths
#     if not os.path.exists(src):
#         print(f"❌ Error: Source directory '{src}' does not exist.")
#         return
#     if not os.path.exists(dst):
#         print(f"ℹ️ Destination directory '{dst}' does not exist. Creating it...")
#         os.makedirs(dst)

#     command = [
#         "robocopy",
#         src,
#         dst,
#         "/E",        # Copy subdirectories, including empty ones
#         "/Z",        # Restartable mode
#         "/MT:16",    # Multithreaded copy (increased to 16 threads)
#         "/R:2",      # Retry 2 times
#         "/W:2",      # Wait 2 seconds between retries
#         "/LOG+:robocopy_log.txt"  # Append log to file
#     ]

#     print(f"🚀 Starting robocopy transfer from '{src}' to '{dst}'...\n")
#     try:
#         result = subprocess.run(
#             command,
#             capture_output=True,  # Capture stdout and stderr
#             text=True,           # Return output as strings
#             shell=False          # Avoid shell=True for safety
#         )

#         # Print robocopy output
#         print("📜 Robocopy Output:")
#         print(result.stdout)
#         if result.stderr:
#             print("⚠️ Robocopy Errors/Warnings:")
#             print(result.stderr)

#         # Check robocopy exit code
#         if result.returncode <= 1:
#             print("\n✅ Transfer completed successfully.")
#         elif result.returncode <= 3:
#             print("\n⚠️ Transfer completed with some differences (extra files or directories).")
#         else:
#             print(f"\n❌ Transfer failed with exit code {result.returncode}. Check robocopy_log.txt for details.")
#     except subprocess.SubprocessError as e:
#         print(f"\n❌ Error executing robocopy: {e}")

# if __name__ == "__main__":
#     fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)








# import subprocess
# import os

# SOURCE_DIR = r"G:\New folder"
# DEST_DIR = r"E:\test"

# def fast_copy_with_robocopy(src, dst):
#     # Validate source and destination paths
#     if not os.path.exists(src):
#         print(f"❌ Error: Source directory '{src}' does not exist.")
#         return
#     if not os.path.exists(dst):
#         print(f"ℹ️ Destination directory '{dst}' does not exist. Creating it...")
#         os.makedirs(dst)

#     command = [
#         "robocopy",
#         src,
#         dst,
#         "/E",        # Copy subdirectories, including empty ones
#         "/Z",        # Restartable mode
#         "/J",        # Unbuffered I/O for large files
#         "/XJ",       # Exclude junction points
#         "/MT:32",    # Multithreaded copy (increased to 32 threads)
#         "/R:2",      # Retry 2 times
#         "/W:2",      # Wait 2 seconds between retries
#         "/NFL",      # No file list (reduces output)
#         "/NDL",      # No directory list (reduces output)
#         "/NOOFFLOAD" # Disable copy offloading
#     ]

#     print(f"🚀 Starting optimized robocopy transfer from '{src}' to '{dst}'...\n")
#     try:
#         result = subprocess.run(
#             command,
#             capture_output=True,  # Capture stdout and stderr
#             text=True,           # Return output as strings
#             shell=False          # Avoid shell=True for safety
#         )

#         # Print minimal robocopy output
#         print("📜 Robocopy Output:")
#         print(result.stdout)
#         if result.stderr:
#             print("⚠️ Robocopy Errors/Warnings:")
#             print(result.stderr)

#         # Check robocopy exit code
#         if result.returncode <= 1:
#             print("\n✅ Transfer completed successfully.")
#         elif result.returncode <= 3:
#             print("\n⚠️ Transfer completed with some differences (extra files or directories).")
#         else:
#             print(f"\n❌ Transfer failed with exit code {result.returncode}.")
#     except subprocess.SubprocessError as e:
#         print(f"\n❌ Error executing robocopy: {e}")

# if __name__ == "__main__":
#     fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)











# import subprocess
# import os

# SOURCE_DIR = r"G:\New folder"
# DEST_DIR = r"E:\test"

# def fast_copy_with_robocopy(src, dst):
#     # Validate source and destination paths
#     if not os.path.exists(src):
#         print(f"❌ Error: Source directory '{src}' does not exist.")
#         return
#     if not os.path.isdir(src):
#         print(f"❌ Error: Source '{src}' is not a directory.")
#         return
#     if not os.path.exists(dst):
#         print(f"ℹ️ Destination directory '{dst}' does not exist. Creating it...")
#         os.makedirs(dst, exist_ok=True)

#     command = [
#         "robocopy",
#         src,
#         dst,
#         "/E",        # Copy subdirectories, including empty ones
#         "/Z",        # Restartable mode
#         "/J",        # Unbuffered I/O for large files
#         "/XJ",       # Exclude junction points
#         "/MT:32",    # Multithreaded copy (32 threads)
#         "/R:2",      # Retry 2 times
#         "/W:2",      # Wait 2 seconds between retries
#         "/NFL",      # No file list
#         "/NDL",      # No directory list
#         "/NOOFFLOAD", # Disable copy offloading
#         "/LOG+:robocopy_log.txt"  # Append log to file for debugging
#     ]

#     print(f"🚀 Starting optimized robocopy transfer from '{src}' to '{dst}'...\n")
#     try:
#         result = subprocess.run(
#             command,
#             capture_output=True,
#             text=True,
#             shell=False
#         )

#         # Print minimal robocopy output
#         print("📜 Robocopy Output:")
#         print(result.stdout)
#         if result.stderr:
#             print("⚠️ Robocopy Errors/Warnings:")
#             print(result.stderr)

#         # Interpret robocopy exit codes
#         if result.returncode == 0:
#             print("\n✅ Transfer completed successfully (no files copied, identical directories).")
#         elif result.returncode == 1:
#             print("\n✅ Transfer completed successfully (files copied).")
#         elif result.returncode <= 3:
#             print("\n⚠️ Transfer completed with some differences (extra files or directories).")
#         else:
#             print(f"\n❌ Transfer failed with exit code {result.returncode}. Check robocopy_log.txt for details.")
#     except subprocess.SubprocessError as e:
#         print(f"\n❌ Error executing robocopy: {e}")
#     except PermissionError:
#         print(f"\n❌ Permission error: Check access rights for '{src}' or '{dst}'.")
#     except OSError as e:
#         print(f"\n❌ OS error: {e} (e.g., disk full or invalid path).")

# if __name__ == "__main__":
#     fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)












import subprocess
import os
from datetime import datetime

# ✅ Configuration
SOURCE_DIR = r"G:\New folder"
DEST_DIR = r"E:\test"

# ✅ Automatically adjust thread count (safe limit)
MAX_THREADS = min(32, os.cpu_count() or 4)

# ✅ Create timestamped log file
log_filename = f"robocopy_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def fast_copy_with_robocopy(src, dst):
    # Check source
    if not os.path.exists(src):
        print(f"❌ Error: Source directory '{src}' does not exist.")
        return
    if not os.path.isdir(src):
        print(f"❌ Error: Source '{src}' is not a directory.")
        return

    # Create destination if missing
    if not os.path.exists(dst):
        print(f"ℹ️ Destination '{dst}' does not exist. Creating it...")
        os.makedirs(dst, exist_ok=True)

    # 🧠 Robocopy command
    command = [
        "robocopy",
        src,
        dst,
        "/E",          # Include subdirectories
        "/Z",          # Restartable mode
        "/J",          # Unbuffered I/O
        "/XJ",         # Exclude junctions
        f"/MT:{MAX_THREADS}",  # Multithreading
        "/R:2",        # Retry count
        "/W:2",        # Wait between retries
        "/NFL",        # No file list
        "/NDL",        # No dir list
        "/NOOFFLOAD",  # Disable hardware copy offloading
        f"/LOG+:{log_filename}"  # Append logs
    ]

    print(f"\n🚀 Starting optimized transfer with {MAX_THREADS} threads...\n")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )

        print("📄 Robocopy Output:\n")
        print(result.stdout.strip())

        if result.stderr.strip():
            print("⚠️ Errors/Warnings:\n")
            print(result.stderr.strip())

        # ✅ Interpret robocopy exit codes
        code = result.returncode
        if code == 0:
            print("\n✅ No files copied — source and destination are identical.")
        elif code == 1:
            print("\n✅ Files copied successfully.")
        elif code <= 3:
            print("\n⚠️ Minor issues (e.g., extra files or mismatched attributes), but copy mostly successful.")
        else:
            print(f"\n❌ Transfer failed with exit code {code}. Check log: {log_filename}")

    except subprocess.SubprocessError as e:
        print(f"\n❌ Subprocess error: {e}")
    except PermissionError:
        print(f"\n❌ Permission denied: Check access to '{src}' or '{dst}'.")
    except OSError as e:
        print(f"\n❌ OS error: {e} (maybe disk full, bad path, or hardware issue)")

if __name__ == "__main__":
    fast_copy_with_robocopy(SOURCE_DIR, DEST_DIR)
