# Let's create a text file containing the context information

context_text = """
1. User owns a grocery store and manages an inventory of goods sold daily.
2. User wants to apply object-oriented programming (OOP) concepts to solve business problems.
3. User wants to write a mystery novel.
4. User completed a master's in Computer Information Systems and started working at Nycasoft Inc. as a computer programmer on STEM OPT. They have gained experience with different technologies, paving the path toward data analytics. They are now a data scientist with AI and DevOps skills.
"""

# Saving the context to a text file
file_path = '/mnt/data/user_context.txt'
with open(file_path, 'w') as file:
    file.write(context_text)

print(file_path)
