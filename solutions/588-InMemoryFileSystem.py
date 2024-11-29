from typing import List

class FileNode:
    def __init__(self):
        self.is_file = False
        self.content = ""
        self.children = {}  # Map child name to FileNode

class FileSystem:
    def __init__(self):
        self.root = FileNode()
    
    def _get_node(self, path):
        """Helper to traverse to the node at given path."""
        if path == "/":
            return self.root
            
        curr = self.root
        # Skip first "/" and split path
        parts = path[1:].split("/")
        
        for part in parts:
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr
    
    def ls(self, path: str) -> List[str]:
        """List all files and directories in given path."""
        node = self._get_node(path)
        if not node:
            return []
            
        # If it's a file, return just the filename
        if node.is_file:
            return [path.split("/")[-1]]
            
        # For directory, return sorted list of all children
        return sorted(node.children.keys())
    
    def mkdir(self, path: str) -> None:
        """Create a directory, will create parent directories if they don't exist."""
        curr = self.root
        # Skip first "/" and split path
        parts = path[1:].split("/")
        
        for part in parts:
            if part not in curr.children:
                curr.children[part] = FileNode()
            curr = curr.children[part]
    
    def addContentToFile(self, filePath: str, content: str) -> None:
        """Add/append content to a file. Create the file if it doesn't exist."""
        curr = self.root
        # Skip first "/" and split path
        parts = filePath[1:].split("/")
        
        # Navigate to parent directory
        for part in parts[:-1]:
            if part not in curr.children:
                curr.children[part] = FileNode()
            curr = curr.children[part]
        
        # Create/update file
        filename = parts[-1]
        if filename not in curr.children:
            curr.children[filename] = FileNode()
        file_node = curr.children[filename]
        file_node.is_file = True
        file_node.content += content
    
    def readContentFromFile(self, filePath: str) -> str:
        """Read and return the content of a file."""
        node = self._get_node(filePath)
        if not node or not node.is_file:
            return ""
        return node.content


# Test cases
def test_filesystem():
    fs = FileSystem()
    
    # Test 1: List empty root directory
    print("Test 1: List empty root")
    print(fs.ls("/"))  # Should print []
    
    # Test 2: Create and list directories
    print("\nTest 2: Create and list directories")
    fs.mkdir("/dir1")
    fs.mkdir("/dir2")
    print(fs.ls("/"))  # Should print ['dir1', 'dir2']
    
    # Test 3: Create nested directories
    print("\nTest 3: Create nested directories")
    fs.mkdir("/dir1/subdir1")
    print(fs.ls("/dir1"))  # Should print ['subdir1']
    
    # Test 4: Create and read file
    print("\nTest 4: Create and read file")
    fs.addContentToFile("/dir1/file1.txt", "Hello")
    fs.addContentToFile("/dir1/file1.txt", " World")
    print(fs.readContentFromFile("/dir1/file1.txt"))  # Should print "Hello World"
    
    # Test 5: List directory with both files and subdirectories
    print("\nTest 5: List mixed directory")
    print(fs.ls("/dir1"))  # Should print ['file1.txt', 'subdir1']
    
    # Test 6: List file (should return just filename)
    print("\nTest 6: List file path")
    print(fs.ls("/dir1/file1.txt"))  # Should print ['file1.txt']
    
    # Test 7: Create file in nested directory
    print("\nTest 7: Create file in nested directory")
    fs.addContentToFile("/dir1/subdir1/file2.txt", "Nested file")
    print(fs.readContentFromFile("/dir1/subdir1/file2.txt"))  # Should print "Nested file"
    
    # Test 8: List nested directory
    print("\nTest 8: List nested directory")
    print(fs.ls("/dir1/subdir1"))  # Should print ['file2.txt']
    
    # Test 9: Read non-existent file
    print("\nTest 9: Read non-existent file")
    print(fs.readContentFromFile("/nonexistent.txt"))  # Should print ""
    
    # Test 10: List non-existent path
    print("\nTest 10: List non-existent path")
    print(fs.ls("/nonexistent"))  # Should print []

if __name__ == "__main__":
    test_filesystem()