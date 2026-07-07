import os
import urllib.request
from pathlib import Path

# Tamizhi-ku available-a irukka libraries list
LIBRARIES = {
    "http": {
        "name": "Tamizhi HTTP Web Server",
        "desc": "Native HTTP Server support for Tamizhi",
        "files": [
            {
                "url": "https://raw.githubusercontent.com/BackendDeveloperHub/Tamizhi/main/lib/http.tz",
                "dest": "~/.tamizhi/lib/http.tz"
            },
            {
                "url": "https://raw.githubusercontent.com/BackendDeveloperHub/Tamizhi/main/core/http_runtime.c",
                "dest": "~/.tamizhi/core/http_runtime.c"
            }
        ]
    }
    # Future-la db, math nu pudhu libraries vandha inga add pannikalam
}

def download_file(url, dest_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
        out_file.write(response.read())

def tamizhi_package_manager():
    print("\n📦 Available Tamizhi Libraries:")
    print("-" * 40)
    
    # 1. Available libraries-a list pandrom
    for key, info in LIBRARIES.items():
        print(f" 👉 [{key}] : {info['name']} - {info['desc']}")
    
    print("-" * 40)
    
    # 2. User kitta input vangrom
    choice = input("Enter the library name to install (eg: http) or 'exit': ").strip().lower()
    
    if choice == 'exit':
        print("Cancelled.")
        return
        
    if choice in LIBRARIES:
        print(f"\n⬇️ Installing '{choice}' library...")
        
        # 3. Select panna library-oda files-a download pandrom
        for file_info in LIBRARIES[choice]["files"]:
            dest = Path(file_info["dest"]).expanduser()
            dest.parent.mkdir(parents=True, exist_ok=True) # Folder illana create pannidum
            
            print(f" 📥 Downloading {dest.name}...")
            try:
                download_file(file_info["url"], dest)
                print(f" ✅ Saved to {dest}")
            except Exception as e:
                print(f" ❌ Failed to download {dest.name}: {e}")
                return
                
        print(f"\n🎉 Successfully installed {LIBRARIES[choice]['name']}!")
    else:
        print("❌ Invalid library name. Please try again.")

# bdh-linux command call aagumbodhu idhu run aagum
if __name__ == "__main__":
    tamizhi_package_manager()
