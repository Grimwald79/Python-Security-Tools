import hashlib
import os

def calculate_sha256(filepath):
    """
    Reads a file in chunks and generates a SHA-256 hash.
    Using chunks prevents memory crashes on large files.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filepath, "rb") as f:
            # Read 4KB chunks
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def check_integrity():
    print("--- File Integrity Monitor (SHA-256) ---")
    file_path = input("Enter the path of the file to check: ")
    
    if os.path.exists(file_path):
        file_hash = calculate_sha256(file_path)
        print(f"\n[+] File: {file_path}")
        print(f"[+] SHA-256 Hash: {file_hash}")
    else:
        print("\n[!] Error: File not found.")

if __name__ == "__main__":
    check_integrity()
