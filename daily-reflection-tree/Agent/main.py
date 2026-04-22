import json
import os

def load_tree(file_name):
    # Adjust path to find the json in the /tree/ folder
    base_path = os.path.dirname(os.path.abspath(__file__))
    tree_path = os.path.join(base_path, '..', 'tree', file_name)
    with open(tree_path, 'r') as f:
        return json.load(f)

def run_reflection():
    try:
        tree = load_tree('reflection-tree.json')
    except FileNotFoundError:
        print("Error: reflection-tree.json not found. Ensure it is in the /tree/ folder.")
        return

    current_node = 'start'
    
    print("=== Daily Reflection Tree Agent ===")
    print("Please select the option that best describes your day.\n")

    while current_node in tree:
        node = tree[current_node]
        
        # Check if we reached the end
        if 'question' not in node:
            print("\n--- Summary ---")
            print(node.get('final_notes', 'Reflection complete.'))
            break
            
        print(f"[{node['axis']}] {node['question']}")
        options = list(node['options'].keys())
        
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
            
        while True:
            try:
                choice = int(input("\nYour choice (number): ")) - 1
                if 0 <= choice < len(options):
                    selected_text = options[choice]
                    current_node = node['options'][selected_text]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print("-" * 20)

if __name__ == "__main__":
    run_reflection()