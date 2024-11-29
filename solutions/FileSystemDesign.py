class FileNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}  # Map of child name to FileNode
        self.parent = parent

class FileSystem:
    def __init__(self):
        # Create root directory '/'
        self.root = FileNode("/")
        self.current = self.root
    
    def mkdir(self, dirname):
        """Create a new directory in the current directory."""
        if dirname in self.current.children:
            print(f"Directory {dirname} already exists")
            return
        
        # Create new directory node with current directory as parent
        new_dir = FileNode(dirname, self.current)
        self.current.children[dirname] = new_dir
    
    def ls(self):
        """List all directories in current directory."""
        return sorted(self.current.children.keys())
    
    def cd(self, dirname):
        """Change current directory. Supports '..' to move up one level."""
        if dirname == "..":
            if self.current.parent:  # Can't go up from root
                self.current = self.current.parent
            return
        
        if dirname not in self.current.children:
            print(f"Directory {dirname} does not exist")
            return
        self.current = self.current.children[dirname]
    
    def pwd(self):
        """Print working directory - full path from root."""
        path = []
        current = self.current
        
        # Traverse up to root collecting directory names
        while current != self.root:
            path.append(current.name)
            current = current.parent
            
        # Handle root directory case
        if not path:
            return "/"
            
        # Build path string
        return "/" + "/".join(reversed(path))


# Example usage
def test_filesystem():
    fs = FileSystem()
    print("Initial pwd:", fs.pwd())  # /
    
    fs.mkdir("documents")
    print("After mkdir documents, ls:", fs.ls())  # ['documents']
    
    fs.cd("documents")
    print("After cd documents, pwd:", fs.pwd())  # /documents
    
    fs.mkdir("photos")
    fs.mkdir("work")
    print("After creating subdirs, ls:", fs.ls())  # ['photos', 'work']
    
    fs.cd("photos")
    print("Current path:", fs.pwd())  # /documents/photos
    
    fs.cd("..")
    print("After cd .., pwd:", fs.pwd())  # /documents
    
    # Test error cases - now prints messages instead of raising exceptions
    fs.mkdir("photos")  # Should print directory already exists
    fs.cd("nonexistent")  # Should print directory doesn't exist

if __name__ == "__main__":
    test_filesystem()