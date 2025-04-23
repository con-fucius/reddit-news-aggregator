import os
import sys
import importlib.util
import types

def find_adk_package_path():
    """Find the path to the installed ADK package."""
    try:
        import google.adk
        return os.path.dirname(google.adk.__file__)
    except ImportError:
        return None

def main():
    adk_path = find_adk_package_path()
    if not adk_path:
        print("❌ ADK package not found. Make sure your virtual environment is activated.")
        return False
    
    logs_path = os.path.join(adk_path, 'cli', 'utils', 'logs.py')
    if not os.path.exists(logs_path):
        print(f"❌ Logs module not found at expected path: {logs_path}")
        return False
    
    # Restore the original file from backup if it exists
    backup_path = logs_path + '.bak'
    if os.path.exists(backup_path):
        try:
            with open(backup_path, 'r') as src:
                original_content = src.read()
            with open(logs_path, 'w') as dst:
                dst.write(original_content)
            print("✅ Restored original file from backup")
        except Exception as e:
            print(f"❌ Error restoring backup: {str(e)}")
            return False
    
    # Read the current file
    try:
        with open(logs_path, 'r') as src:
            content = src.read()
            
        # Create backup if it doesn't exist
        if not os.path.exists(backup_path):
            with open(backup_path, 'w') as dst:
                dst.write(content)
                print(f"✅ Created backup at {backup_path}")
        
        # Find and replace the symlink line with proper indentation
        lines = content.splitlines()
        modified_lines = []
        found = False
        
        for line in lines:
            if "os.symlink(log_filepath, latest_log_link)" in line:
                # Get the indentation from the original line
                indent = line[:line.find("os.symlink")]
                modified_lines.append(f"{indent}try:")
                modified_lines.append(f"{indent}    os.symlink(log_filepath, latest_log_link)")
                modified_lines.append(f"{indent}except (OSError, PermissionError):")
                modified_lines.append(f"{indent}    # Skip symlink creation on Windows when permissions are insufficient")
                modified_lines.append(f"{indent}    pass")
                found = True
            else:
                modified_lines.append(line)
        
        if found:
            modified_content = "\n".join(modified_lines)
            with open(logs_path, 'w') as f:
                f.write(modified_content)
                
            print("✅ Successfully patched ADK logs module to fix symlink issue")
            print("You can now run your agent with: adk run agents/reddit_scout")
            return True
        else:
            print("⚠️ Could not find the symlink code in the logs module. It may have been updated.")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
