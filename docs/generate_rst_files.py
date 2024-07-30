import os

# extract the information from folder snippets that is required to build snippets.rst

# incomplete, still an old attempt
# TODO: instead of generating an rst file per module, produce snippets.rst directly
# TODO: there must be an existing way to do this more efficiently and automatically

# Directory where the Python modules are located
module_dir = '../snippets'

# Directory where Sphinx .rst files will be stored
rst_dir = 'source'

# List all Python files in the module directory
for filename in os.listdir(module_dir):
    if filename.endswith('.py'):
        module_name = filename[:-3]  # Remove the .py extension
        rst_filename = f'{module_name}.rst'
        rst_file_path = os.path.join(rst_dir, rst_filename)

        with open(rst_file_path, 'w') as f:
            f.write(f'{module_name}\n')
            f.write(f'{"=" * len(module_name)}\n\n')
            f.write(f'.. automodule:: snippets.{module_name}\n')
            f.write('    :members:\n')

print(f"RST files generated in {rst_dir}")
