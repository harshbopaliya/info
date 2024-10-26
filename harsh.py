from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Create console with wider width to accommodate horizontal layout
console = Console(record=True, width=200)  # Increased width for horizontal layout

# Create the tree structure for your skills and interests
tree = Tree(":wave: [link=https://www.linkedin.com/in/harshbopaliya2003/]Harsh Bopaliya", guide_style="bold cyan")
education_tree = tree.add(":mortar_board: Education", guide_style="green")
education_tree.add("🎓 Bachelor of Engineering in Computer Engineering | CGPA: 8.02/10.0")
education_tree.add("🎓 Ahmedabad Institute of Technology | Expected Graduation: June 2025 | Ahmedabad, India")

skills_tree = tree.add(":computer: Technical Skills", guide_style="green")
programming_tree = skills_tree.add("💻 Programming")
programming_tree.add("Python (Pandas, NumPy, Scikit-Learn)")
programming_tree.add("SQL, JavaScript (React, Node.js), MERN Stack")

web_tree = skills_tree.add("🌐 Web Development")
web_tree.add("HTML, CSS, JavaScript, MERN Stack (MongoDB, Express.js, React, Node.js)")

ml_tree = skills_tree.add("🤖 Machine Learning & Data Science")
ml_tree.add("Supervised & Unsupervised Learning, Predictive Analytics, Data Visualization")
ml_tree.add("Deep Learning (TensorFlow, Keras), Naive Bayes")

tools_tree = skills_tree.add("🔧 Tools & Technologies")
tools_tree.add("Power BI, Excel, Flask")

math_tree = skills_tree.add("📊 Mathematics")
math_tree.add("Linear Algebra, Calculus, Probability & Statistics")

experience_tree = tree.add(":briefcase: Experience")
ibm_tree = experience_tree.add("IBM SkillBuild CSRBOX | Data Analysis Intern")
ibm_tree.add("🔹 Credit Card Dashboard in Power BI, integrating SQL queries for analytics.")
ibm_tree.add("🔹 Achieved 85% accuracy in customer behavior prediction models.")

csr_tree = experience_tree.add("IBM SkillBuild CSRBOX | Data Analysis Intern")
csr_tree.add("🔹 Developed Madhav Store Sales Dashboard, improving inventory management by 15%.")

code_tree = experience_tree.add("Code Unnati Program | Student")
code_tree.add("🔹 Completed training in ML, Deep Learning, Computer Vision, IoT, SAP ABAP on BTP.")

hackathon_tree = experience_tree.add("Smart India Hackathon | Team Member")
hackathon_tree.add("🔹 Built a financial assistance website using HTML, CSS, and JavaScript.")

# About section panel
about = """\
I'm a student at Ahmedabad Institute of Technology pursuing a Bachelor of Engineering in Computer Engineering.
I've gained technical experience through internships in data analysis and machine learning. 
Some of my projects include developing real-time dashboards in Power BI and building prediction models.
I'm passionate about AI and ML, and I'm constantly exploring new opportunities to grow my skills.
"""

# Create panel with adjusted width
panel = Panel.fit(
    about, 
    box=box.DOUBLE, 
    border_style="blue", 
    title="[b]Hello! :wave:", 
    width=80  # Adjusted width for better horizontal balance
)

# Create columns with the panel and tree side by side
# Using renderables parameter for better horizontal layout
columns = Columns(
    [panel, tree],
    equal=True,
    expand=True
)

# Print the columns
console.print(columns)

# Save the output to an HTML file
CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
