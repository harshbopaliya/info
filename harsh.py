from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns
from rich.padding import Padding

# Initialize console with record=True
console = Console(width=180, record=True)  # Added record=True

# Create main tree
tree = Tree("👋 [link=https://www.linkedin.com/in/harshbopaliya2003/]Harsh Bopaliya", guide_style="bold cyan")

# Add education
education = tree.add("🎓 Education", guide_style="green")
education.add("🎓 Bachelor of Engineering in Computer Engineering | CGPA: 8.02/10.0")
education.add("🎓 Ahmedabad Institute of Technology | Expected Graduation: June 2025 | Ahmedabad, India")

# Add skills
skills = tree.add("💻 Technical Skills", guide_style="green")
programming = skills.add("💻 Programming")
programming.add("Python (Pandas, NumPy, Scikit-Learn)")
programming.add("SQL, JavaScript (React, Node.js), MERN Stack")

web = skills.add("🌐 Web Development")
web.add("HTML, CSS, JavaScript, MERN Stack (MongoDB, Express.js, React, Node.js)")

ml = skills.add("🤖 Machine Learning & Data Science")
ml.add("Supervised & Unsupervised Learning, Predictive Analytics, Data Visualization")
ml.add("Deep Learning (TensorFlow, Keras), Naive Bayes")

tools = skills.add("🔧 Tools & Technologies")
tools.add("Power BI, Excel, Flask")

math = skills.add("📊 Mathematics")
math.add("Linear Algebra, Calculus, Probability & Statistics")

# Add experience
experience = tree.add("💼 Experience", guide_style="green")
ibm = experience.add("IBM SkillBuild CSRBOX | Data Analysis Intern")
ibm.add("🔹 Credit Card Dashboard in Power BI, integrating SQL queries for analytics.")
ibm.add("🔹 Achieved 85% accuracy in customer behavior prediction models.")

csr = experience.add("IBM SkillBuild CSRBOX | Data Analysis Intern")
csr.add("🔹 Developed Madhav Store Sales Dashboard, improving inventory management by 15%.")

code = experience.add("Code Unnati Program | Student")
code.add("🔹 Completed training in ML, Deep Learning, Computer Vision, IoT, SAP ABAP on BTP.")

hackathon = experience.add("Smart India Hackathon | Team Member")
hackathon.add("🔹 Built a financial assistance website using HTML, CSS, and JavaScript.")

# Create about panel with matching width
about = """
I'm a student at Ahmedabad Institute of Technology pursuing a Bachelor of Engineering in Computer Engineering.
I've gained technical experience through internships in data analysis and machine learning. 
Some of my projects include developing real-time dashboards in Power BI and building prediction models.
I'm passionate about AI and ML, and I'm constantly exploring new opportunities to grow my skills.
"""

# Create panel with padding and matching width
panel = Panel(
    Padding(about, (1, 2)),
    title="[b]Hello! 👋",
    box=box.DOUBLE,
    border_style="blue",
    width=85
)

# Create balanced columns
layout = Columns(
    [panel, tree],
    equal=True,
    expand=False,
    padding=(0, 2)
)

# Print with padding
console.print()
console.print(layout)
console.print()

# Save as HTML
CONSOLE_HTML_FORMAT = """
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)