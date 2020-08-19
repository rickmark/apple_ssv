



class File(object):
    _parent: 'Directory'
    _name: str
    _properties: dict

    def __init__(self, name: str, parent: 'Directory', properties=None):
        if properties is None:
            properties = {}

        self._name = name
        self._properties = properties
        self._parent = parent

    @property
    def parent(self) -> 'Directory':
        return self._parent


class Directory(File):
    _children: dict

    def __init__(self, name: str, parent=None, properties=None):
        if parent is None:
            if name is '.':
                parent = self
            else:
                raise NotImplementedError()

        super().__init__(name, parent, properties)

    @property
    def children(self):
        return self._children.values()

    def add_file(self, name: str, properties=None):
        self._children[name] = File(name, self, properties)

    def add_directory(self, name: str, properties=None):
        self._children[name] = Directory(name, self, properties)

    def navigate(self, path) -> File:
        if path is '.':
            return self
        if path is '..':
            return self._parent
        if self._children[path] is not None:
            return self._children[path]

        raise NotADirectoryError()


def parse_file(path):
    defaults = {}


    with open(path, "r") as file:
        line = file.readline()

        while line:
            # Ignore completely empty lines and those with comments
            if not line.isspace() and not line.startswith('#'):
                full_directive = ''
                # Lines with continuation will end with a \
                while not line.endswith('\\'):
                    full_directive += line + ' '
                    line = file.readline()

                # Directives start with /
                if full_directive.startswith('/set'):
                    # TODO: The /set directive modifies defaults

                # Files are added when the line starts with whitespace
                if full_directive.startswith((' ', '\t')):
                    pass

                # TODO: Line is a '.'

                # Directories start with the name of the directory and upon creation
                #  the directory is navigated too