import os

def parse_structure(structure):
    lines = structure.split('\n')
    parsed = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('└') or line.startswith('├'):
            continue
        depth = line.count('│   ')
        name = line.split('─ ')[-1] if '─ ' in line else line.strip()
        parsed.append((depth, name))
    return parsed

def create_structure(structure, base_path='.'):
    parsed = parse_structure(structure)
    current_path = [base_path]
    
    for depth, name in parsed:
        while len(current_path) > depth + 1:
            current_path.pop()
        
        if name.endswith('/'):
            # Es un directorio
            dir_path = os.path.join(*current_path, name.rstrip('/'))
            os.makedirs(dir_path, exist_ok=True)
            current_path.append(name.rstrip('/'))
        else:
            # Es un archivo
            file_path = os.path.join(*current_path, name)
            dir_path = os.path.dirname(file_path)
            os.makedirs(dir_path, exist_ok=True)
            open(file_path, 'a').close()

def main():
    input_file = 'estructura.txt'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            structure = f.read()
        
        create_structure(structure)
        print(f"Estructura creada con éxito a partir de {input_file}")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {input_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
