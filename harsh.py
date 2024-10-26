from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns
from rich.padding import Padding

# Initialize console with record=True
console = Console(width=120, record=True)

# Create main tree
tree = Tree("👋 [link=https://www.linkedin.com/in/harshbopaliya2003/]Harsh Bopaliya", guide_style="bold cyan")

# Add education
education = tree.add("🎓 [bold yellow]Education", guide_style="green")
education.add("[b yellow]B.E. in Computer Engineering | CGPA: 8.02/10.0")
education.add("[b yellow]Ahmedabad Institute of Technology | Graduation: June 2025")

# Add skills
skills = tree.add("💻 [bold yellow]Skills", guide_style="green")
skills.add("[cyan]Python, SQL, JavaScript (React, Node.js)")
skills.add("[cyan]MERN Stack, Power BI, Flask")
skills.add("[cyan]Machine Learning, Data Visualization")

# Add experience
experience = tree.add("💼 [bold yellow]Experience", guide_style="green")
experience.add("[bold red]Data Analysis Intern | IBM CSRBOX")
experience.add("🔹 [green]Built dashboards in Power BI & SQL")

experience.add("[bold red]Code Unnati Program | ML Training")
experience.add("🔹 [green]Completed modules in ML & Computer Vision")

# Create about panel with matching width
about = """
[cyan]Engineering student with experience in data analysis and machine learning.
Created dashboards and predictive models, passionate about AI and continuous learning.[/cyan]
"""

# Create panel with padding and matching width
panel = Panel(
    Padding(about, (1, 2)),
    title="[bold yellow]Hello! 👋",
    box=box.DOUBLE,
    border_style="blue",
    width=60
)

# Create balanced columns layout horizontally
layout = Columns(
    [panel, tree],
    equal=True,
    expand=False,
    padding=(0, 2)
)

# Print layout with horizontal alignment
console.print()
console.print(layout)
console.print()

# Save as HTML
CONSOLE_HTML_FORMAT = """
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
