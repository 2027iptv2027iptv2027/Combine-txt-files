import requests
from datetime import datetime
import os

# ===== CONFIGURATION =====
# List your text file URLs here
FILES = [
    "https://raw.githubusercontent.com/user/repo/main/file1.txt",
    "https://raw.githubusercontent.com/user/repo/main/file2.txt",
    "https://raw.githubusercontent.com/user/repo/main/file3.txt",
    # Add more text file URLs here
]

# Output file name
OUTPUT_FILE = "combined_files.txt"

# ===== FUNCTIONS =====
def get_source_name(url):
    """Extract file name from URL or path"""
    return os.path.basename(url) or "Unnamed_Source.txt"

def fetch_text_file(url):
    """Fetch plain text content from a given URL"""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None

def process_file(content, source_name, outfile):
    """Appends file content with clear section headers"""
    outfile.write(f"# {'=' * 50}\n")
    outfile.write(f"# Source: {source_name}\n")
    outfile.write(f"# {'=' * 50}\n\n")
    
    # Write the main body of the file
    outfile.write(content.strip() + "\n\n\n")

def main():
    """Main function to combine text files"""
    print(f"🚀 Starting to combine {len(FILES)} text files...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        # Write header metadata
        outfile.write(f"# Combined Text Document\n")
        outfile.write(f"# Generated on {datetime.utcnow().isoformat()} UTC\n\n")
        
        # Process each URL
        for url in FILES:
            print(f"🔄 Fetching: {url}")
            content = fetch_text_file(url)
            
            if content is not None:
                source_name = get_source_name(url)
                process_file(content, source_name, outfile)
                print(f"✅ Added: {source_name}")
    
    print(f"\n🎉 Success! All text files combined into '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
