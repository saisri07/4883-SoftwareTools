import csv # to read the csv file
import random  # to generate the random interger 

data = []

# Read the CSV file
with open('family_tree.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the column name
    for row in reader:
        data.append(row)

# Generate the dot file
with open('family_tree.dot', 'w') as file:
    file.write('digraph FamilyTree {\n')
    file.write('node [ shape = "rect"];\n')  # sets shape of the node to rectangle
    file.write('rankdir="TB";\n')  # Set the orientation to top-to-bottom

    # Get unique clans
    clans = list(set(row[14] for row in data if row[14]))

    # Generate random color for each clan
    # random integer is used to generate random clor
    clan_colors = {}
    for clan in clans:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        clan_colors[clan] = color

    # Assign names to clans
    clan_names = {}
    for row in data:
        clan_id = row[14]
        if clan_id not in clan_names:
            clan_names[clan_id] =  f'clan {len(clan_names) + 1}'

    # Write the nodes
    for row in data:
        node_id = row[0]
        name = row[1]
        gender = row[2]
        byear = row[4]
        dyear = row[5]
        spouse_id = row[11]
        clan_id = row[14]



      # To display the information in the node
        label_parts = [name]
        if gender == 'M':
            label_parts.append('(Male)')
        elif gender == 'F':
            label_parts.append('(Female)')
        if byear:
            label_parts.append(f'Birth Year: {byear}')
        if dyear:
            label_parts.append(f'Death Year: {dyear}')
        if spouse_id:
            spouse_name = next((row[1] for row in data if row[0] == spouse_id), '')
            label_parts.append(f'Spouse: {spouse_name}')
        if clan_id:
            clan_name = clan_names[clan_id]
            label_parts.append(f'Clan: {clan_name}')

        label = '\\n'.join(label_parts)

        # Determine the border of the color based on the clan
      
        if clan_id in clan_colors: 
            border_color = clan_colors[clan_id]
            file.write(f'  {node_id} [label="{label}", color="{border_color}", style="filled", fillcolor="white"];\n')
        else:
            file.write(f'  {node_id} [label="{label}"];\n')

    # Write the edges 
    for row in data:
        node_id = row[0]
        spouse_id = row[11]
        parent_id1 = row[12]
        parent_id2 = row[13]
        if spouse_id:
            file.write(f'  {node_id} -> {spouse_id} [label="spouse", dir="none"];\n')
            
        if parent_id1:
            file.write(f'  {parent_id1} -> {node_id} [label="child"];\n')
            file.write(f'  {{rank=same; {parent_id1}; {parent_id2}}};\n')
        
    file.write('}')
