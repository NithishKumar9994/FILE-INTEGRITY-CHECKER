import os
import hashlib
import json
from datetime import datetime

HASH_DB = "hashes.json"

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def load_hash_database():
    """Load saved hash values from the database file."""
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as db:
        return json.load(db)

def save_hash_database(data):
    """Save hash values to the database file."""
    with open(HASH_DB, "w") as db:
        json.dump(data, db, indent=4)

def scan_directory(target_dir):
    """Recursively scan directory and calculate hash values."""
    file_hashes = {}
    for root, _, files in os.walk(target_dir):
        for file in files:
            full_path = os.path.join(root, file)
            hash_value = calculate_hash(full_path)
            if hash_value:
                file_hashes[full_path] = hash_value
    return file_hashes

def compare_hashes(old_hashes, new_hashes):
    """Compare stored hashes with current ones."""
    modified = []
    deleted = []
    new = []

    # Check for modified or deleted
    for path in old_hashes:
        if path not in new_hashes:
            deleted.append(path)
        elif old_hashes[path] != new_hashes[path]:
            modified.append(path)

    # Check for new files
    for path in new_hashes:
        if path not in old_hashes:
            new.append(path)

    return modified, deleted, new

def main():
    target_directory = input("Enter directory to monitor: ").strip()
    print(f"[{datetime.now()}] Scanning '{target_directory}'...")

    new_hashes = scan_directory(target_directory)
    old_hashes = load_hash_database()

    modified, deleted, new = compare_hashes(old_hashes, new_hashes)

    print("\n📊 Integrity Check Report:")
    if modified:
        print(f"\n⚠️ Modified Files ({len(modified)}):")
        for file in modified:
            print(f" - {file}")
    if deleted:
        print(f"\n🗑️ Deleted Files ({len(deleted)}):")
        for file in deleted:
            print(f" - {file}")
    if new:
        print(f"\n🆕 New Files ({len(new)}):")
        for file in new:
            print(f" - {file}")
    if not (modified or deleted or new):
        print("✅ No changes detected.")

    # Save current state
    save_hash_database(new_hashes)
    print("\n🔒 Hash database updated.")

if __name__ == "__main__":
    main()
